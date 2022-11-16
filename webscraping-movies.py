
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll("tr")

for row in table_rows[:6]:
    #print(row)
    #input()
    td =  row.findAll("td")
    if td:
        rank = td[0].text
        release = td[8].text
        total_gross = int(td[7].text.replace('$','').replace(',',''))
        distributor = td[9].text
        theaters = int(td[6].text.replace(',',''))
        avg_revenue = round(total_gross/theaters)

        print(f'Rank: {rank}')
        print(f'Release Date: {release}')
        print(f'Total Gross: ${total_gross}')
        print(f'Average Revenue per theater: ${avg_revenue}')
        print(f'Distributor: {distributor}')
        #print(f'Average Revenue per theater: {avg_revenue}')
        input()








