assume cs:code,ds:data

data segment
	db  'Beginners All-purpose Symbolic Instruction Code.', 0
data ends

code segment
start:
	mov ax, data
	mov ds, ax
	mov si, 0
	call letterc

	mov ax, 4c00h
	int 21h
;子程序letterc
letterc:
	push ax
	push cx
s:
	mov cl, ds:[si]
	mov ch, 0

	jcxz ok		;如果cx==0,则结束循环.判断是否为字符串末尾
	
	cmp cl, 61h
	jb check_out
	cmp cl,91h
	ja check_out

	mov al, cl
	and al, 11011111b
	mov cl, al
	mov ds:[si], cl

check_out:
	inc si
jmp short s

ok:
	pop cx
	pop ax
	ret
code ends
end start