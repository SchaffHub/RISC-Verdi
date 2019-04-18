# RISC-Verdi

RISC-Verdi is a Python application that uses the VC Apps Language link the simulated execution
of a CPU from a Verdi waveform to the source code the CPU is executing.  A graphical user
interface is created by RISC-Verdi using Tk to step forwards and backwards in the source code
much like a very simple debugger.  The application is described in great detail in a paper
and presentation from SNUG Boston 2019.

## Directory Overview
- `Examples` contains TCL and Python example scripts from the SNUG paper.
- `sw` contains the application source code that runs on the CPU in simulation.
- `tb` contains a simple testbench to load the source code, instantiate the CPU, and run the simulation.
- `resources` contains Python modules used in by the RISC-Verdi application.
- `risc-verdi` is the RISC-Verdi application controller code.
- `setup.sh` is a shell script to fetch the RI5CY CPU.

## Getting Started
The build process presented here assumes the use of the Synopsys VCS simulator and the RISC-V
toolchain.  If those are not availble then the appropriate intermediate files have been
provided to sufficiently test drive RISC-Verdi.  Synopsys Verdi is required for RISC-Verdi
to operate properly.  RISC-Verdi uses Python3.

### Fetching RI5CY
The simulation uses the RI5CY CPU core.  RI5CY can be fetched from GitHub by sourcing the
script `setup.sh`.

### Building the Software
To build the software that boot and runs on RI5CY, go to the `sw` directory and type `make`.
The RISC-V toolchain is required for this step.  The make process should produce two files:
`host.lst` and `host.hex`.

### Running the Simulation
To run the simulation, go to the `tb` directory and type `make`.  The simulation should
take no more than a few minutes on a reasonably equipped Linux machine.  The simulation
should produce a file call `waves.fsdb`.

### Launching Verdi
The fsdb file is used to call Verdi or nWave.  For example, type `nWave waves.fsdb` from
the `tb` directory.

### Launching RISC-Verdi
Once a Verdi/nWave window is present, launch RISC-Verdi from the top directory by typing
`./risc-verdi`.  The file `host.lst` should be automatically loaded.  Navigation should
be possible with the next/previous/re-center buttons from the RISC-Verdi application or
by moving the waveform cursor.  Simply press the quit button to exist RISC-Verdi.

## About
RISC-Verdi was authored by Mike Schaffstein at Dover Microsystems.  Special thanks goes to
the team at Dover Microsystems for supporting the open source nature of this material and
for help with key aspects of the build and compile flow.  Thanks also goes out to the SNUG
and Synopsys teams that helped review and refine this material.
