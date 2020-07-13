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
    country_name.append(((values.text).split("[")[0]).split("\n")[0])
i=1
for entry in data:
    if i%3 == 1:
        tc = (entry.text).split("\n")[0]
        tc = tc.replace(',','')
        total_cases.append(tc)
    if i%3 == 2:
        dt = (entry.text).split("\n")[0]
        dt = dt.replace(',','')
        deaths.append(dt)
    if i%3 == 0:
        rec = (entry.text).split("\n")[0]
        rec = rec.replace(',','')
        recovery.append(rec)
    i += 1

for attr in atr:
    attr_name.append((attr.text).split("[")[0])

attr_name[3] = "Recovery"
#print(total_cases)
#print(country_name)
#print(attr_name)




conn = MySQLdb.connect("pradnyapatil.mysql.pythonanywhere-services.com", "pradnyapatil","N126p@punep", "pradnyapatil$default")

c = conn.cursor()
table_name = "covid"
createsqltable = """CREATE TABLE IF NOT EXISTS """ + table_name + " (" + " VARCHAR(50),".join(attr_name) + " VARCHAR(50))"
print (createsqltable)
c.execute(createsqltable)



for (x,x1,x2,x3) in zip(country_name,total_cases,deaths,recovery):
    c.execute("INSERT INTO covid(Location,Cases,Deaths,Recovery) VALUES(%s, %s, %s, %s)", (x,x1,x2,x3,))


conn.commit()

















