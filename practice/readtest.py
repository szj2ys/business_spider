#-*-coding:utf-8-*-
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

lists=[]

for url in first_urls:
      lists.append(url)
      # fp 是 file path
      fp = open('02new.json', 'w')
      json.dump(lists, fp)
      fp.close()


# 读取文件json -----list dict
resulst = json.load(open('02new.json', 'r'))

print(resulst)