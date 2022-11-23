    ; Day2 Part 1
    
    global _start

    section .text

    %include "string.asm"

    _start:
        

    .exit:
        mov       rax, 60               ; system call for exit
        xor       rdi, rdi              ; exit code 0
        syscall                         ; invoke operating system to exit

    section .data
        ; This is a bit of a hack, adding the (reformatted) input file
        ; as an include. The next step is to open the file using assembley!
        boxids:
        %include "day2_test.txt"
        length:     equ ($-boxids)/6
        newline:    db 10
    
    section .bss
        ; For simplicity this section is aligned @ 8 bytes!
        result_str_len  resq 1
        result_str      resb 24
        freq_array      resq 1000 ; the array is quite large...

; Register usage
; rax - Caller-saved register, Function return values
; rbx - Function-saved register
; rcx - Caller-saved register, Function parameter 4
; rdx - Caller-saved register, Function parameter 3
; rdi - Caller-saved register, Function parameter 1
; rsi - Caller-saved register, Function parameter 2
; rbp - Function-saved register
; rsp - Caller-saved register
; r8  - Caller-saved register, Function parameter 5
; r9  - Caller-saved register, Function parameter 6
; r10 - Caller-saved register
; r11 - Caller-saved register
; r12 - Function-saved register
; r13 - Function-saved register
; r14 - Function-saved register
; r15 - Function-saved register