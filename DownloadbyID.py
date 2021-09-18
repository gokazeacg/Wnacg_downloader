from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import wget
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
print('輸入編號：')
no = str(input())
url = str('https://wnacg.org/photos-slide-aid-'+no+'.html')
executable_path = 'chromedriver'
driver = webdriver.Chrome(executable_path=executable_path,options=chrome_options)
driver.set_page_load_timeout(300)
driver.get(url)
tempname = driver.title
name = tempname.replace('- 列表 - 紳士漫畫-專註分享漢化本子|邪惡漫畫','')
soup = BeautifulSoup(driver.page_source)
#print(soup.prettify())
img = soup.find_all('img')
num = 0
imglist = []
for tag in img:
  #print(tag.get('src'))
  imglist.append(tag.get('src'))
del imglist[0]
#print(imglist)
os.system('mkdir /home/g6172506/'+"'"+name+"'")
for num in range(0,len(imglist)):
    url = str(imglist[num])
    if num <= 9:
        num = str(num)
        os.system("wget"+" "+"http:"+url+" "+"-O "+"'"+"/home/g6172506/"+name+"/00"+num+".jpg"+"'")
    elif num <= 99:
        num = str(num)
        os.system("wget"+" "+"http:"+url+" "+"-O "+"'"+"/home/g6172506/"+name+"/0"+num+".jpg"+"'")
    else:
        num = str(num)
        os.system("wget"+" "+"http:"+url+" "+"-O "+"'"+"/home/g6172506/"+name+"/"+num+".jpg"+"'")
driver.quit()
os.system('pkill chrome')
os.system('zip -r '+"'"+name+"'"+" '"+name+"'")
