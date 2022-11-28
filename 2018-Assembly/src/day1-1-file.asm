    global _start

    section .text

    %include    "file.asm"
    %include    "string.asm"

    _start:
        call    file_open         ; open input file
        mov     rbx, 0            ; total
        mov     rbp, read_buffer  ; pointer to number
        ;mov     r12, length       ; length of input array
        xor     r13, r13          ; counter
    
    .add_loop:
        call    file_read_line      ; read a line into buffer
        mov     rsi, read_buffer
        call    println

        ; add     rbx, [rbp]        ; add the numbers
        ; add     rbp, 8            ; move pointer
        ; add     r13, 8            ; increment counter
        ; cmp     r12, r13
        ; jne     .add_loop

        ; mov     rsi, rbx          ; load total
        ; call    int_to_string

        ; mov     rsi, result_str
        ; call    println

    .exit:
        mov       rax, 60         ; system call for exit
        xor       rdi, rdi        ; exit code 0
        syscall                   ; invoke operating system to exit

    section .data
        file_path:          db  "./input/day1_input1.txt", 0
        newline:            db 10
    
    section .bss
        ; For simplicity this section is aligned @ 8 bytes!
        file_descriptor     resq 1
        read_buffer_len     resq 1
        read_buffer         resb 64
        result_str_len      resq 1
        result_str          resb 24

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