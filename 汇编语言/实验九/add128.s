	.file	"add128.cpp"
	.text
	.globl	__Z6add1286int128S_RS_
	.def	__Z6add1286int128S_RS_;	.scl	2;	.type	32;	.endef
__Z6add1286int128S_RS_:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %edx
	movl	24(%ebp), %eax
	addl	%eax, %edx
	movl	40(%ebp), %eax
	movl	%edx, (%eax)
	movl	12(%ebp), %edx
	movl	28(%ebp), %eax
	adcl	%eax, %edx
	movl	40(%ebp), %eax
	movl	%edx, 4(%eax)
	movl	16(%ebp), %edx
	movl	32(%ebp), %eax
	adcl	%eax, %edx
	movl	40(%ebp), %eax
	movl	%edx, 8(%eax)
	movl	20(%ebp), %edx
	movl	36(%ebp), %eax
	adcl	%eax, %edx
	movl	40(%ebp), %eax
	movl	%edx, 12(%eax)
	nop
	popl	%ebp
	ret