/*add2.s*/
	.file	"add2.cpp"			# 源程序名称
	.text
	.globl	__Z3addii			# 定义子程序名称
	.def	__Z3addii;	.scl	2;	.type	32;	.endef
__Z3addii:
	pushl	%ebp				# 将bp寄存器的值push进栈
	movl	%esp, %ebp			# bp = sp
	movl	8(%ebp), %edx		# dx = 8(%ebp) = a
	movl	12(%ebp), %eax		# ax = 12(%ebp) = b
	addl	%edx, %eax			# eax = b+a
	leal	-1(%eax), %edx
	movl	12(%ebp), %eax
	subl	8(%ebp), %eax
	imull	%edx, %eax
	shr 	$1, %eax
	popl	%ebp				# 还原bp的值，即指向源代码的位置
	ret
	.ident	"GCC: (tdm-1) 4.9.2"
