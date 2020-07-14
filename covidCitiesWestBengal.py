from bs4 import BeautifulSoup
import requests


countries = []
data = []
atr = []
city_data= []

urls = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_West_Bengal"
covid_world = requests.get(urls)
soup_world = BeautifulSoup(covid_world.content, 'html.parser')


container = soup_world.find(id = "covid19-container")
container_data = container.find("tbody")
container_data_attr = container.find("tr", class_ = "covid-sticky")


atr += container_data_attr.find_all('th')[:-1]

for tr in container_data.find_all('tr')[3:]:
    countries += tr.find_all('th') + tr.find_all('td')


country_d =[]


for values in countries:
    z = ((values.text).split("[")[0]).split("\n")[0]
    if not "2020" in z:
        country_d.append(z)
    
attr_name = []
n = len(atr)
c1 = [country_d[i * n:(i + 1) * n] for i in range((len(country_d) + n - 1) // n )]

for attr in atr:
    attr_name.append((attr.text).split("[")[0])

print(c1)


