from Karakter import *
from Savas_Mekanigi import *
from Tower import *

clear_console()
input("Hero's Journey Demosuna Hosgeldin")
kontrol = input()
your_character = check_in(kontrol)
your_character.karakter_read()
zindan = tower(100)
zindana_giris(your_character, zindan)
your_character.karakter_write()

