from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client
import keys
url = 'https://crypto.com/price'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.find('table', class_ = 'chakra-table css-1qpk7f7' )

for record in table_rows.find_all('tbody'):
    rows = record.find_all('tr')
    for row in rows[:5]:
        td = row.findAll('td') # list
        

        change = float(td[4].text.replace('%',''))
        
        #coin = row.find('td', class_ = 'css-w6jew4').text
        #print(coin)
        
        name = row.find('p', class_ = 'chakra-text css-rkws3').text
        symbol = row.find('span', class_ = 'chakra-text css-1jj7b1a').text
        price = float(row.find('div', class_ = 'css-b1ilzc').text.replace('$','').replace(',',''))
        #change = float(row.find('td', class_ = 'css-1vyy4qg').text[20:])
        cor_price = round(price * ((100.00-change)/100.00),2)
        
        
        
        
        print(f"Name: {name}")
        print(f"Symbol: {symbol}")
        print(f"Price: ${price}")
        print(f"% Change: {change}%")
        print(f"Coresponding Price: ${cor_price}")
        input()

        import keys
        
        twilionum = '+17432093120'
        mynum = '+12817702428'
        
        #accountSID = 'AC6516c7b5ee5b728ea186ef1385e70b00'
        #authToken = 'd40f609cb4e3e0c98b66b4df63e559c4'

        client = Client(keys.accountSID,keys.authToken)

        if symbol == 'BTC' and price < 40000.00:
            textmsg = client.messages.create(to=mynum,from_=twilionum,body='Bitcoin Dropped below $40,000!')

        if symbol == 'ETH' and price < 3000.00:
            textmsg = client.messages.create(to=mynum,from_=twilionum,body='Ethereum Dropped below $3,000!')

            



        

       

        