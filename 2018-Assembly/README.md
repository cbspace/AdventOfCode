Ok here we go, attempting AOC in 64 bit assembly using NASM. Although NASM is cross platform the code will be calling Linux interrupts directly and therefore will be limited to Linux ELF format.

Requires:

The NASM compiler: `sudo apt install nasm`

LD linker: `sudo apt install build-essential`

To build and run (e.g Day1.asm):

`./run day1`