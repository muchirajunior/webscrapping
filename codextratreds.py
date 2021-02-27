from bs4 import BeautifulSoup
import requests

source=requests.get("https://codextratrends.com/").text
soup=BeautifulSoup(source,'html5lib')

cartegory=[]
titles=[]
links=[]
dates=[]

for i in soup.find_all('span', class_="post-tag"):
    cartegory.append(i.text.replace(" ",''))

data=soup.find_all('div', attrs={'class':"post-content media"})
for item in data:
    titles.append(item.h4.text.replace(' ',''))
    links.append(item.a['href'].replace(' ',''))


for i in soup.find_all('span', class_="post-date-info"):
    dates.append(i.text.replace(' ',''))

#print all the data
for i in range(len(cartegory)):
    print("cartegory : ",cartegory[i])
    print("title : ",titles[i])
    print("link : ", links[i])
    print("date : ",dates[i])
    print(" ")
    print(" ")
    print(" ")
