	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
main:
	push %ebp
	movl %esp, %ebp
	subl $16, %esp
	push $45000
	pop -4(%ebp)
	push $123
	negl 4(%esp)
	pop -8(%ebp)
	push $43
	pop -12(%ebp)
	push -4(%ebp)
	push -8(%ebp)
	addl $4, %esp
	addl %esp, 4(%esp)
	push -12(%ebp)
	addl $4, %esp
	imull %esp, 4(%esp)
	push $100
	addl $4, %esp
	movl $0, %eax
	movl 4(%esp), %eax
	divl %esp
	movl %eax, 4(%esp)
	push -8(%ebp)
	push -12(%ebp)
	addl $4, %esp
	imull %esp, 4(%esp)
	push -4(%ebp)
	addl $4, %esp
	movl $0, %edx
	movl 4(%esp), %eax
	divl %esp
	movl %edx, 4(%esp)
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	addl $4, %esp
	subl %esp, 4(%esp)
	push -12(%ebp)
	addl $4, %esp
	shl %esp, $4(%esp)
	push -12(%ebp)
	push -8(%ebp)
	addl $4, %esp
	subl %esp, 4(%esp)
	push $2
	addl $4, %esp
	shr %esp, $4(%esp)
	addl $4, %esp
	movl $0, %eax
	movl 4(%esp), %eax
	divl %esp
	movl %eax, 4(%esp)
	call printd
	push $0
	movl %ebp, %esp
	pop %ebp
	ret