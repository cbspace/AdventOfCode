    global _start

    section .text

    %include "string.asm"

    _start:
        mov     rbx, 0            ; total
        mov     rbp, numbers      ; pointer to number to write
        mov     r12, length       ; length of input array
        xor     r13, r13          ; counter
    
    .add_loop:
        add     rbx, [rbp]
        add     rbp, 8            ; move pointer
        add     r13, 8            ; increment counter
        cmp     r12, r13
        jne     .add_loop

        mov     [total], rbx      ; save total
        mov     rsi, [total]      ; load total

        call    int_to_string
        mov     rsi, result_str
        call    print

        mov     rsi, newline
        call    print

    .exit:
        mov       rax, 60         ; system call for exit
        xor       rdi, rdi        ; exit code 0
        syscall                   ; invoke operating system to exit

    section .data
        ;Let's do the simple example of 4 numbers
        numbers:    dq 10, 20, 30, 63
        length:     equ $-numbers
        newline:    db 10
    
    section .bss
        total       resq 1
        result_str  resb 20

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