    ; Include file containing helper functions
    ; By Craig Brennan 2022

    ; Print contents of byte at [rsi]
    ; Note: The string length is fixed
    print:
        mov       rax, 1                  ; system call for write
        mov       rdi, 1                  ; file handle 1 is stdout
        mov       rdx, 3                  ; number of bytes
        syscall
        ret

    ; Integer to ASCII: Convert int64 at RDI to ASCII
    ; and save in itoa_result_str - currently signed only
    ; Note the string length is fixed at 3 digits
    itoa:
        mov rbx, 2                        ; 2 means 10^2 divisor or 0 - 999 range
        mov r10, itoa_result_str          ; pointer to string
    .loop:
        mov r11, rbx                      ; loop limit to r11
        mov r9, r11                       ; divisor exponent to r9
        call pow10                        ; get the divisor
        mov rcx, rax                      ; divisor to rcx
        mov rdx, 0                        ; reset rdx (high reg)
        mov rax, rdi                      ; load low reg
        div rcx                           ; rax: quotient, rdx: remainder
        add rax, 30h                      ; convert to ascii char
        mov [r10], rax                    ; store in string
        mov rdi, rdx                      ; remainder becomes new number
        cmp r11, 0
        jz .done
        dec r11
        dec rbx
        inc r10                           ; increment string pointer
        jmp .loop
    .done:
        ret

    ; Take int64 in r9 and return 10^r9 in rax
    ; Fixme - return 0 on overflow
    pow10:
        mov r8, 10
        mov rax, 1
    .multiply_loop:
        cmp r9, 0
        jz .done
        mul r8                    ; rax = rax * r8
        dec r9
        jmp .multiply_loop
    .done:
        ret