ls = [9,7,8,3,2,1,5,6]
# ls_new = []
# for item in ls:
# 	if item % 2 == 0:
# 		item = item * item
# 	ls_new.append(item)
# print(ls)
# print(ls_new)

for i in range(len(ls)):
	item = ls[i]
	if item % 2 == 0:
		ls[i] = item * item
print(ls)
