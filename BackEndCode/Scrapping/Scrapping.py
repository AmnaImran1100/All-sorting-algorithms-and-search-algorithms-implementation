from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from csv import writer

path = 'C:\Program Files\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)

next="/paintings?hitsPerPage=100"

with open('PaintingsData.csv', "w", encoding='utf8', newline='') as f:
    
    thewriter =  writer(f)
    header = ['Name', 'Width', 'Height', 'Depth', 'Painter', 'Country','Price']
    thewriter.writerow(header)

    for i in range(250):

        driver.get("https://www.saatchiart.com" + next)
        content = driver.page_source
        soup = BeautifulSoup(content)

        page1 = soup.findAll('div',attrs={'class':'sc-15ws6ki-0 wZWfg'})
        link = soup.find('a',attrs={'title':'Next'})
        next=link['href']

        for i in page1:

            a = i.find('div',attrs={'data-type':'artwork-info'})
            b = i.find('div',attrs={'data-type':'artist-info'})
            c = i.find('div',attrs={'data-type':'prices'})
            d = b.findAll('p')
            
            name= a.p.a.text
            size= a.find('span',attrs={'class':'sc-144xit5-0 juFwTn'})
            size = size.text
            data = size.split(" ")
            width = data[0]
            height = data[3]
            depth = data[6]
            painter = b.p.a.text
            price = c.p.text
            country = d[1].text
            info = [name, width, height, depth, painter, country, price]
            thewriter.writerow(info)










