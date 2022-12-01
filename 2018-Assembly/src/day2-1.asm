    ; Day2 Part 1
    
    global _start

    section .text

    %include     "file.asm"
    %include     "string.asm"
    %include     "array.asm"

    _start:
        call    file_open

        call    file_read_line          ; read a line from file
        mov     rsi, read_buffer        ; load buffer
        call    println                 ; print the line

        mov     rdi, read_buffer        ; load buffer
        mov     rbx, 'a'                ; character to find
        call    array_count_8           ; get the count
        mov     [temp_count], rax       ; store the count
        mov     rsi, [temp_count]       ; load count to rsi
        call    int_to_string           ; covert to string
        mov     rsi, result_str         ; load string
        call    println                 ; print

        xor     r12, r12                ; number of boxes containing a letter repeated twice
        xor     r13, r13                ; number of boxes containing a letter repeated thre times
        mov     r14, read_buffer        ; pointer to first box_id
        xor     rbx, rbx                ; loop counter

    .loop:
        mov     rdi, read_buffer
        ;call    check_box               ; check the current box for repeating characters

    .exit:
        mov     rax, 60                 ; system call for exit
        xor     rdi, rdi                ; exit code 0
        syscall                         ; invoke operating system to exit

    ; Check for repeated characters in box_id pointed to by rdi
    ; uses r12 for duplicate count and r13 for triplicate count (global)
    ; uses r8 for duplicate count and r9 for triplicate count (local)
    check_box:
        xor     r8, r8                  ; duplicate count
        xor     r9, r9                  ; triplicate count
        xor     r10, r10                ; counter
    .check_loop:
        xor     r11, r11                ; clear all bits in r11
        mov     r11, [rdi]              ; get character

        ret

    section .data
        file_path:          db  "./input/day2_test.txt", 0
        newline:            db  10
    
    section .bss
        ; For simplicity this section is aligned @ 8 bytes!
        file_descriptor     resq 1
        read_buffer_len     resq 1
        read_buffer         resb 32
        result_str_len      resq 1
        result_str          resb 32
        temp_count          resq 1
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