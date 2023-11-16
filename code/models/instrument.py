class Instrument:
     
    def __init__(self, name, ins_type, displayName,
                   pipLocation, tradeUnitsPrecision, marginRate):
          self.name = name
          self.ins_type = ins_type
          self.displayName = displayName
          self.pipLocation = pow(10, pipLocation)    # הופך את ה-4 ל0.0001
          self.tradeUnitsPrecision = tradeUnitsPrecision
          self.marginRate = float(marginRate)

    def __repr__(self):
     return str(vars(self))    # the instrument (self) itself is not an 'official' dict,
                               # vars(self) just give the dictionary version so we can use the str

    #מקבל אובייקט של אינסטרומנט ומחזיר אינסטרומנט חדש עם השדות   
    @classmethod
    def FromApiObject(cls, ob):
        return Instrument(
            ob['name'],
            ob['type'],
            ob['displayName'],
            ob['pipLocation'],
            ob['tradeUnitsPrecision'],
            ob['marginRate'],
        )
    