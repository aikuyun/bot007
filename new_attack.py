# -*- coding: UTF-8 -*-
# The function of this script is to automatically crawl the news
# and then integrate and release it to yuque.

"""
date: 2019-10-26
author: cuteximis
"""

import requests
import sys
import json
import time

reload(sys)
sys.setdefaultencoding('utf-8')

# 设置请求头，其中 XXX 是语雀的 Token
headers = {
'X-Auth-Token':'XXXX',
'Content-Type':'application/json',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
# 知识库的命名空间
namespace = 'cuteximi/daily/'
# API 基础路径
base_url = 'https://www.yuque.com/api/v2/'

response = requests.get('https://36kr.com/pp/api/newsflash?per_page=100')
# dict 类型
data = json.loads(response.text)
# 文档图片,一周 7 张
imgs = {
'1':'![zb01.png](https://cdn.nlark.com/yuque/0/2019/png/199648/1572081941357-5446f157-cd2a-4eb0-a536-084b89c3e3c9.png#align=left&display=inline&height=310&name=zb01.png&originHeight=1000&originWidth=2404&search=&size=147661&status=done&width=746)'
,'2':'![zb07.png](https://cdn.nlark.com/yuque/0/2019/png/199648/1572081941523-02b5fe51-3df9-41e4-af42-b3038ef15001.png#align=left&display=inline&height=350&name=zb07.png&originHeight=1028&originWidth=2194&search=&size=143124&status=done&width=746)'
,'3':'![zb06.png](https://cdn.nlark.com/yuque/0/2019/png/199648/1572081941715-d1e034af-588a-44b9-8b7f-b8ad73caef5e.png#align=left&display=inline&height=964&name=zb06.png&originHeight=964&originWidth=2248&search=&size=137729&status=done&width=2248)'
,'4':'![zb05.png](https://cdn.nlark.com/yuque/0/2019/png/199648/1572081941841-18d5537e-ac32-4fc4-8ede-833696710f62.png#align=left&display=inline&height=946&name=zb05.png&originHeight=946&originWidth=2092&search=&size=129793&status=done&width=2092)'
,'5':'![zb04.png](https://cdn.nlark.com/yuque/0/2019/png/199648/1572081941963-114050ed-3074-431c-9125-b9310c3f7ae1.png#align=left&display=inline&height=1000&name=zb04.png&originHeight=1000&originWidth=2214&search=&size=139787&status=done&width=2214)'
,'6':'![zb03.png](https://cdn.nlark.com/yuque/0/2019/png/199648/1572081942090-251a93f1-76b3-4040-bedb-8e6c0e19de4c.png#align=left&display=inline&height=976&name=zb03.png&originHeight=976&originWidth=2298&search=&size=142590&status=done&width=2298)'
,'0':'![zb02.png](https://cdn.nlark.com/yuque/0/2019/png/199648/1572081942201-30eea89e-cfe4-4b1f-a7e6-b0a78f8f8985.png#align=left&display=inline&height=984&name=zb02.png&originHeight=984&originWidth=2408&search=&size=147392&status=done&width=2408)'
}

# 文档更新时间 & 标题
doc_update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
doc_time = time.strftime("%Y-%m-%d", time.localtime())
doc_tile = '精选互联网早报 {doc_time}'.format(doc_time = doc_time)

# 根据周几，选择图片
img_index = time.strftime("%w", time.localtime())

# 生成文档正文
doc_content = imgs[img_index]+'\n\n'+' > 精选互联网早报，每天 8 点准时更新。'+'\n\n'
for item in data['data']['items']:
    title = '### [{a}]({b})'.format(a = item['title'],b = item['news_url'])
    desc = item['description']
    doc_content = doc_content+'\n\n'+title+'\n\n'+desc
# print(body_content)
"""
Key: Description 可选
title: 标题
slug: 文档 Slug
public: 0 - 私密，1 - 公开
format: 支持 markdown 和 lake，默认为 markdown 可选
body: format 描述的正文内容，最大允许 5MB
"""
params_data = {"title":doc_tile,"slug":doc_time,"public":'1',"format":'markdown',"body":doc_content}
post_data = json.dumps(params_data)

# print(post_data)

# 文档更新接口
url=base_url+'repos/'+namespace+'docs/'
response = requests.post(url,headers=headers,data=post_data)

print(response)

# data = json.loads(response.text)

# print(data)
