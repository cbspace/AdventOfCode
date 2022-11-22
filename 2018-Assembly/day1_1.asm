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

        mov     rsi, rbx          ; load total
        call    int_to_string

        mov     rsi, result_str
        call    print
        mov     rsi, newline
        ;call    print

    .exit:
        mov       rax, 60         ; system call for exit
        xor       rdi, rdi        ; exit code 0
        syscall                   ; invoke operating system to exit

    section .data
        ; This is a bit of a hack, adding the (reformatted) input file
        ; as an include. The next step is to open the file using assembley!
        numbers:
        %include "day1_input.txt"
        length:     equ $-numbers
        newline:    db 10
    
    section .bss
        result_str  resb 21

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