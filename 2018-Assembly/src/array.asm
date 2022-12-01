; Include file for array functions
; By Craig Brennan 2022

%ifndef ARRAY_ASM
    %define ARRAY_ASM

    ; search array for value and return offset of first occurance in rax
    ; input array is pointed to by rdi with length in [rdi - 8]
    ; value to compare stored in rbx
    ; return -1 when not found
    array_index:
        mov       r9, [rdi - 8]         ; array length
        test      r9, r9                ; is the array empty?
        jz        .not_found            ; yes so leave
        xor       r10, r10              ; counter = 0
    .loop:
        mov       r8, [rdi]             ; load array value
        cmp       r8, rbx               ; compare to input value
        je        .found
        add       r10, 8                ; increase counter
        add       rdi, 8                ; increase pointer
        cmp       r10, r9               ; are we at the end of array?
        jne       .loop                 ; no, keep going
    .not_found:
        mov       rax, -1               ; not found, return -1
        ret
    .found:
        mov       rax, r10
        ret

    ; search array for byte and return number of occurances in rax
    ; input array is pointed to by rdi with length in [rdi - 8]
    ; byte to compare stored in rbx
    array_count:
        mov       r9, [rdi - 8]         ; array length
        xor       rax, rax              ; number of occurances
        test      r9, r9                ; is the array empty?
        jz        .done                 ; yes so leave
        xor       r10, r10              ; counter = 0
    .loop:
        mov       r8, [rdi]             ; load array value
        and       r8, 000000ffh         ; mask high bytes
        cmp       r8, rbx               ; compare to input value
        jne       .not_match            ; value does not match
        inc       rax                   ; match, increase count
    .not_match:
        inc       r10                   ; increase counter
        add       rdi, 1                ; increase pointer
        cmp       r10, r9               ; are we at the end of array?
        jne       .loop                 ; no, keep going
    .done:
        ret

%endif