class ApiPrice:

    def __init__(self, api_ob):
        self.instrument = api_ob['instrument']
        self.ask = api_ob['asks'][0]['price']
        self.bid = api_ob['bids'][0]['price']
        self.sell_conv = float(api_ob['quoteHomeConversionFactors']['negativeUnits'])
        self.buy_conv = float(api_ob['quoteHomeConversionFactors']['positiveUnits'])
        
    def __repr__(self):
        return f"ApiPrice() {self.instrument} {self.ask} {self.bid} {self.sell_conv} {self.buy_conv}"