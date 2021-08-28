import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

lists= []
for x in range (1,30):
    print(x)
    url = f'https://www.holidayfrancedirect.co.uk/cottages-holidays/index.htm?board=sc&d=France&people=2&prop_type%5B0%5D=cottagegite&page={x}'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    #print(soup.title)

    propertyy = soup.find_all('div',class_ = 'property-grid-item')
    
    for i in propertyy:
        title = i.find('h2').text
        spec = i.find('p', class_ = 'property-spec').text
        price = i.find('div',class_ = 'property-pricing').text
        data = {
            'Title':title,
            "Specs": spec,
            "Price": price
        }
        lists.append(data)
    time.sleep(3)

df = pd.DataFrame(lists)
df.to_csv('France.csv')
