    ; Day2 Part 1
    
    global _start

    section .text

    %include     "string.asm"
    %define      BOX_ID_LENGTH 6

    _start:
        xor     r12, r12                ; number of boxes containing a letter repeated twice
        xor     r13, r13                ; number of boxes containing a letter repeated thre times
        mov     r12, box_ids            ; pointer to first box_id
        xor     rbx, rbx                ; loop counter

    .loop:
        call    check_box

        mov     rdx, 6                  ; load str len
        mov     rsi, r12                ; load string
        call    print                   ; temp print
        call    printcr

        add     r12, BOX_ID_LENGTH      ; incrememnt the pointer
        add     rbx, BOX_ID_LENGTH      ; increment counter
        cmp     rbx, length             ; check if we reached the end
        jne     .loop

    .exit:
        mov     rax, 60                 ; system call for exit
        xor     rdi, rdi                ; exit code 0
        syscall                         ; invoke operating system to exit

    ; Check for repeated characters in box_id pointed to by rdi
    check_box:

        ret

    section .data
        ; This is a bit of a hack, adding the (reformatted) input file
        ; as an include. The next step is to open the file using assembley!
        box_ids:
        %include        "day2_test.txt"
        length:         equ ($-box_ids)    ; size of box_ids
        newline:        db 10
    
    section .bss
        ; For simplicity this section is aligned @ 8 bytes!
        result_str_len  resq 1
        result_str      resb 24

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