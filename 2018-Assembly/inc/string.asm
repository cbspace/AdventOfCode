; Include file containing helper functions
; By Craig Brennan 2022

%ifndef STRING_ASM
    %define STRING_ASM

    ; Print contents of bytes from [rsi]
    ; Number of bytes (str len) at [rsi-8]
    ; println adds newline character
    println:
        mov     rax, 1            ; system call for write
        mov     rdi, 1            ; file handle 1 is stdout
        mov     rdx, [rsi - 8]
        syscall
        mov     rax, 1            ; system call for write
        mov     rdx, 1            ; string length is 1
        mov     rsi, newline      ; newline character
        syscall
        ret

    print:
        mov     rax, 1            ; system call for write
        mov     rdi, 1            ; file handle 1 is stdout
        syscall
        ret

    ; Integer to string: Convert int64 at rsi to string
    ; and save in result_str - currently positive ints only
    int_to_string:
        mov     rbx, 19           ; 2 means 10^19 divisor or 0 - 9.99e19 range
        mov     rdi, 0            ; 0 means no digits reached yet
        mov     r10, result_str   ; pointer to string
    .loop:
        mov     r11, rbx          ; loop limit to r11
        mov     r9, r11           ; divisor exponent to r9
        call    pow10             ; get the divisor
        mov     rcx, rax          ; divisor to rcx
        mov     rdx, 0            ; reset rdx (high reg)
        mov     rax, rsi          ; load low reg
        div     rcx               ; rax: quotient, rdx: remainder
        add     rdi, rax          ; add quotient with leading zero flag
        jz      .skip_write       ; digit is leading zero so don't save it
        add     rax, 30h          ; convert to ascii char
        mov     [r10], rax        ; store in string
        inc     r10               ; increment string pointer
        mov     rdi, 1            ; set flag to 1 as no more leading zeros
    .skip_write:
        mov     rsi, rdx          ; remainder becomes new number
        test    r11, r11          ; test r11 and set zf accordingly
        jz      .done
        dec     r11               ; decrement loop counter
        dec     rbx               ; decrement divisor
        jmp     .loop
    .done:
        mov     rcx, r10          ; load pointer to end of string
        sub     rcx, result_str   ; calculate string length
        mov     [result_str_len], rcx   ; populate string length
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