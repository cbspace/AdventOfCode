    ; Day2 Part 1
    
    global _start

    section .text

    %include     "file.asm"
    %include     "string.asm"
    %include     "array.asm"

    _start:
        mov     qword[no_of_duplicates], 0      ; initialise to 0
        mov     qword[no_of_triplicates], 0     ; initialise to 0
        call    file_open

    .loop:
        call    file_read_line                  ; read a line from file
        test    rax, rax                        ; test return value (characters read)
        jz      .get_answer                     ; if zero exit loop
        mov     rdi, read_buffer                ; load buffer
        call    array_get_unique_8              ; get unique array
        call    check_box                       ; check the current box for repeating characters
        jmp     .loop

    .get_answer:
        mov     rax, [no_of_duplicates]         ; load no of duplicates
        mov     rcx, [no_of_triplicates]        ; load no of triplicates
        mul     rcx                             ; multiply
        mov     qword [answer], rax             ; save answer
        mov     rsi, [answer]                   ; load answer
        call    int_to_string                   ; convert to string
        mov     rsi, result_str                 ; load string
        call    println                         ; print answer
        
    .exit:
        mov     rax, 60                         ; system call for exit
        xor     rdi, rdi                        ; exit code 0
        syscall                                 ; invoke operating system to exit

    ; Check for repeated characters in box_id stored in read_buffer
    ; use unique characters from result_str
    ; updates no_of_duplicates and no_of_triplicates (global)
    check_box:
        xor     r12, r12                        ; duplicate count
        xor     r13, r13                        ; triplicate count
        mov     r14, [result_str_len]           ; counter (length -> 0)
        mov     rsi, result_str                 ; pointer to unique characters
    .check_loop:
        mov     rdi, read_buffer                ; pointer to box_id
        mov     rbx, [rsi]                      ; get character to find
        and     rbx, 000000ffh                  ; mask high bytes
        call    array_count_8                   ; get character count
        cmp     rax, 2                          ; compare no of characters against 2
        jnge    .next                           ; less than 2 so move on
        jne     .test_for_3                     ; not equal to 2 so test for 3
        inc     r12                             ; increase duplicate count
    .test_for_3:
        cmp     rax, 3                          ; do we have 3 characters?
        jne     .next                           ; no so move on
        inc     r13                             ; increment triplicate count
    .next:
        inc     rsi                             ; increment pointer
        dec     r14                             ; decrement counter
        jnz     .check_loop                     ; keep loopoing

        cmp     r12, 1                          ; compare no of duplicates against 1
        jnge    .no_of_triplicates              ; if not >= than 1 move on
        inc     qword [no_of_duplicates]        ; increment number of duplicates
    .no_of_triplicates:
        cmp     r13, 1                          ; compare no of triplicates against 1
        jnge    .done                           ; if not >= than 1 move on
        inc     qword [no_of_triplicates]       ; increment number of triplicates
    .done:
        ret


    section .data
        file_path:          db  "./input/day2_input.txt", 0
        newline:            db  10
    
    section .bss
        ; For simplicity this section is aligned @ 8 bytes!
        file_descriptor     resq 1
        read_buffer_len     resq 1
        read_buffer         resb 32
        result_str_len      resq 1
        result_str          resb 32
        no_of_duplicates    resq 1
        no_of_triplicates   resq 1
        answer              resq 1

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