from Savas_Mekanigi import *

def rounding(sayi):
    if isinstance(sayi , int):
        return int(sayi)
    else :
        return int(sayi) + 1

class tower:
    def __init__(self,floor) :
        self.floor = floor
        #self.type = type
    def zindan_tanimlama(self, oyuncu_seviyesi :int):
        sayi = max(1, oyuncu_seviyesi/3)
        if oyuncu_seviyesi % 3 == 0 :
            sayi = int(sayi)
        self.floor = rounding(sayi)
        return self.floor

