	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
main:
	push %ebp
	movl %esp, %ebp
	subl $8, %esp
	push $.s0
	pop -4(%ebp)
	push $.s1
	pop -4(%ebp)
	push $.s2
	pop 0(%ebp)
	push $.s0
	call printf
	push $.s0
	push $.s5
	call strcat
	call printf
	push -4(%ebp)
	push $.s5
	call strcat
	call printf
	push $.s0
	push -4(%ebp)
	call strcat
	call printf
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	call printf
	push -4(%ebp)
	push 0(%ebp)
	call strcat
	push -4(%ebp)
	call strcat
	call printf
	push -4(%ebp)
	push 0(%ebp)
	push -4(%ebp)
	call strcat
	call strcat
	call printf
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	call strcat
	call printf
	push -4(%ebp)
	push 0(%ebp)
	call strcat
	push -4(%ebp)
	call strcat
	call printf
	push $0
	movl %ebp, %esp
	pop %ebp
	ret
.section		.rodata
	.s0	.string "hello"
	.s1	.string " world\n"
	.s2	.string "bye"
	.s3	.string "hello"
	.s4	.string "hello"
	.s5	.string "world\n"
	.s6	.string "world\n"
	.s7	.string "hello"
	