; Include file for file operations
; By Craig Brennan 2022

%ifndef FILE_ASM
    %define FILE_ASM

    %define SYS_READ     0
    %define SYS_WRITE    1
    %define SYS_OPEN     2
    %define SYS_CLOSE    3

    %define O_RDONLY     0
    %define MODE_T       0444o

    ; int open(const char *pathname, int flags, mode_t mode)
    ; https://man7.org/linux/man-pages/man2/open.2.html
    file_open:
        mov     rdi, file_path          ; the file path
        mov     rsi, O_RDONLY           ; flags - O_RDONLY
        mov     rdx, MODE_T             ; user/group/others have read permission
        mov     rax, SYS_OPEN           ; syscall for open
        syscall
        mov     [file_descriptor], rax  ; store file descriptor
        ret

    ; read( <file descriptor>, <buffer>, <buffer length> )
    ; rdi - file descriptor
    ; rsi - buffer
    ; rdx - buffer length
    ; FIXME: Currently we just read 1024 bytes without checking
    ; if there are any more bytes or checking for errors.
    file_read_line:
        mov     rdi, [file_descriptor]  ; the file name
        mov     rsi, read_buffer        ; buffer for read
        mov     rdx, 1024               ; length to read
        mov     rax, 0                  ; syscall for read
        syscall
        mov     [read_buffer_len], rax  ; store the buffer length
        ret

    ; close( <file descriptor> )
    file_close:
        mov     rdi, [file_descriptor]  ; load file descriptor
        mov     rax, 3                  ; close
        syscall
        ret

%endif