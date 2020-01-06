#12-05每日一题，构造无重复数字的三位数。有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？请打印输出。 
#思路提示：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

lst = []
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if(i !=j and j != k and i != k):
				t = i*100+ j*10 + k
				lst.append(t)

print('the total num is:',len(lst))
print(lst)