import requests
import argparse
import time


parser=argparse.ArgumentParser(description="provided to send your text messages to your phone to alert you about CoinGecko info")
parser.add_argument('-p', help="Phone Number Text Belt Api will reach out to" ,dest="phone", type=str, required=True)
parser.add_argument('-a', help="api from TextBelt" ,dest="key", type=str, required=True)
parser.add_argument('-s', dest="sell", type=float, required=True, help="The Selling price Example in Decimal format For Example 09")
parser.add_argument('-c',help="Coin you would like to watch from Coin Gecko" ,dest="coin", type=str, required=False)
parser.add_argument('-t',help="sleep time" ,dest="time", type=int, required=True)
args=parser.parse_args()


while True:
  sellrvn = args.sell
  data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+ str(args.coin) +"&vs_currencies=USD")
  data = data.json()
  data = (data[('%s' % (args.coin,))]['usd'])
  print(data)
  txtmsg = "Time to sell, Current Price is " + str(data)
  if data > sellrvn: 
     print("Time to sell " + str(data) + " is the current price")
     resp = requests.post('https://textbelt.com/text', {
       'phone': args.phone,
       'message': txtmsg,
       'key': args.key,
     })
     print(resp.json())

  time.sleep(args.time)
  continue
