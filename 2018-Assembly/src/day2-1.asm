    ; Day2 Part 1
    
    global _start

    section .text

    %include     "file.asm"
    %include     "string.asm"
    %define      BOX_ID_LENGTH 6

    _start:
        call    file_open

        call    file_read
        mov     rsi, read_buffer
        call    println

        xor     r12, r12                ; number of boxes containing a letter repeated twice
        xor     r13, r13                ; number of boxes containing a letter repeated thre times
        mov     r12, read_buffer        ; pointer to first box_id
        xor     rbx, rbx                ; loop counter

    .loop:
        call    check_box               ; check the current box for repeating characters

        ; mov     rdx, 6                  ; load str len
        ; mov     rsi, r12                ; load string
        ; call    print                   ; temp print
        ; call    printcr



        call    file_close

        add     r12, BOX_ID_LENGTH      ; incrememnt the pointer
        add     rbx, BOX_ID_LENGTH      ; increment counter
        ;cmp     rbx, length             ; check if we reached the end
        ;jne     .loop

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
        read_buffer         resb 1024
        result_str_len      resq 1
        result_str          resb 24
        no_of_duplicates    resq BOX_ID_LENGTH
        no_of_triplicates   resq BOX_ID_LENGTH

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