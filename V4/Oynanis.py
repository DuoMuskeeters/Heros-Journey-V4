from Karakter import *
from Savas_Mekanigi import *
from Ekran import *
from Hikayeler import * 

clear_console()
input("Hero's Journey Demosuna Hosgeldin")
kontrol = input()
your_character = check_in(kontrol)
karakter = Karakter_tanimlama(f"{your_character.name}.json")

giris()
kontrol2 = input("\nİsterseniz bu yıldız gücüne daha detaylı bakalım.Devam etmek için 2'e basın.")
if kontrol2 == "2":
    Yildiz_Gücü()
if kontrol2 == "2":
    kontrol3 = input("Devam etmek için 3'e basın.") 
    if kontrol3 == "3":
        karakter_anlatim(karakter.name)

#mob = random_mob()
#Savas_Mekanigi(karakter, mob)


