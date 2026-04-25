import csv
import requests
from lxml import etree

url = "https://movie.douban.com/top250"
headers = {"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"}
response = requests.get(url,headers=headers)
data = response.text
data_x = etree.HTML(data)
res1 = data_x.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
res2= data_x.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[1]')

text = [
    ['排名', '电影名称', '导演主演']
]
for i,j in enumerate(res1):
    text_=text.append([i+1,j,res2[i]])
with open('电影单页_xpath.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(text)
























