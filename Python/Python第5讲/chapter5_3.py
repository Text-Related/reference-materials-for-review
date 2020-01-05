# 将单词表中的英文单词分出来

word4s = ['abandon vt.丢弃;放弃，抛弃','ability n.能力;能耐，本领','abnormal a.不正常的;变态的','aboard ad.在船(车)上;上船',
      'abroad ad.(在)国外;到处','absence n.缺席，不在场;缺乏','absent a.不在场的;缺乏的','absolute a.绝对的;纯粹的',
      'absolutely ad.完全地;绝对地','absorb vt.吸收;使专心','abstract a.抽象的 n.摘要','abundant a.丰富的;大量的']

word4s_original = []                  # 保存切分出来的英文单词
print('把list中的每个元素按空格切分（因每个元素中只有一个空格，所以只分成两部分）')
for item in word4s:
	s = item.split()
	print(s)                  # split 默认按空格进行切分   
	print(s[0])               # s[0]保存的是空格前面的单词，如 abandon
	print(s[1])               # s[1]保存的是空格后面的内容，如 vt.丢弃;放弃，抛弃
	print()
	word4s_original.append(s[0])  # 将英文单词保存在列表中word4s_original
print('-----------单词列表-----------')
print(word4s_original)
