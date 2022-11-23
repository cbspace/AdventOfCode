Ok here we go, attempting AOC in 64 bit assembly using NASM. Although NASM is cross platform the code will be calling Linux syscalls directly and therefore will be limited to Linux ELF format.

Requires:

The NASM assembler: `sudo apt install nasm`

LD linker: `sudo apt install build-essential`

To build and run (e.g day1-1.asm):

`./run day1-1`