DOVER_DIR = /home2/mikes/dover-repos/dover-hw/SOC/verif

COMMON_INCLUDE = -I tests/common -I $(DOVER_DIR)/tests/common/dover-os/common
HOST_INCLUDE =

COMMON_SOURCE += $(DOVER_DIR)/tests/common/dover-os/common/ns16550.c 
COMMON_SOURCE += $(DOVER_DIR)/tests/common/dover-os/common/snprintf.c 
COMMON_SOURCE += $(DOVER_DIR)/tests/common/dover-os/common/vsnprintf.c 
COMMON_SOURCE += $(DOVER_DIR)/tests/common/dover-os/common/string.c 
COMMON_SOURCE += $(DOVER_DIR)/tests/common/uart.c 


HOST_GCCPREFIX  = riscv32-unknown-elf
HOST_GCCDEFINES = -DMEM_MB=$(MEM_MB)
HOST_MCPU       = 
HOST_LDARCH     = -melf32lriscv
HOST_LDLIBS     =


HOST_GCC_TOOL       = ${HOST_GCCPREFIX}-gcc
# -g puts debug information in the object file
#HOST_GCC_SW         = ${HOST_MCPU} ${HOST_GCCDEFINES} -nostartfiles -nostdlib -static -g
HOST_GCC_SW         = ${HOST_MCPU} ${HOST_GCCDEFINES} -nostartfiles -static -g -O

HOST_ASM_TOOL       = ${HOST_GCCPREFIX}-as
HOST_ASM_SW         = -D ${HOST_MCPU}

HOST_LD_TOOL        = ${HOST_GCCPREFIX}-ld
#HOST_LD_SW          = ${HOST_LDARCH} -nostdlib -static ${HOST_LDLIBS}
HOST_LD_SW          = ${HOST_LDARCH} -static ${HOST_LDLIBS}

HOST_OBJDUMP_TOOL   = ${HOST_GCCPREFIX}-objdump 
HOST_OBJDUMP_SW     =

HOST_OBJCOPY_TOOL   = ${HOST_GCCPREFIX}-objcopy 
HOST_OBJCOPY_SW     = 

HOST_COMMON_SOURCE := 
#tests/common/asm_utils.s

# TODO create dynamic common source listing 
HOST_COMMON_SOURCE := $(DOVER_DIR)/tests/common/asm_helpers.S 

# Take default host_boot_entry.S if none exists in test
###ifeq ($(wildcard tests/$(TEST)/host_boot_entry.S),)
    HOST_BROM_SOURCE := ./host_boot_entry.S
###endif

# Take default host_boot.c if none exists in test
###ifeq ($(wildcard tests/$(TEST)/host_boot.c),)
    HOST_BROM_SOURCE := $(HOST_BROM_SOURCE) ./host_boot.c
###endif

# Take any additional test specific host_boot source and the common source files
HOST_BROM_SOURCE := $(HOST_BROM_SOURCE) $(HOST_COMMON_SOURCE)

# Take default host_entry.S if none exists in test
###ifeq ($(wildcard tests/$(TEST)/host_entry.S),)
    HOST_SRAM_SOURCE := ./host_entry.S
###endif

# Take default host.c if none exists in test
###ifeq ($(wildcard tests/$(TEST)/host.c),)
    HOST_SRAM_SOURCE := $(HOST_SRAM_SOURCE) ./host.c
###endif

# Take any additional test specific host source and the common source files
HOST_SRAM_SOURCE := $(HOST_SRAM_SOURCE) $(HOST_COMMON_SOURCE)
HOST_SRAM_SOURCE := $(filter-out $(HOST_BROM_SOURCE),$(HOST_SRAM_SOURCE)) $(HOST_COMMON_SOURCE)

HOST_BROM_LD_SCRIPT := tests/common/host_boot.ld 
HOST_SRAM_LD_SCRIPT := tests/common/host.ld

all:
	riscv32-unknown-elf-gcc \
		-DMEM_MB=1 \
		-nostartfiles -nostdlib -static -g \
		-I /home2/mikes/dover-repos/dover-hw/CoreGuard/verif/cg/src/shared \
		-I /home2/mikes/dover-repos/dover-os \
		-I /home2/mikes/dover-repos/isp-headers \
		-I /home2/mikes/dover-repos/dover-hw/CoreGuard/TPU/verif/src/shared \
		-I /home2/mikes/dover-repos/isp-headers/isp32_mpu \
		-T host.ld \
		host_boot_entry.S \
		/home2/mikes/dover-repos/dover-hw/CoreGuard/verif/cg/src/shared/utils.rv32.S \
		/home2/mikes/dover-repos/dover-hw/CoreGuard/verif/cg/src/shared/verif_utils.c \
		/home2/mikes/dover-repos/dover-os/common/vsnprintf.c \
		host.c \
		-o host.out
	riscv32-unknown-elf-objcopy -O binary host.out host.bin
	hexdump -v -e'1/1 "%02x""\n"' host.bin > host.hex
	riscv32-unknown-elf-objdump -dS host.out > host.lst
	riscv32-unknown-elf-objdump -s -j .rodata -j .sdata host.out >> host.lst
