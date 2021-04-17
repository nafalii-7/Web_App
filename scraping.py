from bs4 import BeautifulSoup
import requests
import datetime


## scraping data
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

url1 ='http://www.covidmaroc.ma/Pages/AccueilAR.aspx'
url2 = 'https://covid.hespress.com/'

reception = requests.get(url1,headers=header).text
response = requests.get(url2).text

soup = BeautifulSoup(reception,'lxml')
soup2 = BeautifulSoup(response, 'lxml')

             
cas_confirmes = soup2.find('h4' ,class_ = 'mb-0 font-30').text
test_total = soup.find('span',class_='ms-rteFontSize-5').text
les_guerri = soup.find('span',class_='ms-rteForeColor-6 ms-rteFontSize-3').text
les_decede = soup.find('span',class_='ms-rteThemeForeColor-9-4 ms-rteFontSize-5').text
vaccination = soup2.find('h4' , class_ = 'mb-0').text


# afficher la date 
date = datetime.date.today()
print(date)


# afficher les données scrapées

print("\n\n le nombre de tests totals est :",test_total)
print("\n\n les cas confirmés sont :", cas_confirmes)
print("\n\n le nombre des guerries est :",les_guerri)
print("\n\n le nombre des décedé est :",les_decede)

x = vaccination.split()
print('\n \n personnes vaccinées dose 1 :', x[2],x[3],x[4])
print('\n \n personnes vaccinées dose 2 :', x[7],x[8],x[9])


# mettre les données en fichier csv 


    
    
targetList_var = ([date, test_total, cas_confirmes, les_guerri , les_decede ,vaccination  ])

with open('covid19_data.csv' , "a", encoding="utf-8") as f:
    f.write(str(targetList_var))
