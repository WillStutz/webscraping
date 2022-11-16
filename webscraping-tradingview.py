from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#print(title.text)
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')		

tablescells = soup.findAll("div",attrs={"class":"table-cell"})

#print(tablescells[0].text)

for cell in tablescells[:7]:
    print(cell.text)


counter = 1

for x in range(5):
    name = tablescells[counter].text
    change = tablescells[counter+2].text
    high = float(tablescells[counter+4].text)
    low = float(tablescells[counter+5].text)

    calc_change = round(((high - low)/low) * 100,2)

    print(name)
    print(f"%change on webpage: {change}")
    print(f"High: {high}")
    print(f"low: {low}")
    print(f"Calculated change %: {calc_change}")
    print()
    print()

    counter += 11





#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

