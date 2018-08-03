#!/usr/bin/python
#coding=utf-8

import urllib
import sys
import re

word ="contain"
print "单词：" + word

searchUrl = "http://dict.youdao.com/search?q=+ word + &keyfrom=dict.index"	#查找的地址
response = urllib.urlopen(searchUrl).read() #获得查找到的网页源码

#从网页源码提取出单词释义那一部分
searchSuccess = re.search(r"(?s)<div class=\"trans-container\">\s*<ul>.*?</div>",response)

if searchSuccess:
	means = re.findall(r"(?m)<li>(.*?)</li>",searchSuccess.group()) #获取我们想提取的核心单词释义
	print "释义："
	for mean in means:
		print "\t" + mean	#输出释义
else:
	print "未查找到释义."