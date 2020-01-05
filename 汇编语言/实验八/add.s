	.file	"add.cpp"				# 源程序名称
	.text
	.globl	__Z3addii			# 定义子程序名称
	.def	__Z3addii;	.scl	2;	.type	32;	.endef
__Z3addii:
	pushl	%ebp				# 将bp寄存器的值push进栈
	movl	%esp, %ebp			# bp = sp
	movl	8(%ebp), %edx		# dx = 8(%ebp) = a
	movl	12(%ebp), %eax	# ax = 12(%ebp) = b
	addl	%edx, %eax			# ax = ax + dx
	popl	%ebp					# 还原bp的值
	ret
	.ident	"GCC: (tdm-1) 4.9.2"
