	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
main:
	push %ebp
	movl %esp, %ebp
	subl $8, %esp
	push $0
	push $0
	push $100
	addl $4, %esp
	imull %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE0
	push $11
	push $1
	push $4
	addl $4, %esp
	imull %esp, 4(%esp)
	addl $4, %esp
	addl %esp, 4(%esp)
	pop -4(%ebp)
	jmp .END0
.ELSE0:
	push $12
	push $2
	addl $4, %esp
	addl %esp, 4(%esp)
	pop -4(%ebp)
.END0:
	push $.s0
	push $.s1
	call strcat
	push $.s1
	push $.s3
	call strcat
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .END1
	push $.s4
	push $.s5
	call strcat
	pop -4(%ebp)
.END1:
	push -4(%ebp)
	pop -4(%ebp)
.LOOP0:
	push $0
	push $1
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .BODY0
	jmp .LOOPEND0
.BODY0:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	pop -4(%ebp)
	push -4(%ebp)
	push $.s6
	call strcat
	pop -4(%ebp)
	jmp .LOOP0
.LOOPEND0:
	push -4(%ebp)
	movl %ebp, %esp
	pop %ebp
	ret
.section		.rodata
	.s0	.string "a"
	.s1	.string "aa"
	.s2	.string "aa"
	.s3	.string 'a'
	.s4	.string "abc"
	.s5	.string "def"
	.s6	.string '1'
	