assume cs:codesg
data segment
	dw 1, 2, 3, 4, 5, 6, 7, 8, 9
	dw 9, 8, 7, 6, 5, 4, 3, 2, 1
data ends

result segment
	dd 0, 0, 0, 0, 0, 0, 0, 0, 0
result ends

codesg segment
	start:
		mov ax, data
		mov ds, ax			;将a,b矩阵移入ds
		mov ax, result
		mov es, ax
		call matrix_mul

		mov ax, 4c00h
		int 21h

	matrix_mul:
		mov bx, 0				;bx = i
		mov cx, 3
		s1:
			push cx
			mov cx, 3
			mov di, 0			;di = j
		s2:
			push cx
			mov cx, 3
			mov si, 0			;si = k
		s3:
			mov ax, 3
			mul bx
			mov bp, ax
			mov ax, ds:[bp + si]	;ax = a[i][k]
			push ax

			mov ax, 3
			mul si
			mov bp, ax
			pop ax
			mul word ptr ds:[bp + 18 + di]	;ax = a[i][k] * b[k][j]
			push ax

			mov ax, 3
			mul bx
			add ax, di
			mov bp, ax			;bp = 3 * i + j
			add bp, bp
			pop ax
			add es:[bp], ax
			add es:[bp + 2], dx

			add si, 2
			loop s3

			pop cx
			add di, 2
			loop s2

			pop cx
			add bx, 2
			loop s1
			ret
codesg ends

end strat