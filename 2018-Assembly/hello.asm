section .data
    hello_str: db 'Hello World!', 10 
    hello_len: equ $-hello_str

section .text
    global _start

    _start:
        call print
        jmp end  
        
    print:
        mov eax, 4
        mov ebx, 1
        mov ecx, hello_str
        mov edx, hello_len
        int 80h
        ret

    end:
        mov eax,1
        mov ebx,0
        int 80h  