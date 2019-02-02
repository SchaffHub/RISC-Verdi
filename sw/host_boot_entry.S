// 
// Common PEX Boot Entry
// 
// The objective of this code is to house a generic interrupt and trap 
// jump table that work work for the majority of SOC tests. The code 
// will set up registers to support C for common boot code. 
//

#include "asm_utils.h"
#include "isp32_mpu/memory_map.h"

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

///.org 0x100
// Entry point from user mode (mtvec + 0x000)
///uentry:
///.align 6
///    j bad_trap

// Entry point from supervisor mode (mtvec + 0x040)
///sentry:
///.align 6
///    j bad_trap
        
// Entry point from hypervisor mode (mtvec + 0x080)
///hentry:
///.align 6
///    j bad_trap

// Entry point from machine mode (mtvec + 0x0C0)
///mentry:
///.align 6
///    j bad_trap

// Entry point for NMIs (mtvec + 0x0FC)
///nmi:
///    j bad_trap

// Pulp's RISCY core expects a reset vector table starting at 0x80 for some reason...
.org 0x180
j host_boot_entry

.org 0x200
// Entry point for power-on reset (mtvec + 0x100)
//.org 0x200
host_boot_entry:
    // s2 -> ROM header - optional in case we want bits in there
    auipc   s2, 0
    addi    s2, s2, -0x200

    // we skip x18 here, because that's s2, and we need to preserve that
    ZERO_REG 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17
    ZERO_REG 19,20,21,22,23,24,25,26,27,28,29,30,31

    // set up a temporary stack at the top of memory so that C code in the bootloader
    // can function.
    li sp, SOC_ADDR_HOST_RAM +  SOC_SRAM_STEP
        
    // do the main boot
    jal main

    // Change PEX's mtvec to SRAM3
    li      x1, SOC_ADDR_HOST_RAM 
    csrrw   x0, mtvec, x1

    // Jump to SRAM3 0x200 address
    li      x1, SOC_ADDR_HOST_RAM + 0x200
    jr      x1

bad_trap:
    j bad_trap
