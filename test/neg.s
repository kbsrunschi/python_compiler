	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
main:
	push %ebp
	movl %esp, %ebp
	subl $8, %esp
	push $123
	pop -4(%ebp)
	push -4(%ebp)
	negl 4(%esp)
	call printd
	push $123
	negl 4(%esp)
	call printd
	push $123
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	negl 4(%esp)
	call printd
	push -4(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	negl 4(%esp)
	call printd
	push $0
	movl %ebp, %esp
	pop %ebp
	ret