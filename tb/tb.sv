// FIXME: add a license header
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
