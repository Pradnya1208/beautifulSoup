import MySQLdb
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
total_cases = []
deaths = []
recovery =[]
attr_name =[]

for values in countries:
    country_name.append((values.text).split("[")[0])
i=1
for entry in data:
    if i%3 == 1:
        total_cases.append(entry.text)
    if i%3 == 2:
        deaths.append(entry.text)
    if i%3 == 3:
        recovery.append(entry.text)
    i += 1

for attr in atr:
    attr_name.append((attr.text).split("[")[0])

attr_name[3] = "Recovery"
#print(total_cases)
#print(country_name)
#print(attr_name)


conn = MySQLdb.connect("mysql.server", "username","password", "database name")

c = conn.cursor()

table_name = "World"
createsqltable = """CREATE TABLE IF NOT EXISTS """ + table_name + " (" + " CHAR(50),".join(attr_name) + " CHAR(50))"
#print (createsqltable)
c.execute(createsqltable)

for x in country_name:
    c.execute("INSERT INTO World(Location) VALUES(%s)", (x,))

for x in total_cases:
    c.execute("INSERT INTO World(Cases) VALUES(%s)", (x,))

for x in deaths:
    c.execute("INSERT INTO World(Deaths) VALUES(%s)", (x,))

for x in recovery:
    c.execute("INSERT INTO World(Recovery) VALUES(%s)", (x,))

DELETE FROM World WHERE Location IS NULL;

conn.commit()
















