from api.oanda_api import OandaApi 
from infrastructure.instrument_collection import instrumentCollection
import time

if __name__ == '__main__':
    api = OandaApi()  
    instrumentCollection.LoadInstruments("./data")
    trade_id = api.place_trade("EUR_USD", -100, 1)
    time.sleep(5)
    api.close_trade(trade_id)