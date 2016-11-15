	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
fact:
	push %ebp
	movl %esp, %ebp
	subl $-4, %esp
	push 4(%ebp)
	push $1
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .END0
	push $1
	movl %ebp, %esp
	pop %ebp
	ret
.END0:
	push 4(%ebp)
	push 4(%ebp)
	push $1
	addl $4, %esp
	subl %esp, 4(%esp)
	call fact
	addl $4, %esp
	imull %esp, 4(%esp)
	movl %ebp, %esp
	pop %ebp
	ret
main:
	push %ebp
	movl %esp, %ebp
	subl $0, %esp
	push $10
	call fact
	call printd
	push $0
	movl %ebp, %esp
	pop %ebp
	ret