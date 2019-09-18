#-*-coding:utf-8-*-
import os
import requests
from lxml import etree
import random
import json

first_urls=[
      'https://www.meitulu.com/t/yiyang-elly/',
            'https://www.meitulu.com/t/yuejintong/','https://www.meitulu.com/t/sugar-xiaotianxincc/','https://www.meitulu.com/t/chunxiaoxi/','https://www.meitulu.com/t/1280/',
            'https://www.meitulu.com/t/1096/','https://www.meitulu.com/t/1214/','https://www.meitulu.com/t/nixiaoyao/','https://www.meitulu.com/t/mengxinyue-candice/',
            'https://www.meitulu.com/t/1283/','https://www.meitulu.com/t/sugar-xiaotianxincc/','https://www.meitulu.com/t/xiezhixin-sindy/','https://www.meitulu.com/t/1148/',
            'https://www.meitulu.com/t/manuela/','https://www.meitulu.com/t/1166/','https://www.meitulu.com/t/ningmengc-lemon/','https://www.meitulu.com/t/1214/',
            'https://www.meitulu.com/t/xiezhixin-sindy/','https://www.meitulu.com/t/wangyuchun/','https://www.meitulu.com/t/linlin-ailin/','https://www.meitulu.com/t/lixingyi/',
            'https://www.meitulu.com/t/shenmitao-off/','https://www.meitulu.com/t/zhouyanxi/','https://www.meitulu.com/t/wenxinyi/','https://www.meitulu.com/t/1206/','https://www.meitulu.com/t/1148/',
            'https://www.meitulu.com/t/1347/','https://www.meitulu.com/t/mansulana/','https://www.meitulu.com/t/1206/','https://www.meitulu.com/t/zhouyanxi/','https://www.meitulu.com/t/mufeifei/',
            'https://www.meitulu.com/t/1348/','https://www.meitulu.com/t/1165/','https://www.meitulu.com/t/1166/','https://www.meitulu.com/t/liuyuer/','https://www.meitulu.com/t/sabrina/',
            'https://www.meitulu.com/t/guxinyi/','https://www.meitulu.com/t/chenbaola/','https://www.meitulu.com/t/1112/','https://www.meitulu.com/t/foxyini-menghuli/',
            'https://www.meitulu.com/t/1384/','https://www.meitulu.com/t/1216/'
      ]
model_name=''
data=''
urls = []



user_agent_file= json.load(open('user_agent.json','r'))

headers = {'User-Agent': random.choice(user_agent_file)}


for first_url in first_urls:
    if first_url not in urls:
        urls.append(first_url)


for url in urls:
    data = requests.get(url, headers=headers)
    response=data.content.decode()
    # 1.转解析类型
    xpath_data = etree.HTML(response)
    # 2调用 xpath的方法,
    result = xpath_data.xpath('/html/head/title/text()')
    model_name="".join(result).split('|')[0]
    print("now download"+model_name)
    print("url address is :"+url)
    # create model's name path
    name_path="/home/szj/spider/meitu/"+model_name+"/"
    if not os.path.exists(name_path):
        os.mkdir(name_path)


    hrefs=xpath_data.xpath('/html/body/div[2]/div[4]/ul/li/a/@href')

    for i in range(0,len(hrefs)):
        num=hrefs[i].split("/")[4].split(".")[0]
        for j in range(1,120):
            picture_url="https://mtl.ttsqgs.com/images/img/"+num+"/"+str(j)+".jpg"




            # 读取文件json -----list dict
            downloaded_url_txt = json.load(open('02new.json', 'r'))

            # 将下载过的url追加写入文件夹
            if picture_url not in str(downloaded_url_txt):
                picture_response=requests.get(picture_url,headers=headers)
                picture=picture_response.content
                # print(type(picture_response.status_code))
                if (picture_response.status_code != 200):
                   break
                picture_name=name_path+num+str(j)+".jpg"

                with open(picture_name,'wb') as f:
                    f.write(picture)
                    print(picture_name)
                    downloaded_url_txt.append(picture_url)
                    # fp 是 file path
                    fp = open('02new.json', 'w')
                    json.dump(downloaded_url_txt, fp)
                    fp.close()

