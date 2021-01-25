from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree

url = "https://m.weibo.cn/detail/4595707808060645"
#实例化一个浏览器对象
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument(r"C:\Users\29429\AppData\Local\Google\Chrome\User Data")
chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
myWeb = webdriver.Chrome(options=chromeOptions)
#让myWeb向特定url发起请求
myWeb.get(url)
#获得网页源代码
sleep(100)
page_text = myWeb.page_source
#获得etree对象
t = open('微博评论_复工.txt','w',encoding='utf-8')
tree = etree.HTML(page_text)
news_li_list = tree.xpath('//div[@class="comment-content"]/div')
for li in news_li_list:
     news_name = li.xpath('./div//div[@class="m-text-box"]/h3/text()')
     if len(news_name)!=0:
          t.write(news_name[0]+'\n')
myWeb.quit()
