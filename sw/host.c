//#include "isp32_mpu/memory_map.h"
//#include "uart.h"

//static ns16550_pio_t * pio = (ns16550_pio_t *)(void*)NS16550_AP_BASE;
#include "verif_utils.h"     // for info, error, printm, pex_done, tmt_write_entry

void main() {
    print("host main.c done\n");
    //uart_txline(pio,"Host Main Begin\n");
    //uart_txline(pio,"AP DONE\n"); 
}
