from Karakter import *
from Savas_Mekanigi import *
from Ekran import *
from Tower import *

clear_console()
input("Hero's Journey Demosuna Hosgeldin")
kontrol = input()
your_character = check_in(kontrol)
karakter = Karakter_read(f"{your_character.name}.json")
zindan = tower(100)

zindana_giris(karakter, zindan)
Karakter_write(karakter)

