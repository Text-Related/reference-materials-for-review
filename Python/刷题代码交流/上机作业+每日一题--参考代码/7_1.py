# 编程实现使用文本文件保存随机生成的5组,每组10个分数）比赛分数，以逗号分隔；
# 打开保存的文件，读取并计算每队的平均分数并打印；

import random

num = 5
f_score = open('scores.txt','w')                    # 保存分数的文件
for i in range(num):                                  # 有4个队参加比赛
	for j in range(10):                             # 有10个评委进行打分
		tem_score = random.randint(70,99)           # 生成一个随机数  
		f_score.write('{0:<3}'.format(tem_score))   # 写到文件中
		if j <9:
			f_score.write(',')
	f_score.write('\n')
f_score.close()

f_r_score = open('scores.txt','r')                  # 读取文件
scores = []                                         # 保存数据的list
lines = f_r_score.readlines()                       # 把文件中的内容全部读入到lines中
for line in lines:                                  # 对读取的每行数据进行操作
	ls_score = line.split(',')                        # 按,进行切分
	float_score = [float(item) for item in ls_score]  # 因读取数据默认是字符串格式，这里需做一步转换，将字符数据转成float数据
	scores.append(float_score)                        # 将转换后的数据，放置于列表scores中 

ave_scores = []                                     # 存放平均得分的列表
for i in range(len(scores)):
	ave_tem = sum(scores[i]) /len(scores[i])
	ave_scores.append(ave_tem)

for i in range(num):
	print('第{0}队平均分为：{1}'.format(i+1,ave_scores))
f_r_score.close()