assume cs:codesg
codesg segment
	mov ax, 1000H
	mov bh, 0
	div bh
codesg ends
end