assume cs:codesg
data segment
	db '1975','1976','1977','1978','1979','1980','1981','1982','1983'
	db '1984','1985','1986','1987','1988','1989','1990','1991','1992'
	db '1993','1994','1995'

	dd 16,22,382,1356,2390,8000,16000,24486,50065,97479,140417,197514
	dd 345980,590827,803530,1183000,1843000,2759000,3753000,4649000,5973000

	dw 3,7,9,13,28,38,130,220,476,778,1001,1442,2258,2793,4037,5635,8226
	dw 11542,14430,15257,17800
data ends

table segment
	db 21 dup ('year summ ne ?? ')
table ends

codesg segment  
	start:
		mov ax,data
		mov ds,ax
		mov ax,table
		mov es,ax

		mov bx,0	;年份、收入的偏移
		mov si,0	;雇员数、人均收入的偏移
		mov di,0	;1年的偏移
		mov cx,21

		s:
			;存入年份
			mov ax,ds:[bx]
			mov es:[di],ax
			mov ax,ds:[bx+2]
			mov es:[di+2],ax
			;存入收入
			mov ax,ds:[bx + 84]
			mov es:[di + 5],ax
			mov ax,ds:[bx + 86]
			mov es:[di + 7],ax
			;存入雇员数
			mov ax,ds:[si + 168]	
			mov es:[di + 10],ax
			;存入年均收入
			mov dx,es:[di + 7]
			mov ax,es:[di + 5]
			div word ptr es:[di + 10]
			mov es:[di + 13],ax
			;循环条件
			add bx,4
			add si,2
			add di,16
		loop s

		mov ax,4c00H
		int 21H
	codesg ends
end start