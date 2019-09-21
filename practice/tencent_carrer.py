#-*-coding:utf-8-*-
import requests
import json

url="https://careers.tencent.com/tencentcareer/api/post/Query?&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=4953&language=zh-cn&area=cn"
response = requests.get(url).content.decode()
with open("tencent.json","w") as f:
    f.write(response)