from bitmex_websocket import BitMEXWebsocket
import logging
from time import sleep
from mongo_order import *
symbol = input('symbol = (ex.XBTUSD)')
exchange = "bitmex"
mongo = MongoOrder('trade','testprice')
# Basic use of websocket.
def run():
   logger = setup_logger()

   # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
   ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol=symbol,
                        api_key='W3P6SJrm4T4n1ZunuvFqHTh7', api_secret='VdyjaXtF5Wx9NPlBS04VmDA9AcNIGfUCRuhN6OImxgo0ezo6')

   #logger.info("Instrument data: %s" % ws.get_instrument())

   # Run forever
   #currentPrice = ws.get_ticker()
   instriment = ws.get_instrument()
   bid = 0
   ask = 0
   bidsize = 0
   asksize = 0
   while(ws.ws.sock.connected):
      instrument = ws.get_instrument()
      quote = ws.get_quote()
      #print (quote)
      logger.info("bid price/size: %s %s ask price/size: %s %s" ,instrument['bidPrice'],quote['bidSize'],instrument['askPrice'],quote['askSize'])
      newbid = instrument['bidPrice']
      newask = instrument['askPrice']
      newbidsize = quote['bidSize']
      newasksize = quote['askSize']
      if(bid != newbid or ask != newask or bidsize != newbidsize or asksize != newasksize):
         data = {'market':symbol,'exchange':exchange,'bid':newbid,'bidSize':newbidsize,'ask':newask,'askSize':newasksize}
         mongo.UpdateFieldByExchange(exchange,data)
         ask = newask
         bid = newbid
         bidsize = newbidsize
         asksize = newasksize
         print ("save!")

      #if ws.api_key:
      #    logger.info("Funds: %s" % ws.funds())
      #logger.info("Market Depth: %s" % ws.market_depth())
      #logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
      sleep(1)

def setup_logger():
   # Prints logger info to terminal
   logger = logging.getLogger()
   logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
   ch = logging.StreamHandler()
   # create formatter
   formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
   # add formatter to ch
   ch.setFormatter(formatter)
   logger.addHandler(ch)
   return logger

if __name__ == "__main__":
   run()