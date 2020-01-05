;宏定义puts(str) 
PUTS MACRO STRING
	PUSH AX
	PUSH DX
	LEA DX, STRING
	MOV AH, 09h
	INT 21h
	POP DX
	POP AX
ENDM

_STACK SEGMENT
	DB  7FFEh DUP(0)
TOS DW 0
_STACK ENDS

_DATA SEGMENT
DIFFICULTY  DW  ?
POS_X DW 0A0h
POS_Y DW 0A0h
MISSILE    DW 512 DUP('$$')
MISSILESNUM DW 0
ENEMY      DW 512 DUP('$$')
ENEMYNUM   DW 0
PLANEMAP DW  1,1,3,3,3,3,3,3,7,14,16,14,6,2,2,6,6 
N1		 EQU  ($-PLANEMAP)/2	;我方飞机
MISSILEMAP DW 1,1,3,3,3
N2		 EQU  ($-MISSILEMAP)/2	;子弹
ENEMYMAP  DW 3,3,1,1
N3       EQU  ($-ENEMYMAP)/2	;敌机
TIMER    DW  0
MAX     DW 30
SCORE   DW 0
HIGHEST DW 0

MAINMENU DB  '-------------Welcome-------------',0Dh,0Ah
		 DB  'How to play',0Dh,0Ah
		 DB  'Move: left up right down',0Dh,0Ah
		 DB  'Shoot: space key',0Dh,0Ah
		 DB  'Score: Hit(+2), Escape(-5), Collide(Game over)',0Dh,0Ah
		 DB  'Now you can press Enter to start!',0Dh,0Ah
		 DB  'Or press ESC to quit(also in the game)',0Dh,0Ah
		 DB  '-----------Liang qilin-----------',0Dh,0Ah,'$'
		 
CHOOSEMENU	DB  '         1.Easy',0Dh,0Ah
		 	DB  '         2.Middle',0Dh,0Ah
		 	DB  '         3.Hard',0Dh,0Ah
		 	DB  '         4.Very hard',0Dh,0Ah
		 	DB  '         please choose:',0Dh,0Ah,'$'
		 
		 
GAMEOVER DB  'Your highest score:',0Dh,0Ah
		 DB  0Dh,0Ah
		 DB  '--------------GAME OVER---------------',0Dh,0Ah
		 DB  0Dh,0Ah
		 DB  '$'
_DATA ENDS

_TEXT SEGMENT 
ASSUME CS:_TEXT, DS:_DATA, SS:_STACK

Start:
		MOV AX, _DATA
		MOV DS, AX
		CLI						;禁止中断发生
		MOV AX, _STACK
		MOV SS, AX
		MOV SP, Offset TOS		;Sp指向栈顶
		STI						;允许中断发生
		
		CALL init				;初始化Menu
		
		MOV AH, 00h				;空格,不显示任何数据
		MOV AL, 04h				;320*200图形
		INT 10h					;调用显存
		MOV CX, N1				;存储飞机长度
		PUSH CX
		MOV SI, Offset PLANEMAP
		PUSH SI
		MOV CX, 0001h
		PUSH CX
		PUSH POS_Y
		PUSH POS_X
		CALL drawCraft
		ADD SP, 10				;堆栈使用完毕,“还”给系统
Again:
		MOV AH, 01h
		INT 16h					;键盘I/O中断调用,若有按键操作（即键盘缓冲区不空）,则ZF＝0
Next:  
		JZ  Process				;若键盘输入为空,则跳转Process
		MOV AH, 00h				;从键盘读入字符送AL寄存器
		INT 16h
		CMP AL, 27				;如果AL = 27则跳转结束,如果ESC则结束
		JZ EndMain
		CMP AL, ' '				;如果输入空格,则发出子弹
		JZ Shoot
		PUSH AX					;把键盘缓冲区的值,现在的坐标放入栈中
		PUSH POS_Y
		PUSH POS_X
		CALL movePlane			;调用移动飞机的函数
		ADD SP, 6
		JMP Again				;循环整个过程
Shoot: 
		PUSH POS_Y				;只存入现在的坐标
		PUSH POS_X
		CALL fireMissile
		ADD SP, 4
		JMP Again
Process:
		PUSH SCORE				;开始处理程序
		CALL showScoreByDemical	;显示分数
		ADD SP, 2
		CALL checkCollision
		INC TIMER
		MOV DX, DIFFICULTY		;分配难度
		CMP TIMER, DX			;如果TIMER >= DX则跳转
		JBE Loc1 
		CALL dropEnemy  
		MOV DX, MAX
		SUB DX, TIMER
		MOV TIMER, 0
		CMP ENEMYNUM, DX
		JA  Loc1
		CALL generateEnemy		;随机分配敌机
Loc1:
		CMP MISSILESNUM, 0		;如果没有子弹的时候跳转,继续读入键盘操作
		JZ Again
		CALL riseMissile		;当子弹上升时.继续读入键盘操作
		JMP Again

	   
EndMain:
		MOV AX, 4C00h
		INT 21h

;初始化游戏菜单
init	PROC NEAR				;子程序与主程序在一处
		MOV AX, 0003h			;80*25的文字
		INT 10h
		PUTS MAINMENU
Redo2:		
		MOV AH,01h				;键盘输入并回显,AL = 输入字符
		INT 21h
		CMP AL, 27
		JZ  ESCT				;如果AL = 27则跳转结束,如果ESC则结束
		CMP AL, 0Dh	
		JNZ Redo2				;如果AL != 0Dh则回显
		
		MOV AX, 0003h
		INT 10h
		PUTS CHOOSEMENU
Redo:		
		MOV AH,01h
		INT 21h
		SUB AL, '0'
		CMP AL, 1
		JZ IF_1
		CMP AL, 2
		JZ IF_2
		CMP AL, 3
		JZ IF_3
		CMP AL, 4
		JZ IF_4
		JMP Redo				;如果都不是则回显
IF_1:	MOV DIFFICULTY, 5
		JMP IFEND
IF_2:	MOV DIFFICULTY, 3
		JMP IFEND
IF_3:	MOV DIFFICULTY, 1
		JMP IFEND
IF_4:	MOV DIFFICULTY, 0
		JMP IFEND
ESCT:	MOV AX, 4C00h
		INT 21h
IFEND:  
		RET
init	ENDP

;画一条直线
drawALine	PROC NEAR
			PUSH BP
			MOV BP, SP			;BP = SP
			PUSH AX
			PUSH CX
			PUSH DX
			PUSH SI

			MOV AH, 0Ch			;写入点像，要写入位置 X 座标存于 CX 寄存器，Y 座标存于 DX 寄存器，颜色存于 AL 寄存器。
			MOV CX, [BP+4]
			MOV DX, [BP+6]
			MOV SI, [BP+8]
			MOV AL, Byte Ptr [BP+10]
drawALineLoop:
			INT 10h
			INC CX
			DEC SI				;SI != 0则跳转
			JNZ drawALineLoop
			;数据保护
			POP SI
			POP DX
			POP CX
			POP AX
			MOV SP, BP
			POP BP
			RET
drawALine	ENDP

;绘制飞机或敌机或子弹
drawCraft	PROC NEAR
			PUSH BP
			MOV BP, SP
			SUB SP, 8				;开辟一个栈空间

			PUSH AX
			PUSH DX
			PUSH SI
			PUSH DI
			MOV DI, 0

			MOV AX, [BP+12]			;[BP-8] = [BP+12]
			MOV [BP-8],AX
			MOV SI, [BP+10]			;设定SI为偏移始址
			MOV AX, [BP+8]			;[BP-6] = 0001h
			MOV [BP-6], AX
			MOV AX, [BP+6]			;[BP-4] = POS_Y
			MOV [BP-4], AX
			MOV AX, [BP+4]			;[BP-2] = POS_X
			MOV [BP-2], AX
drawCraftLoop:
			PUSH Word Ptr [BP-6]	;传入颜色
			MOV DX, Word Ptr [SI]
			PUSH DX	    			;传入这条线的长度
			PUSH Word Ptr [BP-4]	;传入POS_Y
			MOV AX, [BP-2]
			SHR DX, 1
			SUB AX, DX
			PUSH AX					;传入POS_X = POS_X - [SI] / 2
			CALL drawALine
			ADD SP, 8				;还原分配空间
			ADD Word Ptr [BP-4], 1	;每循环一次POS_Y++
			ADD SI, 2				;走向下一位偏移地址
			INC DI
			CMP DI, [BP-8]			;如果循环结束,结束整个流程
			JB  drawCraftLoop
			
			POP DI
			POP SI
			POP DX
			POP AX    
			MOV SP, BP
			POP BP
			RET
drawCraft ENDP

;移动飞机
movePlane	PROC NEAR
			PUSH BP
			MOV BP, SP
		 
			PUSH AX
			PUSH BX
			PUSH CX
			
			MOV AX,N1
			PUSH AX
			MOV AX, Offset PLANEMAP
			PUSH AX
			MOV AX, 0000h
			PUSH AX					;颜色换为黑色,即擦除
			MOV AX, [BP+6]
			PUSH AX
			MOV AX, [BP+4]
			PUSH AX
			CALL drawCraft			;将原有的飞机擦除
			ADD SP, 10
			
			MOV CX, CS:MoveItems
			MOV AH, Byte Ptr [BP+9]
			MOV BX, Offset MoveCase
movePlaneLoop1:		 
			CMP AH, Byte Ptr CS:[BX]
			JE  ToCase				;如果AH = CS:[BX]则跳转
			ADD BX, 4				;一直做判断,判断键盘读入方向
			LOOP movePlaneLoop1
		 
ToCase:	 JMP Word Ptr CS: [BX+2]
MoveItems DW 4
MoveCase DW 75, Case1, 72, Case2,77, Case3, 80, Case4, 0, Default
Default: 	JMP EndSwitch			;如果没有移动,就在原处建立一个新飞机
Case1:  	SUB POS_X, 5			;向左
			JMP EndSwitch
Case2:		SUB POS_Y, 5			;向上
			JMP EndSwitch
Case3:		ADD POS_X, 5			;向右
			JMP EndSwitch
Case4:  	ADD POS_Y, 5			;向下
	
EndSwitch:
			MOV CX, N1
			PUSH CX
			MOV CX, Offset PLANEMAP
			PUSH CX
			MOV CX, 0001h
			PUSH CX
			PUSH POS_Y
			PUSH POS_X
			CALL drawCraft			;在此处画一个新的飞机
			ADD SP, 10
EndMovePlane:
			POP CX
			POP BX
			POP AX
			MOV SP, BP 
			POP BP
			RET
movePlane ENDP

;程序暂停6000s
delay PROC 	NEAR
			PUSH CX
			MOV CX, 0
delayLoop:
			INC CX
			CMP CX, 6000
			JB delayLoop			;如果CX < 6000则继续
			POP CX
			RET
delay ENDP

;当按下空格时发出子弹,首先要绘制子弹
fireMissile	PROC NEAR	
		 	PUSH BP
			MOV BP, SP
	      
			PUSH CX
			PUSH DX
			PUSH SI
			PUSH DI
			
			MOV CX, [BP+4]			;Pos_X
			MOV DX, [BP+6]			;Pos_Y
			SUB DX, 5
			MOV SI, Offset MISSILE	;将始址移为子弹的始址
fireMissileLoop:
			CMP Word Ptr [SI], '$$'	;比较子弹的结束符
			JZ  fireMissileIf		;如果不是子弹的话
			ADD SI, 4
			JMP fireMissileLoop
fireMissileIf:
			MOV [SI], CX			;[SI] = Pos_X
			MOV [SI+2], DX			;[SI] = Pos_Y - 5
			
			MOV DI, N2
			PUSH DI
			MOV DI, Offset MISSILEMAP
			PUSH DI
			MOV DI, 0003h			;传入颜色
			PUSH DI
			PUSH DX
			PUSH CX
			CALL drawCraft			;通过调整为MISSILEMAP开始绘制子弹
			ADD SP, 10
			
			INC MISSILESNUM			;增加总共发出子弹的数目
			POP DI
			POP SI
			POP DX
			POP CX
			MOV SP, BP
			POP BP
			RET
fireMissile  ENDP

;使所有在屏幕上的子弹往前走
riseMissile PROC NEAR
			PUSH BP
			MOV BP, SP
			
			PUSH SI
			PUSH CX
			PUSH DX
				
			MOV SI, Offset MISSILE	;将SI移到子弹列表中
			MOV CX, 256
riseMissileLoop:		  
			CMP Word Ptr [SI], '$$'	;如果是字符尾
			JZ  riseMissileIf		;跳转
			
			MOV DX, N2
			PUSH DX
			MOV DX, Offset MISSILEMAP
			PUSH DX 
			MOV DX, 0000h
			PUSH DX
			MOV DX, Word Ptr [SI+2]
			PUSH DX
			MOV DX, Word Ptr [SI]
			PUSH DX
			CALL drawCraft			;擦除原有的子弹
			ADD SP, 10
			
			SUB Word Ptr [SI+2],2	;使子弹向上,POS_Y--
			JLE riseMissileIf2		;如果越界,则抹除这个子弹的存在
			
			MOV DX, N2
			PUSH DX
			MOV DX, Offset MISSILEMAP
			PUSH DX 
			MOV DX, 0003h
			PUSH DX
			MOV DX, Word Ptr [SI+2]
			PUSH DX
			MOV DX, Word Ptr [SI]
			PUSH DX
			CALL drawCraft			;绘制新的子弹
			ADD SP, 10
			
			JMP riseMissileIf
riseMissileIf2:
			MOV Word Ptr [SI], '$$'
			MOV Word Ptr [SI+2], '$$'
			DEC MISSILESNUM			;抹除越界子弹的X,Y以及数量
riseMissileIf:	
			ADD SI, 4 
			LOOP riseMissileLoop	;一直重复擦除旧的子弹,绘制新的子弹
			
			POP DX
			POP CX
			POP SI
			POP AX	
			
			MOV SP, BP
			POP BP
			RET
riseMissile ENDP

;使用系统时间生成随机数
randByBX	PROC NEAR
			PUSH AX
			PUSH CX
			PUSH DX
			MOV AH, 0				;CX:DX＝时钟“滴答”计数
			INT 1Ah					;读取时钟“滴答”计数
			MOV AX, DX
			TEST AX, 000000001b		;若为奇数时间
			JZ ODD
			SHR AX, 1				;否则减半
			JMP LOC2
ODD: 		SHL AX, 1				;奇数时间则翻倍
LOC2:		XOR AX, 01011111b
			SUB AX, 3214
			XOR AX, 10111100b
			ADD AX, 30124
			MOV CX, 250
			MOV DX, 0
			DIV CX
			ADD DX, 50
			MOV BX, DX				;获取随机值
			POP DX
			POP CX
			POP AX
			RET 
randByBX ENDP

;随机生成敌机
generateEnemy	PROC NEAR
				PUSH BP
				MOV BP, SP
				PUSH BX
				PUSH SI
				
				MOV BX, N3
				PUSH BX
				MOV BX, Offset ENEMYMAP
				PUSH BX
				MOV BX, 0002h
				PUSH BX
				MOV BX, 00h
				PUSH BX				;Pos_Y = 00h,从最上方下落
				CALL randByBX
				PUSH BX				;随机获取的Pos_X
				CALL drawCraft
				ADD SP, 10
				
				MOV SI, Offset ENEMY;读取敌人的坐标
generateEnemyLoop:
				CMP Word Ptr [SI], '$$'
				JZ  generateEnemyIF
				ADD SI, 2
				JMP generateEnemyLoop
generateEnemyIF:
				MOV Word Ptr[SI], BX
				MOV Word Ptr[SI+2], 00h
				
				INC ENEMYNUM		;敌人数目加一
				POP SI
				POP BX
				MOV SP, BP
				POP BP 
				RET
generateEnemy ENDP

;向下移动所有敌机
dropEnemy PROC NEAR 
		  PUSH BP
		  MOV BP, SP
		  
		  PUSH SI
		  PUSH CX
		  PUSH DX
			    
		  MOV SI, Offset ENEMY		;移动到存储敌机位置数组的始址
		  MOV CX, 256
dropEnemyLoop:		  
		  CMP Word Ptr [SI], '$$'	;如果没有敌机了
		  JZ  dropEnemyIf
		  
		  MOV DX, N3
		  PUSH DX
		  MOV DX, Offset ENEMYMAP
		  PUSH DX 
		  MOV DX, 0000h
		  PUSH DX
		  MOV DX, Word Ptr [SI+2]
		  PUSH DX
		  MOV DX, Word Ptr [SI]
		  PUSH DX
		  CALL drawCraft			;擦除一个敌机
		  ADD SP, 10
		  
		  
		  INC Word Ptr [SI+2]		;向下移动敌机
		  CMP Word Ptr [SI+2], 200	;与下边界判断
		  JAE dropEnemyIf2
		  
		  MOV DX, N3
		  PUSH DX
		  MOV DX, Offset ENEMYMAP
		  PUSH DX 
		  MOV DX, 0002h
		  PUSH DX
		  MOV DX, Word Ptr [SI+2]
		  PUSH DX
		  MOV DX, Word Ptr [SI]
		  PUSH DX
		  CALL drawCraft			;绘制一个新的敌机
		  ADD SP, 10
		  
		  JMP dropEnemyIf
dropEnemyIf2:
		  SUB SCORE, 5				;如果敌机掉落到下边界,则分数减5
		  MOV Word Ptr [SI], '$$'
		  MOV Word Ptr [SI+2], '$$'
		  DEC ENEMYNUM	  			;清楚该敌机
dropEnemyIf:	
		  ADD SI, 4 				;继续处理下一架敌机
		  LOOP dropEnemyLoop
		  
		  POP DX
		  POP CX
		  POP SI
		  POP AX	
		    
		  MOV SP, BP
		  POP BP
		  RET
dropEnemy ENDP

;判断子弹和敌机、敌机和我方飞机是否相撞
checkCollision 	PROC NEAR	
				PUSH BP
				MOV BP, SP	

				PUSH AX
				PUSH BX
				PUSH CX
				PUSH DX
				PUSH SI
				PUSH DI
				
				MOV SI, Offset ENEMY
				MOV DI, Offset MISSILE
				MOV AX, 0
				MOV BX, 0
checkCollisionLoop1:
				;判断是不是敌机
				CMP Word Ptr [SI], '$$'
				JZ  checkCollisionIf
				
				MOV CX, POS_X
				SUB CX, Word Ptr[SI];把目前的敌机的X位置与我方飞机进行比较
				JGE checkCollisionLoc1
				NEG CX				;CX取反加1
checkCollisionLoc1:
				;如果POS_X - [SI] > 8则转移
				CMP CX, 8
				JA checkCollisionLoop2
				
				MOV DX, POS_Y
				SUB DX, Word Ptr[SI+2]
				JGE checkCollisionLoc2;比较Y方向的差距
				NEG DX				;置CF = 1
checkCollisionLoc2:
				CMP DX, 1			;如果DX > 1,则转移,否则游戏结束
				JA checkCollisionLoop2

				JMP GAMEEND
checkCollisionLoop2:	  
				CMP Word Ptr [DI], '$$'
				JZ  checkCollisionIf3
				
				MOV CX, Word Ptr[SI]
				SUB CX, Word Ptr[DI]
				JGE checkCollisionLoc3	;判断敌机和子弹是否相撞
				NEG CX
checkCollisionLoc3:
				CMP CX, 5
				JA checkCollisionIf3
				
				MOV DX, Word Ptr[SI+2]
				SUB DX, Word Ptr[DI+2]
				JGE checkCollisionLoc4
				NEG DX
checkCollisionLoc4:
				CMP DX, 5
				JA checkCollisionIf3
				
				JMP deleteEnemy		;如果相撞则消除敌机
checkCollisionIf3:  
				INC BX
				ADD DI, 4
				CMP BX, 256
				JB  checkCollisionLoop2
checkCollisionIf:
				ADD SI, 4
				MOV BX, 0
				INC AX
				CMP AX, 256			;判断循环是否终止
				MOV DI, Offset MISSILE
				JB checkCollisionLoop1 
				JMP checkCollisionEnd;如果循环已终止,则结束该函数
deleteEnemy:		  
				MOV DX, N3
				PUSH DX
				MOV DX, Offset ENEMYMAP
				PUSH DX 
				MOV DX, 0000h
				PUSH DX
				MOV DX, Word Ptr [SI+2]
				PUSH DX
				MOV DX, Word Ptr [SI]
				PUSH DX
				CALL drawCraft
				ADD SP, 10
				MOV Word Ptr [SI], '$$'
				MOV Word Ptr [SI+2], '$$'
				DEC ENEMYNUM
				ADD SCORE, 2		;消除敌机的同时增加分数
				MOV DX, SCORE
				CMP DX, HIGHEST		;并且与最高分做比较
				JL checkCollisionIf3
				MOV HIGHEST, DX
				JMP checkCollisionIf3
GAMEEND:
				MOV AX, 0003h
				INT 10h
				CALL delay			;如果游戏结束,程序暂停
				PUTS GAMEOVER
				;显示最高分
				PUSH HIGHEST
				CALL showScoreByDemical
				ADD SP, 2
				MOV AX, 4C00h
				INT 21h
checkCollisionEnd: 
				POP DI
				POP SI 
				POP DX
				POP CX
				POP BX
				POP AX
				MOV SP, BP	
				POP BP	
				RET
checkCollision ENDP

;展现分数
showScoreByDemical 	PROC NEAR
					PUSH BP
					MOV BP,SP
					SUB SP,2
					PUSH AX
					PUSH BX
					PUSH CX
					PUSH DX
					
					MOV Byte Ptr [BP-2],5
					MOV AX, [BP+4]
					MOV CX, 0
					MOV BX, 10
					OR AX, AX
					JNS showRep1
					NEG AX
					PUSH AX
					
					MOV DH, 1
					MOV DL, [BP-2]
					ADD Byte Ptr [BP-2],1
					MOV AH, 02h
					INT 10h
					MOV AH, 0Ah
					MOV AL, '-'
					MOV CX, 1
					INT 10h
					POP AX
					MOV CX, 0
showRep1:
					MOV DX, 0
					DIV BX
					ADD DX, '0'
					PUSH DX
					INC CX
					OR AX, AX
					JNZ showRep1  
showRep2:
					POP DX
					MOV AL, DL
					MOV DH, 1
					MOV DL, [BP-2]
					ADD Byte Ptr [BP-2],1
					MOV AH, 02h
					INT 10h 		;置光标位置,BH = 页号,DH = 行,DL = 列
					MOV AH, 0Ah
					PUSH CX
					MOV CX, 1
					INT 10h			;在光标位置只显示字符,BH = 显示页,AL = 字符,CX = 字符重复次数
					POP CX
					LOOP showRep2
					
					POP DX
					POP CX
					POP BX
					POP AX
					MOV SP,BP
					POP BP
					RET
showScoreByDemical ENDP
_TEXT ENDS
END Start