    global _start

    section .text
    _start:
        mov     rcx, 0
        mov     rdx, numbers              ; pointer to number to write
        mov     r8, length
        xor     r9, r9                    ; counter
    
    .add_loop:
        add     rcx, [rdx]
        add     rdx, 8                    ; move pointer
        add     r9, 8                     ; increment counter
        cmp     r8, r9
        jne     .add_loop

        mov     [total], rcx
        mov     rdi, [total]
        call    itoa
        mov     rsi, itoa_result_str
        call    print

        mov     rsi, newline
        call    print

    .exit:
        mov       rax, 60                 ; system call for exit
        xor       rdi, rdi                ; exit code 0
        syscall                           ; invoke operating system to exit

    ; Print contents of byte at [rsi]
    print:
        mov       rax, 1                  ; system call for write
        mov       rdi, 1                  ; file handle 1 is stdout
        mov       rdx, 2                  ; number of bytes
        syscall
        ret

    ; Integer to ASCII: Convert int64 at RDI to ASCII
    ; and save in itoa_result_str - currently signed only
    itoa:
        mov rbx, 2      ; 2 means 10^2 divisor or 0 - 999 range
        mov rdx, 0
        mov rax, rdi
        mov rcx, 10
        div rcx         ; rax: quotient, rdx: remainder
        add rax, 30h
        mov [itoa_result_str], rax
        add rdx, 30h
        mov [itoa_result_str + 1], rdx
        ret

    ; Take int64 in rsp and return 10^rsp in rax
    ; Fixme - return 0 on overflow
    pow10:
        mov r8, 10
        mov rax, 1
        mul r8
        ret


    section .data
        ;Let's do the simple example of 4 numbers
        numbers:    dq 10, 20, 30, 63
        length:     equ $-numbers
        newline:    db 10
    
    section .bss
        total           resq 1
        itoa_result_str resb 20