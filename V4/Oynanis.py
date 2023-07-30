from Karakter import *
from Savas_Mekanigi import *
from Ekran import *

clear_console()
input("Hero's Journey Demosuna Hosgeldin")
kontrol = input()
your_character = check_in(kontrol)
karakter = Karakter_tanimlama(f"{your_character.name}.json")


#mob = random_mob()
#Savas_Mekanigi(karakter, mob)



