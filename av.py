#coding:utf-8
import urllib2
import json
import time
import jieba

start = 1

words = {}
f = open("comment", "w")
while start < 600:
    url = "https://api.douban.com/v2/movie/subject/26100958/comments?start={0}&count={1}&apikey=your_own_api_key".format(start,20)
    data = urllib2.urlopen(url, timeout=5)
    j = json.load(data)
    for comment in j["comments"]:
        f.write(comment["content"].encode("utf8"))
        
        word_list = jieba.cut(comment["content"].replace('\n','').encode("utf8"))
        for word in word_list:
            word = word.strip()
            if words.get(word):
                words[word] = words[word] + 1
            else:
                words[word] = 1
    start = start + 20 

f.close()
sorted_words = sorted(words.items(), key=lambda d: d[1], reverse=True)
for item in sorted_words:
    print item[0].encode("utf8"), item[1]
