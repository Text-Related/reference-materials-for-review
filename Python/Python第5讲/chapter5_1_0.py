# 辩论赛,用到tuple和list

teams = ('信科','经管','体育','物理')
avescores = []
scores1 = (98,87,99,98,80,97,86,70,80,98)
scores2 = (95,85,89,88,86,95,89,98,85,80)
scores3 = (81,89,77,71,71,73,95,75,79,89)
scores4 = (80,71,90,92,86,92,96,88,82,80)

ave_1 = 0
for sc in scores1:
    ave_1 += sc
    
ave_1 -= max(scores1)
ave_1 -= min(scores1)
ave_1 /=(len(scores1)-2)
    
#ave_1 = (sum(scores1) - max(scores1) -min(scores1))/(len(scores1)-2)
avescores.append(ave_1)

ave_2 = (sum(scores2) - max(scores2) -min(scores2))/(len(scores2)-2)
avescores.append(ave_2)

ave_3 = (sum(scores3) - max(scores3) -min(scores3))/(len(scores3)-2)
avescores.append(ave_3)

ave_4 = (sum(scores4) - max(scores4) -min(scores4))/(len(scores4)-2)
avescores.append(ave_4)

print('参赛队伍：',end=' ')
for nam in teams:
    print(str.format('{0:10}',nam),sep=',',end=' ')
print()    
print('得分情况：',end=' ')    
for ave in avescores:
    print(str.format('{0:10}',ave),sep=',',end=' ')
print() 
max_score = max(avescores)
idx = avescores.index(max_score)     # 求最高分所在组的下标
team_idx = teams[idx]
print(str.format('获得最高分的院系是：{0}, 得分为：{1}',team_idx,max_score))

