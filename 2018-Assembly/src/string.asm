; Include file containing helper functions
; By Craig Brennan 2022

%ifndef STRING_ASM
    %define STRING_ASM

    ; Print contents of bytes from pointer in rsi
    ; Number of bytes (str len) at rsi-8
    ; with newline character
    println:
        mov     rax, 1                  ; system call for write
        mov     rdi, 1                  ; file handle 1 is stdout
        mov     rdx, [rsi - 8]
        syscall
        mov     rax, 1                  ; system call for write
        mov     rdx, 1                  ; string length is 1
        mov     rsi, newline            ; newline character
        syscall
        ret

    ; printcr - newline character
    ; print   - print number of bytes specified in rdx from address in rsi
    printcr:
        mov     rdx, 1                  ; string length is 1
        mov     rsi, newline            ; newline character
    print:
        mov     rax, 1                  ; system call for write
        mov     rdi, 1                  ; file handle 1 is stdout
        syscall
        ret

    ; Integer to string: Convert int64 in rsi to string and save in result_str
    int_to_string:
        mov     r8, 19                  ; 19 means 10^19 divisor or 0 - 9.99e19 range
        mov     rdi, 0                  ; 0 means no digits reached yet
        mov     r10, result_str         ; pointer to string
        test    rsi, rsi                ; test the number
        jz      .number_is_zero         ; if number is zero jump to label
        cmp     rsi, -1                 ; compare number to -1
        jg      .loop                   ; if number is positive go to loop
        neg     rsi                     ; make number positive
        mov     rax, '-'                ; load minus character
        mov     [r10], rax              ; store in string
        inc     r10                     ; increment string pointer
    .loop:
        mov     r11, r8                 ; loop limit to r11
        mov     r9, r11                 ; divisor exponent to r9
        call    pow10                   ; get the divisor
        mov     rcx, rax                ; divisor to rcx
        mov     rdx, 0                  ; reset rdx (high reg)
        mov     rax, rsi                ; load low reg
        div     rcx                     ; rax: quotient, rdx: remainder
        add     rdi, rax                ; add quotient with leading zero flag
        jz      .skip_write             ; digit is leading zero so don't save it
        add     rax, 30h                ; convert to ascii char
        mov     [r10], rax              ; store in string
        inc     r10                     ; increment string pointer
        mov     rdi, 1                  ; set flag to 1 as no more leading zeros
    .skip_write:
        mov     rsi, rdx                ; remainder becomes new number
        test    r11, r11                ; test r11 and set zf accordingly
        jz      .done
        dec     r11                     ; decrement loop counter
        dec     r8                      ; decrement divisor
        jmp     .loop
    .number_is_zero:
        mov     rax, '0'                ; load 0 character
        mov     [r10], rax              ; store in string
        inc     r10                     ; increment string pointer
    .done:
        mov     rcx, r10                ; load pointer to end of string
        sub     rcx, result_str         ; calculate string length
        mov     [result_str_len], rcx   ; populate string length
        ret

    ; Convert string pointed to by rsi to int64 stored in rax
    ; string length stored in [rsi - 8]
    ; input string is integer with optional leading '-'
    string_to_int:
        mov     r11, 0                  ; the total value
        mov     r8, [rsi - 8]           ; get string length / counter
        mov     rax, r8                 ; store length in rax
        dec     rax                     ; calculate offset
        add     rsi, rax                ; move to end of string
        mov     rdi, 0                  ; int power of 10
        cmp     r8, 0                   ; is string empty?
        jnz     .add_loop               ; nope so keep going
        mov     rax, 0                  ; return 0 on empty string
        ret                             ; string is empty so get outta here
    .add_loop:
        mov     r10, [rsi]              ; get character
        and     r10, 000000ffh          ; mask high bytes
        dec     rsi                     ; move pointer
        sub     r10, 30h                ; minus ASCII '0' value
        js      .leading_char           ; negative value
        cmp     r10, 9                  ; compare value to '9'
        jg      .leading_char           ; non integer value
        mov     r9, rdi                 ; load the power of 10 to r9
        call    pow10                   ; multiply by 10^n
        mul     r10                     ; rdx:rax = rax * r10
        add     r11, rax                ; add to total
        inc     rdi                     ; increase power of 10
        dec     r8                      ; decrement length counter
        jz      .done                   ; end of the string
        jmp     .add_loop               ; go to next character
    .leading_char:
        cmp     r10, -3                 ; do we have '-' character?
        jne     .done                   ; no we don't
        neg     r11                     ; we have '-' so negate value
    .done:
        mov     rax, r11                ; return the number in rax
        ret

    ; Take int64 in r9 and return 10^r9 in rax
    ; Fixme - return 0 on overflow
    pow10:
        mov     rcx, 10
        mov     rax, 1
    .multiply_loop:
        cmp     r9, 0
        jz      .done
        mul     rcx                      ; rdx:rax = rax * rcx
        dec     r9
        jmp     .multiply_loop
    .done:
        ret

%endif