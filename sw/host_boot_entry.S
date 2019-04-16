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

#define HOST_RAM  0x80000000
#define STACK_RAM (HOST_RAM + 0x00100000)

// ZERO_REG will zero out the integer file registers that you list
// e.g. ZERO_REG 1,2,3,4,5 will zero x1 through x5
.macro ZERO_REG from=0, to=0, rest:vararg
   .if \from
   li x\from, 0
   .endif
   .if \to
   li x\to, 0
   ZERO_REG \rest
   .endif
.endm

.section .text.init,"ax",@progbits
.align 1
.option norvc
.globl host_boot_entry


// RI5CY Interrupts 0-31
.org 0x0
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap
    j bad_trap

// RI5CY Reset
.org 0x80
    j host_boot_entry

.org 0x180
j host_boot_entry

.org 0x200
// Entry point
host_boot_entry:
    // s2 -> ROM header - optional in case we want bits in there
    auipc   s2, 0
    addi    s2, s2, -0x200

    // we skip x18 here, because that's s2, and we need to preserve that
    ZERO_REG 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17
    ZERO_REG 19,20,21,22,23,24,25,26,27,28,29,30,31

    // set up a temporary stack at the top of memory so that C code
    // in the bootloader can function.
    li sp, STACK_RAM
        
    // do the main boot
    jal main

    // Change mtvec to RAM
    li      x1, HOST_RAM 
    csrrw   x0, mtvec, x1

    // Jump to RAM 0x200 address
    li      x1, HOST_RAM + 0x200
    jr      x1

bad_trap:
    j bad_trap
