    global _start

    section .text
    _start:
        mov     rcx, 30h                  ; ASCII '0'
        mov     rdx, numbers              ; pointer to number to write
        mov     r8, length
        xor     r9, r9                    ; counter
    
    .add_loop:
        add     rcx, [rdx]
        add     rdx, 4                    ; move pointer
        add     r9, 4                     ; increment counter
        cmp     r8, r9
        jne     .add_loop

        mov     [total], rcx
        mov     rsi, total
        call    print

        mov     rsi, newline
        call    print

    .exit:
        mov       rax, 60                 ; system call for exit
        xor       rdi, rdi                ; exit code 0
        syscall                           ; invoke operating system to exit

    ; Print contents of byte at rsi
    print:
        mov       rax, 1                  ; system call for write
        mov       rdi, 1                  ; file handle 1 is stdout
        mov       rdx, 1                  ; number of bytes
        syscall
        ret

    section .data
        ;Let's do the simple example of "+1, -2, +3, +1"
        numbers:    dd 1, -2, 3, 1
        length:     equ $-numbers
        newline:    db 10
    
    section .bss
        total resb 1