	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
main:
	push %ebp
	movl %esp, %ebp
	subl $12, %esp
	push $45000
	pop -4(%ebp)
	push $3
	pop -8(%ebp)
	push -4(%ebp)
	push -8(%ebp)
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push $45000
	push -8(%ebp)
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push -4(%ebp)
	push $3
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push $45000
	push $3
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push -4(%ebp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push -4(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push -4(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push -4(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	push $3
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push $45000
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	shl %esp, $4(%esp)
	call printd
	push $0
	movl %ebp, %esp
	pop %ebp
	ret