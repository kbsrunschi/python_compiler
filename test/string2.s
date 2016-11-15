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
	push -4(%ebp)
	push -4(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE0
	push $1
	call printd
	jmp .END0
.ELSE0:
	push $0
	call printd
.END0:
	push $.s3
	push $.s3
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE1
	push $1
	call printd
	jmp .END1
.ELSE1:
	push $0
	call printd
.END1:
	push -4(%ebp)
	push -4(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE2
	push $1
	call printd
	jmp .END2
.ELSE2:
	push $0
	call printd
.END2:
	push -4(%ebp)
	push $.s3
	call strcat
	push 0(%ebp)
	push $.s6
	call strcat
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE3
	push $1
	call printd
	jmp .END3
.ELSE3:
	push $0
	call printd
.END3:
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	push 0(%ebp)
	call strcat
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	push 0(%ebp)
	call strcat
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE4
	push $1
	call printd
	jmp .END4
.ELSE4:
	push $0
	call printd
.END4:
	push -4(%ebp)
	push -4(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE5
	push $1
	call printd
	jmp .END5
.ELSE5:
	push $0
	call printd
.END5:
	push $.s3
	push $.s3
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE6
	push $1
	call printd
	jmp .END6
.ELSE6:
	push $0
	call printd
.END6:
	push -4(%ebp)
	push -4(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE7
	push $1
	call printd
	jmp .END7
.ELSE7:
	push $0
	call printd
.END7:
	push -4(%ebp)
	push $.s3
	call strcat
	push 0(%ebp)
	push $.s6
	call strcat
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE8
	push $1
	call printd
	jmp .END8
.ELSE8:
	push $0
	call printd
.END8:
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	push 0(%ebp)
	call strcat
	push -4(%ebp)
	push -4(%ebp)
	call strcat
	push 0(%ebp)
	call strcat
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE9
	push $1
	call printd
	jmp .END9
.ELSE9:
	push $0
	call printd
.END9:
	push $0
	movl %ebp, %esp
	pop %ebp
	ret
.section		.rodata
	.s0	.string "hello"
	.s1	.string "helll"
	.s2	.string "hellp"
	.s3	.string "abc"
	.s4	.string "abc"
	.s5	.string "abc"
	.s6	.string "ab"
	.s7	.string "abc"
	.s8	.string "abc"
	.s9	.string "abc"
	.s10	.string "ab"
	