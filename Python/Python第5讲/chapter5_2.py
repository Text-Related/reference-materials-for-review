# 辩论赛
# 用到tuple和list,循环

teams = ('信科','经管','体育','物理')
avescores = []
scores = ((98,87,99,98,80,97,86,70,80,98),(95,85,89,88,86,95,89,98,85,80),
          (81,89,77,71,71,73,95,75,79,89),(80,71,90,92,86,92,96,88,82,80))

for i in range(len(teams)):
	ave_tem  = ( sum(scores[i]) - max(scores[i]) -min(scores[i]) )/(len(scores[i])-2)
	avescores.append(ave_tem)

max_score = max(avescores)
idx = avescores.index(max_score)     # 求最高分所在组的下标
team_idx = teams[idx]
print('获得最高分的院系是：{0}, 得分为：{1}',team_idx,max_score)
