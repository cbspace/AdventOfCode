    ; Day1 Part 2: It works! This one chugs though, lucky it's written in assembly :)
    ; There's probably a better algorithm to solve this that is more efficient.
    ; Fun fact - This takes 1.95s to run on my machine and the python version takes 25.1s
    
    global _start

    section .text

    %include "file.asm"
    %include "string.asm"

    _start:
        call    file_open               ; open input file
        mov     r15, input_numbers      ; pointer to number
        mov     rbx, 0                  ; counter for number of inputs
    .read_inputs:
        call    file_read_line          ; read a line into buffer
        mov     r12, rax                ; store return value (!EOF)
        mov     rsi, read_buffer        ; load the string
        call    string_to_int           ; convert to int
        mov     [r15], rax              ; store the number
        inc     rbx                     ; increment count
        add     r15, 8                  ; increment pointer
        test    r12, r12                ; test if end of file
        jnz     .read_inputs
        call    file_close              ; close input file
        mov     [input_numbers_len], rbx; store length

        mov     rsi, rbx
        call    int_to_string
        mov     rsi, result_str
        call    println ; see what the length is

        mov     rbx, 0                  ; total
        mov     r14, freq_array         ; pointer to freq_array
        mov     rbp, 0                  ; freq_array_length
    .loop_init:
        mov     r15, input_numbers      ; pointer to number
        xor     r13, r13                ; counter
    .add_loop:
        add     rbx, [r15]              ; increase total
        add     r15, 8                  ; move pointer
        add     r13, 8                  ; increment counter

        call    search_array            ; check if number is in array
        cmp     rax, 1                  ; compare return value
        je      .found                  ; found a match

        mov     [r14], rbx              ; store total in array
        add     r14, 8                  ; move pointer
        add     rbp, 8                  ; increment array length

        cmp     r13, [input_numbers_len]  ; test if end of list
        jne     .add_loop               ; not yet, keep looping
        jmp     .loop_init              ; at end, start list again

    .found:
        mov     rsi, rbx                ; load total
        call    int_to_string           ; convert to string
        mov     rsi, result_str         ; load string
        call    println                 ; print

    .exit:
        mov       rax, 60               ; system call for exit
        xor       rdi, rdi              ; exit code 0
        syscall                         ; invoke operating system to exit

    ; search array and return 1 in rax if found
    search_array:
        test      rbp, rbp              ; is the array empty?
        jz        .not_found            ; yes so leave
        xor       r10, r10              ; counter = 0
        mov       r11, freq_array       ; pointer to array
    .loop:
        mov       r8, [r11]             ; load array value
        cmp       r8, rbx               ; compare to input value
        je        .found
        add       r10, 8                ; increase counter
        add       r11, 8                ; increase pointer
        cmp       r10, rbp              ; are we at the end of array?
        jne       .loop                 ; no, keep going
    .not_found:
        mov       rax, 0                ; not found, return 0
        ret
    .found:
        mov       rax, 1                ; return 1
        ret

    section .data
        file_path:  db  "./input/day1_input.txt", 0
        newline:    db  10
    
    section .bss
        ; For simplicity this section is aligned @ 8 bytes!
        file_descriptor     resq 1
        read_buffer_len     resq 1
        read_buffer         resb 64
        result_str_len      resq 1
        result_str          resb 24
        input_numbers_len   resq 1
        input_numbers       resq 1000      
        freq_array          resq 1000000   ; need a large array


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