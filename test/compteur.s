	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
main:
	push %ebp
	movl %esp, %ebp
	subl $8, %esp
	push $0
	pop -4(%ebp)
.LOOP0:
	push -4(%ebp)
	push $1000
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .BODY0
	jmp .LOOPEND0
.BODY0:
	push -4(%ebp)
	call printd
	push $.s0
	call printf
	push $1
	call sleep
	push $27
	push $.s1
	call strcat
	call printf
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	pop -4(%ebp)
	jmp .LOOP0
.LOOPEND0:
	push $0
	movl %ebp, %esp
	pop %ebp
	ret
.section		.rodata
	.s0	.string "\n"
	.s1	.string "M"
	