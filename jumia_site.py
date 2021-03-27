import requests
from bs4 import BeautifulSoup

source=requests.get("https://www.jumia.co.ke/phones-tablets/").text
soup=BeautifulSoup(source,'html5lib')

data=[]
for item in soup.find_all('header',class_="row _no-g -fw-nw -j-bet -i-ctr -phm -mh-48px"):
    head=item.h2.text
    data.append(str(head))
names=[]
for item in soup.find_all('div',class_='name'):
    name=item.text
    names.append(name)
for item in soup.find_all('h3',class_='name'):
    name=item.text
    names.append(name)

prices=[]
for item in soup.find_all('div', class_='prc'):
    price=item.text#.replace("KSh ",'')
    prices.append(price)
    # price=price.replace(',','')
    # price=str(price)
    # if (price!=''):
    #     price=int(price)
    #     prices.append(price)
    
print("headers :",data)
print()

for item in range(len(names)):
    print (names[item]," ",prices[item])

