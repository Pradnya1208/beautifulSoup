from bs4 import BeautifulSoup
import requests


countries = []
data = []
atr = []


urls = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States"
covid_world = requests.get(urls)
soup_world = BeautifulSoup(covid_world.content, 'html.parser')


container = soup_world.find(id = "covid19-container")
container_data = container.find("tbody")
container_data_attr = container.find("tr", class_ = "covid-sticky")


atr += container_data_attr.find_all('th')[:-2]

for tr in container_data.find_all('tr')[3:]:
    countries += tr.find_all('th') + tr.find_all('td')[:-2]

country_d =[]

for values in countries:
    z = ((values.text).split("[")[0])
    if not z == "\n":
        country_d.append(z.split("\n")[0])


attr_name = []
n = len(atr)
c1 = [country_d[i * n:(i + 1) * n] for i in range((len(country_d) + n - 1) // n )]

for attr in atr:
    attr_name.append((attr.text).split("[")[0])
    
print(attr_name)
print(country_d)
print(c1)

