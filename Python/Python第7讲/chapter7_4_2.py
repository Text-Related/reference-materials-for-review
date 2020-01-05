def outer_func():
	tax_rate = 0.17 #局部变量示例
	print('outer func tax_rate = ',tax_rate)
	def innner_func():
		nonlocal tax_rate
		tax_rate = 0.05
		print('inner func tax_rate = ',tax_rate)
	innner_func()
	print('outer func tax_rate = ',tax_rate)
outer_func() #测试代码

