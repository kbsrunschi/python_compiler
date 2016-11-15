	.section    __TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.globl  _main
	.align  4, 0x90
main:
	push %ebp
	movl %esp, %ebp
	subl $12, %esp
	push $450
	pop -4(%ebp)
	push $123
	negl 4(%esp)
	pop -8(%ebp)
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE0
	push -4(%ebp)
	call printd
	jmp .END0
.ELSE0:
	push -8(%ebp)
	call printd
.END0:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE1
	push -4(%ebp)
	call printd
	jmp .END1
.ELSE1:
	push -8(%ebp)
	call printd
.END1:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE2
	push -4(%ebp)
	call printd
	jmp .END2
.ELSE2:
	push -8(%ebp)
	call printd
.END2:
	push $45
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE3
	push -4(%ebp)
	call printd
	jmp .END3
.ELSE3:
	push -8(%ebp)
	call printd
.END3:
	push $45
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE4
	push -4(%ebp)
	call printd
	jmp .END4
.ELSE4:
	push -8(%ebp)
	call printd
.END4:
	push $45
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE5
	push -4(%ebp)
	call printd
	jmp .END5
.ELSE5:
	push -8(%ebp)
	call printd
.END5:
	push -4(%ebp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE6
	push -4(%ebp)
	call printd
	jmp .END6
.ELSE6:
	push -8(%ebp)
	call printd
.END6:
	push -4(%ebp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE7
	push -4(%ebp)
	call printd
	jmp .END7
.ELSE7:
	push -8(%ebp)
	call printd
.END7:
	push -4(%ebp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jge .ELSE8
	push -4(%ebp)
	call printd
	jmp .END8
.ELSE8:
	push -8(%ebp)
	call printd
.END8:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE9
	push -4(%ebp)
	call printd
	jmp .END9
.ELSE9:
	push -8(%ebp)
	call printd
.END9:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE10
	push -4(%ebp)
	call printd
	jmp .END10
.ELSE10:
	push -8(%ebp)
	call printd
.END10:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE11
	push -4(%ebp)
	call printd
	jmp .END11
.ELSE11:
	push -8(%ebp)
	call printd
.END11:
	push $45
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE12
	push -4(%ebp)
	call printd
	jmp .END12
.ELSE12:
	push -8(%ebp)
	call printd
.END12:
	push $45
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE13
	push -4(%ebp)
	call printd
	jmp .END13
.ELSE13:
	push -8(%ebp)
	call printd
.END13:
	push $45
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE14
	push -4(%ebp)
	call printd
	jmp .END14
.ELSE14:
	push -8(%ebp)
	call printd
.END14:
	push -4(%ebp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE15
	push -4(%ebp)
	call printd
	jmp .END15
.ELSE15:
	push -8(%ebp)
	call printd
.END15:
	push -4(%ebp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE16
	push -4(%ebp)
	call printd
	jmp .END16
.ELSE16:
	push -8(%ebp)
	call printd
.END16:
	push -4(%ebp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jle .ELSE17
	push -4(%ebp)
	call printd
	jmp .END17
.ELSE17:
	push -8(%ebp)
	call printd
.END17:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE18
	push -4(%ebp)
	call printd
	jmp .END18
.ELSE18:
	push -8(%ebp)
	call printd
.END18:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE19
	push -4(%ebp)
	call printd
	jmp .END19
.ELSE19:
	push -8(%ebp)
	call printd
.END19:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE20
	push -4(%ebp)
	call printd
	jmp .END20
.ELSE20:
	push -8(%ebp)
	call printd
.END20:
	push $45
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE21
	push -4(%ebp)
	call printd
	jmp .END21
.ELSE21:
	push -8(%ebp)
	call printd
.END21:
	push $45
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE22
	push -4(%ebp)
	call printd
	jmp .END22
.ELSE22:
	push -8(%ebp)
	call printd
.END22:
	push $45
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE23
	push -4(%ebp)
	call printd
	jmp .END23
.ELSE23:
	push -8(%ebp)
	call printd
.END23:
	push -4(%ebp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE24
	push -4(%ebp)
	call printd
	jmp .END24
.ELSE24:
	push -8(%ebp)
	call printd
.END24:
	push -4(%ebp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE25
	push -4(%ebp)
	call printd
	jmp .END25
.ELSE25:
	push -8(%ebp)
	call printd
.END25:
	push -4(%ebp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jl .ELSE26
	push -4(%ebp)
	call printd
	jmp .END26
.ELSE26:
	push -8(%ebp)
	call printd
.END26:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE27
	push -4(%ebp)
	call printd
	jmp .END27
.ELSE27:
	push -8(%ebp)
	call printd
.END27:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE28
	push -4(%ebp)
	call printd
	jmp .END28
.ELSE28:
	push -8(%ebp)
	call printd
.END28:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE29
	push -4(%ebp)
	call printd
	jmp .END29
.ELSE29:
	push -8(%ebp)
	call printd
.END29:
	push $45
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE30
	push -4(%ebp)
	call printd
	jmp .END30
.ELSE30:
	push -8(%ebp)
	call printd
.END30:
	push $45
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE31
	push -4(%ebp)
	call printd
	jmp .END31
.ELSE31:
	push -8(%ebp)
	call printd
.END31:
	push $45
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE32
	push -4(%ebp)
	call printd
	jmp .END32
.ELSE32:
	push -8(%ebp)
	call printd
.END32:
	push -4(%ebp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE33
	push -4(%ebp)
	call printd
	jmp .END33
.ELSE33:
	push -8(%ebp)
	call printd
.END33:
	push -4(%ebp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE34
	push -4(%ebp)
	call printd
	jmp .END34
.ELSE34:
	push -8(%ebp)
	call printd
.END34:
	push -4(%ebp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jg .ELSE35
	push -4(%ebp)
	call printd
	jmp .END35
.ELSE35:
	push -8(%ebp)
	call printd
.END35:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE36
	push -4(%ebp)
	call printd
	jmp .END36
.ELSE36:
	push -8(%ebp)
	call printd
.END36:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE37
	push -4(%ebp)
	call printd
	jmp .END37
.ELSE37:
	push -8(%ebp)
	call printd
.END37:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE38
	push -4(%ebp)
	call printd
	jmp .END38
.ELSE38:
	push -8(%ebp)
	call printd
.END38:
	push $45
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE39
	push -4(%ebp)
	call printd
	jmp .END39
.ELSE39:
	push -8(%ebp)
	call printd
.END39:
	push $45
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE40
	push -4(%ebp)
	call printd
	jmp .END40
.ELSE40:
	push -8(%ebp)
	call printd
.END40:
	push $45
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE41
	push -4(%ebp)
	call printd
	jmp .END41
.ELSE41:
	push -8(%ebp)
	call printd
.END41:
	push -4(%ebp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE42
	push -4(%ebp)
	call printd
	jmp .END42
.ELSE42:
	push -8(%ebp)
	call printd
.END42:
	push -4(%ebp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE43
	push -4(%ebp)
	call printd
	jmp .END43
.ELSE43:
	push -8(%ebp)
	call printd
.END43:
	push -4(%ebp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	jne .ELSE44
	push -4(%ebp)
	call printd
	jmp .END44
.ELSE44:
	push -8(%ebp)
	call printd
.END44:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE45
	push -4(%ebp)
	call printd
	jmp .END45
.ELSE45:
	push -8(%ebp)
	call printd
.END45:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE46
	push -4(%ebp)
	call printd
	jmp .END46
.ELSE46:
	push -8(%ebp)
	call printd
.END46:
	push -4(%ebp)
	push $1
	addl $4, %esp
	addl %esp, 4(%esp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE47
	push -4(%ebp)
	call printd
	jmp .END47
.ELSE47:
	push -8(%ebp)
	call printd
.END47:
	push $45
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE48
	push -4(%ebp)
	call printd
	jmp .END48
.ELSE48:
	push -8(%ebp)
	call printd
.END48:
	push $45
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE49
	push -4(%ebp)
	call printd
	jmp .END49
.ELSE49:
	push -8(%ebp)
	call printd
.END49:
	push $45
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE50
	push -4(%ebp)
	call printd
	jmp .END50
.ELSE50:
	push -8(%ebp)
	call printd
.END50:
	push -4(%ebp)
	push -8(%ebp)
	push $0
	addl $4, %esp
	addl %esp, 4(%esp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE51
	push -4(%ebp)
	call printd
	jmp .END51
.ELSE51:
	push -8(%ebp)
	call printd
.END51:
	push -4(%ebp)
	push $123
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE52
	push -4(%ebp)
	call printd
	jmp .END52
.ELSE52:
	push -8(%ebp)
	call printd
.END52:
	push -4(%ebp)
	push -8(%ebp)
	addl $4, %esp
	cmpl %esp, 4(%esp)
	addl $4, %esp
	je .ELSE53
	push -4(%ebp)
	call printd
	jmp .END53
.ELSE53:
	push -8(%ebp)
	call printd
.END53:
	push $0
	movl %ebp, %esp
	pop %ebp
	ret