from bs4 import BeautifulSoup
import requests

source= requests.get('https://www.nse.co.ke/market-statistics.html').text
source2=requests.get('https://www.nse.co.ke/market-statistics.html?start=50').text
stock=BeautifulSoup(source,'html5lib')
stocks=BeautifulSoup(source2,'html5lib')

companies=[]
table=stock.find_all('table',attrs={'class':"marketStats table table-striped"})

date=[]
for i in table:
    date.append(i.thead.tr.td.div.div.strong.text)

for i in table:
    companies.append(i.tbody.tr.td)

print(date)