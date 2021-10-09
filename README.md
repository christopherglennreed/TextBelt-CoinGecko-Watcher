# TextBelt-CoinGecko-Watcher
This is a Python Script built to watch the price of Crypto in USD and send a Text Message. 


This will watch on Crypto via Coin Gecko API and send a Text when it has reached your set threshold. I use the Textbelt API to send the message, so you will have to sign up at a cost https://textbelt.com/,  Sorry. 



-p Phone Number Text Belt Api will reach out to
-a api from TextBelt, do not Share. 
-s The Selling price Example in Decimal format For Example .09
-c Coin you would like to watch from Coin Gecko
-t sleep time or how long until next interval check. In Seconds -t 10 equals 10 seconds. 

Command which need to be fed to python. 

Example of Command Usage

python3.9 args.py -s .22 -p phonenumber -c ravencoin -a 113412341264672457845689456sdgasdfasd -t 10 
