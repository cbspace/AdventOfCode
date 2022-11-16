section .data
    ;Let's do the simple example of "+1, -2, +3, +1"
    numbers: dw 1, -2, 3, 1 
    length: equ $-numbers

    section .text
        global _start

    _start:
        