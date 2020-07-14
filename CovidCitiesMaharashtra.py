import pandas as pd

from bs4 import BeautifulSoup
import requests


c_name = []
urls = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Maharashtra"
covid_world = requests.get(urls)
soup_world = BeautifulSoup(covid_world.content, 'html.parser')


container = soup_world.find("table", class_= "wikitable plainrowheaders sortable")
attr = container.find("tbody")
table_col = attr.find("tr")
column= table_col.find_all("th")
data = []
city_data = []
for i in column:
    c_name.append((i.text).split("\n")[0])
    
for tr in attr.find_all('tr')[1:]:
    data += tr.find_all('th') + tr.find_all('td')

for d in data:
    city_data.append(((d.text).split("[")[0]).split("\n")[0])
    
    

n = len(column)
c1 = [city_data[i * n:(i + 1) * n] for i in range((len(city_data) + n - 1) // n )]
    
#brics = pd.DataFrame(c1, columns=c_name)
#print(brics)
