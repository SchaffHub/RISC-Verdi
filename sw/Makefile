#all:
#	riscv32-unknown-elf-gcc \
#		-DMEM_MB=1 \
#		-nostartfiles -nostdlib -static -g \
#		-I /home2/mikes/dover-repos/dover-hw/CoreGuard/verif/cg/src/shared \
#		-I /home2/mikes/dover-repos/dover-os \
#		-I /home2/mikes/dover-repos/isp-headers \
#		-I /home2/mikes/dover-repos/dover-hw/CoreGuard/TPU/verif/src/shared \
#		-I /home2/mikes/dover-repos/isp-headers/isp32_mpu \
#		-T host.ld \
#		host_boot_entry.S \
#		/home2/mikes/dover-repos/dover-hw/CoreGuard/verif/cg/src/shared/utils.rv32.S \
#		/home2/mikes/dover-repos/dover-hw/CoreGuard/verif/cg/src/shared/verif_utils.c \
#		/home2/mikes/dover-repos/dover-os/common/vsnprintf.c \
#		host.c \
#		-o host.out
#	riscv32-unknown-elf-objcopy -O binary host.out host.bin
#	hexdump -v -e'1/1 "%02x""\n"' host.bin > host.hex
#	riscv32-unknown-elf-objdump -dS host.out > host.lst
#	riscv32-unknown-elf-objdump -s -j .rodata -j .sdata host.out >> host.lst

all: host.lst host.hex

REMOTE_DIR =	/home2/mikes/dover-repos

HOST_SOURCE =	$(REMOTE_DIR)/dover-hw/CoreGuard/verif/cg/src/shared/utils.rv32.S \
		$(REMOTE_DIR)/dover-hw/CoreGuard/verif/cg/src/shared/verif_utils.c \
		$(REMOTE_DIR)/dover-os/common/vsnprintf.c \
		host_boot_entry.S \
		host.c

HOST_INCLUDE =  -I $(REMOTE_DIR)/dover-hw/CoreGuard/verif/cg/src/shared \
		-I $(REMOTE_DIR)/dover-os \
		-I $(REMOTE_DIR)/isp-headers \
		-I $(REMOTE_DIR)/dover-hw/CoreGuard/TPU/verif/src/shared \
		-I $(REMOTE_DIR)/isp-headers/isp32_mpu

HOST_LD_SCRIPT = host.ld

MEM_MB         = 1
GCC_DEFINES    = -DMEM_MB=$(MEM_MB)
GCC_PREFIX     = riscv32-unknown-elf

GCC_TOOL       = ${GCC_PREFIX}-gcc
GCC_SW         = ${GCC_DEFINES} -nostartfiles -nostdlib -static -g

OBJDUMP_TOOL   = ${GCC_PREFIX}-objdump 

OBJCOPY_TOOL   = ${GCC_PREFIX}-objcopy 

host.out : $(HOST_LD_SCRIPT) $(HOST_SOURCE)
	$(GCC_TOOL) $(GCC_SW) $(HOST_INCLUDE) \
		-T $(HOST_LD_SCRIPT) $(HOST_SOURCE) -o $@ 

%.lst : %.out
	$(OBJDUMP_TOOL) -dS $^ > $@
	-$(OBJDUMP_TOOL) -s -j .rodata -j .sdata $^ >> $@

%.bin : %.out
	$(OBJCOPY_TOOL) -O binary $^ $@

%.hex : %.bin
	hexdump -v -e'1/1 "%02x""\n"' $^ > $@
	@echo ""

clean:
	rm -f *.lst
	rm -f *.hex
	rm -f *.out
	rm -f *.bin
