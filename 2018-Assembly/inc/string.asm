; Include file containing helper functions
; By Craig Brennan 2022

%ifndef STRING_ASM
    %define STRING_ASM

    ; Print contents of bytes from [rsi]
    ; Note: The string length is fixed
    print:
        mov     rax, 1            ; system call for write
        mov     rdi, 1            ; file handle 1 is stdout
        mov     rdx, 3            ; number of bytes
        syscall
        ret

    ; Integer to string: Convert int64 at rsi to string
    ; and save in result_str - currently signed only
    ; Note the string length is fixed at 3 digits
    int_to_string:
        mov     rbx, 2            ; 2 means 10^2 divisor or 0 - 999 range
        mov     r10, result_str   ; pointer to string
    .loop:
        mov     r11, rbx          ; loop limit to r11
        mov     r9, r11           ; divisor exponent to r9
        call    pow10             ; get the divisor
        mov     rcx, rax          ; divisor to rcx
        mov     rdx, 0            ; reset rdx (high reg)
        mov     rax, rsi          ; load low reg
        div     rcx               ; rax: quotient, rdx: remainder
        add     rax, 30h          ; convert to ascii char
        mov     [r10], rax        ; store in string
        mov     rsi, rdx          ; remainder becomes new number
        inc     r10               ; increment string pointer
        test    r11, r11          ; test r11 and set zf accordingly
        jz      .done
        dec     r11               ; decrement loop counter
        dec     rbx               ; decrement divisor
        jmp     .loop
    .done:
        mov     [r10], byte 0     ; null terminate string
        ret

    ; Take int64 in r9 and return 10^r9 in rax
    ; Fixme - return 0 on overflow
    pow10:
        mov     r8, 10
        mov     rax, 1
    .multiply_loop:
        cmp     r9, 0
        jz      .done
        mul     r8                ; rax = rax * r8
        dec     r9
        jmp     .multiply_loop
    .done:
        ret

%endif