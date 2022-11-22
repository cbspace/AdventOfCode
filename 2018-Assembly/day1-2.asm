    global _start

    section .text

    %include "string.asm"

    _start:
        mov     rbx, 0                  ; total
        mov     r12, length             ; length of input array
        mov     r14, freq_array         ; pointer to freq_array
        mov     rbp, 0                  ; freq_array_length
    .loop_init:
        mov     r15, numbers            ; pointer to number
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

        ; mov     rsi, rbx                ; temp print
        ; call    int_to_string
        ; mov     rsi, result_str
        ; call    println

        cmp     r12, r13                ; test if end of list
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
        xor       r10, r10              ; counter = 0
        mov       r11, freq_array       ; pointer to array
    .loop:
        cmp       r10, rbp              ; are we at the end of array?
        je        .not_found            ; yes we are so leave
        mov       r8, [r11]             ; load array value
        cmp       r8, rbx               ; compare to input value
        je        .found
        add       r10, 8                ; increase counter
        add       r11, 8                ; increase pointer
        jmp       .loop
    .not_found:
        mov       rax, 0                ; not found, return 0
        ret
    .found:
        mov       rax, 1                ; return 1
        ret

    section .data
        ; This is a bit of a hack, adding the (reformatted) input file
        ; as an include. The next step is to open the file using assembley!
        numbers:    dq 3, 3, 4, -2, -4
        ;numbers:
        ;%include "day1_input.txt"
        length:     equ $-numbers
        newline:    db 10
    
    section .bss
        ; For simplicity this section is aligned @ 8 bytes!
        result_str_len  resq 1
        result_str      resb 24
        freq_array      resq 1000

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