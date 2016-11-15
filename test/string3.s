	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
sub:
	push %ebp
	movl %esp, %ebp
	subl $8, %esp
	push $.s0
	pop -4(%ebp)
	push 4(%ebp)
	pop -4(%ebp)
.LOOP0:
	push -4(%ebp)
	push 4(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .BODY0
	jmp .LOOPEND0
.BODY0:
	push -4(%ebp)
	push 4(%ebp)
	call get_char_at
	call strcat
	pop -4(%ebp)
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	pop -4(%ebp)
	jmp .LOOP0
.LOOPEND0:
	push -4(%ebp)
	movl %ebp, %esp
	pop %ebp
	ret
invert:
	push %ebp
	movl %esp, %ebp
	subl $-4, %esp
	push 4(%ebp)
	push $.s0
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .END0
	push $.s0
	movl %ebp, %esp
	pop %ebp
	ret
.END0:
	push 4(%ebp)
	call sub
	call invert
	push 4(%ebp)
	call get_char_at
	call strcat
	movl %ebp, %esp
	pop %ebp
	ret
main:
	push %ebp
	movl %esp, %ebp
	subl $8, %esp
	push $.s3
	pop -4(%ebp)
	push $.s4
	pop -4(%ebp)
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	call invert
	call strcat
	call printf
	push -4(%ebp)
	call invert
	call invert
	call invert
	call invert
	call invert
	call invert
	call invert
	call invert
	call printf
	push $0
	movl %ebp, %esp
	pop %ebp
	ret
.section		.rodata
	.s0	.string ""
	.s1	.string ""
	.s2	.string ""
	.s3	.string "hello"
	.s4	.string "world"
	