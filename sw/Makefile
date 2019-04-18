all: host.lst host.hex

HOST_SOURCE =	host_boot_entry.S \
		host.c

HOST_INCLUDE =  

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
		-T $(HOST_LD_SCRIPT) $(HOST_SOURCE) -o $@ -lgcc

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
