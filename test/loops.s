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
	push $10
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .BODY0
	jmp .LOOPEND0
.BODY0:
	push -4(%ebp)
	call printd
	push -4(%ebp)
	push $2
	addl $4, %esp
	addl %esp, 4(%esp)
	pop -4(%ebp)
	jmp .LOOP0
.LOOPEND0:
	push $10
	negl 4(%esp)
	pop -4(%ebp)
.LOOP1:
	push -4(%ebp)
	push $10
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .BODY1
	jmp .LOOPEND1
.BODY1:
	push -4(%ebp)
	call printd
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	pop -4(%ebp)
	jmp .LOOP1
.LOOPEND1:
	push $0
	pop -4(%ebp)
.BODY2:
	push -4(%ebp)
	call printd
	push -4(%ebp)
	push $1
	addl $4, %esp
	subl %esp, 4(%esp)
	pop -4(%ebp)
.LOOP2:
	push -4(%ebp)
	push $20
	negl 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .BODY2
	push $0
	movl %ebp, %esp
	pop %ebp
	ret