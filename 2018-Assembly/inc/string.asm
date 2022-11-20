; Include file containing helper functions
; By Craig Brennan 2022

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