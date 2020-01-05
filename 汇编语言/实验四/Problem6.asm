assume cs:codesg
codesg segment
	mov ax, 0
	mov bx, 1
	mov dx, 1

	mov cx, 20

  s:mov ax, dx
  	add dx, ax
  	mov bx, dx
  	loop s

codesg ends
end