from Karakter import *
from Savas_Mekanigi import *
from Ekran import *
import time

def anlatim(metin :str, timer : int):
    print(metin)
    time.sleep(timer)

def giris():
    anlatim("Etharya: Yıldız Gücüyle Dolu Bir Dünya", 3)
    anlatim("\nYüzyıllar önce, Etharya adlı büyülü bir dünya doğdu. Bu benzersiz evren, yıldızlardan gelmeyen ancak tüm varlıkların ruhlarında doğuştan var olan gizemli bir enerji kaynağı ile doludur." , 7)
    anlatim("İnsanlar bu güce Yıldız Gücü derler. ", 3)
    anlatim("Bu enerji, sadece savaş için değil, aynı zamanda hayatın her yönünü etkileyecek kadar hayati bir öneme sahiptir." , 5)
    anlatim("Yıldız Gücü, insanların günlük yaşamlarını, evlerini, tarlalarını ve ormanları korumak ve beslemek için kullanılır", 5)
    anlatim("Aynı zamanda sanat, zanaat ve tıp gibi alanlarda da büyük bir etkendir.", 3)
    anlatim("Büyücüler, hekimler, marangozlar ve diğer ustalar, Yıldız Gücü'nü ustaca kullanarak muhteşem eserler ve iyileştirici çözümler yaratırlar.",7)

def Yildiz_Gücü():
    anlatim("\nEtharya'da, her insan doğuştan Yıldız Gücü'ne sahiptir ancak bu gücü tam anlamıyla kullanmak için eğitim ve çaba gereklidir.",7)
    anlatim("İnsanlar, Yıldız Gücü Seviyeleri olarak adlandırılan bir hiyerarşiye göre sınıflandırılır",5)    
    anlatim("Bu seviyeler, sosyal sınıfların ve statülerin belirlenmesinde önemli bir ölçüttür", 3)    
    anlatim("Herkes, doğduğunda 1. Seviye ile başlar ve bu seviyeyi geliştirmek için Yıldız Gücü Okulu'na katılmak zorundadır.\n\n",5)    

def karakter_anlatim(karakter_adi):
    print(f"\nAna karakterimiz {karakter_adi}, sıradan bir ailenin çocuğu olarak, etkileyici güzellikteki Yıldız Gücü Köyü'nde doğar")
    time.sleep(5)
    anlatim("Bu köy, doğanın büyülü dokusunun içinde barış içinde yaşayan huzurlu bir yerdir. ",5)
    print(f"{karakter_adi}'ın ailesi, saygın ve örnek bir ailedir. Babası, bir marangoz olmasına rağmen, marangozluk zanaatını Yıldız Gücü'nü kullanarak daha büyülü ve özel eserler yaratmada kullanır")
    time.sleep(7)
    anlatim("Annesi, halkın iyiliği ve refahı için çalışan sevecen bir kadındır",3)
    print(f"{karakter_adi}, küçük yaşlardan itibaren, Yıldız Enerjisi'nin sırlarına ve büyülü hikayelere olan merakıyla büyür")
    time.sleep(5)
    anlatim("Geceleri, gökyüzündeki yıldızları izler ve içinde bu gizemli enerjiyi hisseder.",3)
    anlatim("Çevresindeki diğer çocuklarla oyun oynarken dahi, Yıldız Gücü'ne doğuştan gelen bir kabiliyetle diğerlerinden farklı olduğunu fark eder.",5)
    