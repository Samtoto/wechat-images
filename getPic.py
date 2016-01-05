# -*- coding : utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os


url = "http://mp.weixin.qq.com/s?__biz=MzA3NzIxMjY5OQ==&mid=211462573&idx=3&sn=5282c265482ad233620523db0f0830b1&scene=1&srcid=0104SYaXa2kcwwBLk269ys6h#rd"

res = requests.get(url)

# resText = ""
# with open(res.text, 'a+') as fp:
#     resText = fp.read()
soup = BeautifulSoup(res.text)
# print soup.prettify()
print '***********title***********'
# print type(soup.title)
# print type(soup.find('title'))
print u'make folder'
print soup.title.string
os.mkdir(soup.title.string)

print '***********get img src*********'

for img in soup.find_all('img'):
    src = img.get('data-src')

    print src

    if src:
        # print '**********************'
        imgTit = src[50:80]
        # print '**********************'
        srcFmt = src[src.find('wx_fmt')+7:]
        if srcFmt == 'jpeg':
            srcFmt = 'jpg'

        with open('./'+soup.title.string+'/'+imgTit + '.' + srcFmt, 'wb') as f:
            f.write(requests.get(src).content)
        # print srcFmt
    # print url.find('mp.')

