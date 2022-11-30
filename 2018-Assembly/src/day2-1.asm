    ; Day2 Part 1
    
    global _start

    section .text

    %include     "file.asm"
    %include     "string.asm"

    _start:
        call    file_open

        call    file_read
        mov     rsi, read_buffer
        call    println

        xor     r12, r12                ; number of boxes containing a letter repeated twice
        xor     r13, r13                ; number of boxes containing a letter repeated thre times
        mov     r14, read_buffer        ; pointer to first box_id
        xor     rbx, rbx                ; loop counter

    .loop:
        call    check_box               ; check the current box for repeating characters

    .exit:
        mov     rax, 60                 ; system call for exit
        xor     rdi, rdi                ; exit code 0
        syscall                         ; invoke operating system to exit

    ; Check for repeated characters in box_id pointed to by rdi
    check_box:

        ret

    section .data
        file_path:          db  "./input/day2_test.txt", 0
        newline:            db  10
    
    section .bss
        ; For simplicity this section is aligned @ 8 bytes!
        file_descriptor     resq 1
        read_buffer_len     resq 1
        read_buffer         resb 32
        result_str_len      resq 1          ; for debug
        result_str          resb 32         ; for debug
        ;no_of_duplicates    resq 1
        ;no_of_triplicates   resq 1

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