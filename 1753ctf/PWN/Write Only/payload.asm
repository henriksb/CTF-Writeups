; Move the flag address from RAX to RSI (since RAX will be overwritten for syscall number)
mov rsi, rax

; Write syscall number (1) to RAX
mov rax, 1

; Set file descriptor to stdout (1) in RDI
mov rdi, 1

; Set number of bytes to write in RDX
mov rdx, 0x40

; Invoke the syscall
syscall

; Exit syscall
mov rax, 60  ; syscall number for exit
xor rdi, rdi ; status code 0
syscall
