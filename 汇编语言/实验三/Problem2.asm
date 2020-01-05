assume cs:codesg
codesg segment
	mov ax, 0ffffH
	mov ds, ax

	mov ax, 2200H
	mov ss, ax

	mov sp, 0100H

	mov ax, ds:[0]
	add ax, ds:[2]
	mov bx, ds:[4]
	add bx, ds:[6]

	push ax
	push bx
	pop ax
	pop bx

	push ds:[4]
	push ds:[6]
codesg ends
end