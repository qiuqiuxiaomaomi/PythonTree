# -*- coding: utf-8 -*-

import jieba
from gensim import corpora, models, similarities
from collections import defaultdict

#定义文件目录
workdir = "E:\\scrapyfile\\"
f1 = workdir + "a.txt"
f2 = workdir + "b.txt"
c1 = open(f1, "rb").read().decode("gbk").encode("utf-8")
c2 = open(f2, "rb").read().decode("gbk").encode("utf-8")

#jieba分词
data1 = jieba.cut(c1)
data2 = jieba.cut(c2)

data11 = ""
for i in data1:
    data11 += i + " "

data21 = ""
for i in data2:
    data21 += i + " "

doc1 = [data11, data21]
print doc1

t1 = [[word for word in doc.split()]
      for doc in doc1]

freq = defaultdict(int)
for i in t1:
    for j in i:
        freq[j] += 1

t2 = [[token for token in k if freq[j] >= 3]
      for k in t1]
print t2

dict1 = corpora.Dictionary(t2)
dict1.save(workdir + "yuliaoku.txt")

f3 = workdir+"c.txt"
c3 = open(f3).read()

#jieba分词
data3 = jieba.cut(c3)
data31 = ""

for i in data3:
    data31 += i + " "

new_doc = data31
print new_doc


new_vec = dict1.doc2bow(new_doc.split())
new_corpor = [dict1.doc2bow(t3) for t3 in t2]
tfidf = models.TfidfModel(new_corpor)

featurenum = len(dict1.token2id.keys())

idx = similarities.SparseMatrixSimilarity(tfidf[new_corpor], num_features=featurenum)
sims = idx[tfidf[new_vec]]
print sims


