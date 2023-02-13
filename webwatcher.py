import requests
import argparse
import time


parser=argparse.ArgumentParser(description="provided to send your text messages to your phone to alert you about CoinGecko info")
parser.add_argument('-p', help="Phone Number Text Belt Api will reach out to" ,dest="phone", type=str, required=True)
parser.add_argument('-a', help="api from TextBelt" ,dest="key", type=str, required=True)
parser.add_argument('-u',help="url to watch" ,dest="url", type=str, required=False)
parser.add_argument('-t',help="sleep time" ,dest="time", type=int, required=True)
args=parser.parse_args()

Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


while True:
  data = requests.get(url=args.url, headers=Headers)
  data = data.text
  txtmsg = "looks good to buy!" + (args.url) 
  if not "This product is excluded from all promotional" in data : 
     print("Time to buy as the shoes are no longer prevented from discount")
     resp = requests.post('https://textbelt.com/text', {
       'phone': args.phone,
       'message': txtmsg,
       'key': args.key,
     })
     print(resp.json())

  time.sleep(args.time)
  continue
  
  
  ### EXAMPLE of usage python webwather.py -p 8003647667 -a 1casdfasdfasdagdga234461342y5rgfdsgf -u "https://google.com" -t 150 
