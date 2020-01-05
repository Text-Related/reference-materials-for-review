# 将阅读理解中的单词出进行统计分析
# 用到str,list,set
# 用到词典
str1 ='''  Could you reproduce Silicon Valley elsewhere, or is there something unique about it?
It wouldn't be surprising if it were hard to reproduce in other countries, because you couldn't reproduce it in most of the US either.What does it take to make a Silicon Valley?
It's the right people. If you could get the right ten thousand people to move from Silicon Valley toBuffalo, Buffalo would become Silicon Valley.
You only need two kinds of people to create a technology hub: rich people and nerds.
Observation bears this out. Within the US, towns have become star, up hubs if and only if theyhave both rich people and nerds. Few startups happen in Miami , for example , because although it's fullof rich people, it has few nerds.It's not the kind of place nerds like.
Whereas Pittsburgh has the opposite problem: plenty of nerds, but no rich people.The top USComputer Science departments are said to be MIT , Stanford , Berkeley , and Carnegie-Mellon. MITyielded Route 128.Stanford and Berkeley yielded Silicon Valley. But what did Carnegie-Mellon yield inPittsburgh ? And what happened in Ithaca, home of Cornell University , which is also high on the list ?'''

str_ls = str1.split()       # 将字符串转成list

set_val = set(str_ls)       # 再将list转换成set，因list中有重复单词，转成set，则留下不重复单词
ls_val = list(set_val)      # 再将转set转成list,这时的list里已经没有重复的单词了

dict_val = dict()                     # 将单词及出现频率，用字典存储

for item in set_val:
	count_tem = str_ls.count(item)    # 统计单词在字符串str_ls中出现的次数
	dict_val[item] = count_tem

print('the following is the list of vacabulary and the corresponding num')
print('{0:20}, {1:3}'.format('vacabulary','num'))

for item in dict_val.items():
	print('{0:20}, {1:<3}'.format(item[0],item[1]))
	
