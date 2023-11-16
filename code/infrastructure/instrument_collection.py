import json
from models.instrument import Instrument

class InstrumentCollection:
    FILENAME = "instruments.json"
    API_KEYS = ['name', 'type', 'displayName', 'pipLocation',
        'displayPrecision', 'tradeUnitsPrecision', 'marginRate']

    def __init__(self):
        self.instrument_dict = {}
    
    #from file to instruments_dict
    #הפונקציה תקח מקובץ ג'סון בשם הקבוע שלמעלה שאנחנו נספק את המיקום שלו ותעמיס את התוכן לתוך האובייקט
    def LoadInstruments(self, path):
        self.instrument_dict = {}
        fileName = f"{path}/{self.FILENAME}"
        with open(fileName, "r") as f:
            data = json.loads(f.read()) #הופך קובץ שיש בו ג'סון לאובייקט פייתון
            for k, v in data.items():
                self.instrument_dict[k]=Instrument.FromApiObject(v)

    #from api to file (through instruments_dict)
    #data = comes from the api (data = api.get_account_instruments)
    def CreateFile(self, data, path):
        if data is None:
            print("Instrument file creation failed")
            return
        
        instruments_dict = {}
        for i in data:
            key = i['name']
            instruments_dict[key] = { k: i[k] for k in self.API_KEYS }
        
        fileName = f"{path}/{self.FILENAME}"
        with open(fileName,  "w") as f:
            f.write(json.dumps(instruments_dict, indent=2))

    def PrintInstruments(self):
        [print(k,v) for k,v in self.instrument_dict.items()]
        print(len(self.instrument_dict.keys()), "instruments")
    
instrumentCollection = InstrumentCollection()