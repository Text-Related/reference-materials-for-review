# 从输入字符串中清楚HTML标记
import re
def html_txt(htmlwithtag):
	regex_href = re.compile(r'<.+?>')
	return regex_href.sub('',htmlwithtag)# 替换为空，并返回替换结果

# htmltxt = r'<a href=\"index.html\">Welcome to Python world!</a>'
htm1 = r'<title>北京师范大学 - Beijing Normal University</title>'
htm2 = r'<a style="border-right: 1px solid rgb(212, 211, 206);" href="http://news.bnu.edu.cn/" target="_blank" class="fisrtmenu">师大新闻</a>'
print(html_txt(htm1))
print(html_txt(htm2))