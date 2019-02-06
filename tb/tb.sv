//
// Copyright 2018-2019 Dover Microsystems, Inc.
// 
// Permission is hereby granted, free of charge, to any person
// obtaining a copy of this software and associated documentation
// files (the "Software"), to deal in the Software without restriction,
// including without limitation the rights to use, copy, modify, merge,
// publish, distribute, sublicense, and/or sell copies of the Software,
// and to permit persons to whom the Software is furnished to do so,
// subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
// HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
// WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
// DEALINGS IN THE SOFTWARE.
//

module tb;

    logic clk_i, rstn_i;
    localparam int CLK_PERIOD = 10;

    top _top
        (
         .clk_i,
         .rstn_i,

         .irq_i(1'b0),
         .irq_id_i(5'b0),
         .irq_ack_o(),
         .irq_id_o(),
         .irq_sec_i(1'b0),

         .sec_lvl_o(),

         .debug_req_i(1'b0),
         .debug_gnt_o(),
         .debug_rvalid_o(),
         .debug_addr_i(15'b0),
         .debug_we_i(1'b0),
         .debug_wdata_i(32'b0),
         .debug_rdata_o(32'b0),

         .fetch_enable_i(1'b1),
         .core_busy_o()
         );

    initial begin
        $readmemh("host.hex", _top.ram_i.dp_ram_i.mem);
        $fsdbDumpvars(0, _top, "+fsdbfile+waves.fsdb");
        clk_i  = '0;
        rstn_i = '0;
        #(CLK_PERIOD*20);
        rstn_i = '1;
        #(CLK_PERIOD*100);
        $finish;
    end

    always #CLK_PERIOD clk_i = ~clk_i;

endmodule
