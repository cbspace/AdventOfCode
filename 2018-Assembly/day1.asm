    global _start

    section .text

    %include "string.asm"

    _start:
        mov     rcx, 0
        mov     rdx, numbers              ; pointer to number to write
        mov     r8, length
        xor     r9, r9                    ; counter
    
    .add_loop:
        add     rcx, [rdx]
        add     rdx, 8                    ; move pointer
        add     r9, 8                     ; increment counter
        cmp     r8, r9
        jne     .add_loop

        mov     [total], rcx
        mov     rdi, [total]

        call    itoa
        mov     rsi, itoa_result_str
        call    print

        mov     rsi, newline
        call    print

    .exit:
        mov       rax, 60                 ; system call for exit
        xor       rdi, rdi                ; exit code 0
        syscall                           ; invoke operating system to exit

    section .data
        ;Let's do the simple example of 4 numbers
        numbers:    dq 10, 20, 30, 63
        length:     equ $-numbers
        newline:    db 10
    
    section .bss
        total           resq 1
        itoa_result_str resb 20

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