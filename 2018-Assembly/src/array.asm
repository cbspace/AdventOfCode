; Include file for array functions
; By Craig Brennan 2022
; Functions for 8 bit and 64 bit arrays (ASCII string and int64)
; In the future can be reduced by using macros to combine 8 and 64 bit

%ifndef ARRAY_ASM
    %define ARRAY_ASM

    ; search array for value and return offset of first occurance in rax
    ; input array is pointed to by rdi with length in [rdi - 8]
    ; value to compare stored in rbx
    ; return -1 when not found
    array_index_64:
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
    array_count_8:
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

    ; search array and create array of unique bytes
    ; input array is pointed to by rdi with length in [rdi - 8]
    ; store the unique array and length in result_str and result_str_len
    array_get_unique_8:
        xor       r11, r11               ; result length
        mov       r12, rdi               ; pointer to input array
        xor       r9, r9                 ; loop counter
        mov       rsi, result_str        ; point to result str
        mov       r8, [rdi - 8]          ; array length
        test      r8, r8                 ; test if empty
        jnz        .loop                 ; if empty end
        mov       [result_str_len], r11  ; store result length of 0
        ret                              ; empty string so end
    .loop:
        mov       rbx, [r12]             ; get character
        and       rbx, 000000ffh         ; mask high bytes
        mov       rdi, result_str        ; load the result array
        push      r8                     ; save registers
        push      r9
        push      r10
        call      array_count_8          ; check if char already in array
        pop       r10                    ; restore registers
        pop       r9
        pop       r8
        test      rax, rax               ; check result value
        jnz       .not_unique            ; character already exists
        mov       [rsi], rbx             ; save character in array
        inc       rsi                    ; increment pointer to result
        inc       r11                    ; increment result array length
        mov       [result_str_len], r11  ; store result length
    .not_unique:
        inc       r9                     ; increment counter
        inc       r12                    ; increment pointer to input array
        cmp       r9, r8                 ; see if we are at the end of input
        jne       .loop                  ; not at the end so keep looping
        ret
    

    ; search array for byte and remove all instances of the byte
    ; input array is pointed to by rdi with length in [rdi - 8]
    ; byte to remove stored in rbx
    ; return value is number of bytes removed
    array_remove_all_of_8:
        
        ret

%endif