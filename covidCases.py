from bs4 import BeautifulSoup
import requests


countries = []
data = []
atr = []

urls = "https://en.wikipedia.org/wiki/COVID-19_pandemic"
covid_world = requests.get(urls)
soup_world = BeautifulSoup(covid_world.content, 'html.parser')


container = soup_world.find(id = "covid19-container")
container_data = container.find("tbody")
container_data_attr = container.find("tr", class_ = "covid-sticky")


atr += container_data_attr.find_all('th')[0:4]

for tr in container_data.find_all('tr')[2:]:
    countries += tr.find_all('th')[1:]
    data += tr.find_all('td')[:-1]


country_name =[]
country_data = []
attr_name =[]

for values in countries:
    country_name.append((values.text).split("[")[0])

for d in data:
    country_data.append(d.text)

for attr in atr:
    attr_name.append((attr.text).split("[")[0])

print(country_data)
print(country_name)
print(attr_name)

















