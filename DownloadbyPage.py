from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import wget
import os

print('輸入頁數：')
no = str(input())
indexurl = str('https://wnacg.org/albums-index-page-'+no+'-cate-9.html')
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
executable_path = 'chromedriver'
driver = webdriver.Chrome(executable_path=executable_path,options=chrome_options)
driver.set_page_load_timeout(300)
driver.get(indexurl)
indexsoup = BeautifulSoup(driver.page_source)
driver.quit()
booklink = indexsoup.find_all('a')
del booklink[0:25]
del booklink[len(booklink)-9:]
#print(booklink[1::2])
booklist = []
for tag in booklink[1::2]:
  #print(tag.get('href'))
  hreflist = str(tag.get('href'))
  hreflist = hreflist.replace('/photos-index-aid-','')
  hreflist = hreflist.replace('.html','')
  #print(hreflist)
  booklist.append(hreflist)
print(booklist)
for booklistnum in booklist:
  no = str(booklistnum)
  url = str('https://wnacg.org/photos-slide-aid-'+no+'.html')
  print(url)
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
  executable_path = 'chromedriver'
  driver = webdriver.Chrome(executable_path=executable_path,options=chrome_options)
  driver.set_page_load_timeout(300)
  driver.get(url)
  tempname = driver.title
  name = tempname.replace('- 列表 - 紳士漫畫-專註分享漢化本子|邪惡漫畫','')
  print(name)
  soup = BeautifulSoup(driver.page_source)
  driver.quit()
  img = soup.find_all('img')
  num = 0
  imglist = []
  for tag in img:
    #print(tag.get('src'))
    imglist.append(tag.get('src'))
  del imglist[0]
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
  os.system('zip -r '+"'"+name+"'"+" '"+name+"'")
os.system('pkill chrome')
