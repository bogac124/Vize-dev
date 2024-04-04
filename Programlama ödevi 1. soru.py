import numpy as np
import matplotlib.pyplot as plt
import random


deneme_sayisi = 0
g = 9.81
aci = np.radians(30)
hedef_xaxis = 20000+200*random.randint(-10,10)
alt_sinir_hiz = 330
üst_sinir_hiz = 1800

while(True):
    ilk_hiz= (alt_sinir_hiz + üst_sinir_hiz)/2
    yüksekliğe_ucus = 2 * ilk_hiz * np.sin(aci) / g
    toplam_süre1 = 2 * ilk_hiz * np.sin(aci) / g  
    toplam_süre= np.linspace(0, toplam_süre1, 100)
    
    max_yüksekliğe_süresi = np.linspace(0,yüksekliğe_ucus/2,100)
    mesafe= ilk_hiz* np.cos(aci) * toplam_süre
    yükseklik= 4 + ilk_hiz * np.sin(aci) * toplam_süre - 0.5 * g * toplam_süre ** 2
    maks_yükseklik = 4 + ilk_hiz * np.sin(aci) * max_yüksekliğe_süresi - 0.5 * g * max_yüksekliğe_süresi ** 2
    
    if( hedef_xaxis == mesafe[-1] or hedef_xaxis+1000 > mesafe[-1] >hedef_xaxis-1000 ):
        print("hedefi vurdunuz")
        print("vurmak için gereken hiz",ilk_hiz)
        print("deneme sayisi",deneme_sayisi)
        print("max yükseklik",maks_yükseklik[-1])

        break
    elif(hedef_xaxis+1000 >= mesafe[-1]):
        print("hedefin önünde")
        alt_sinir_hiz = alt_sinir_hiz + 80

    elif(hedef_xaxis-1000 <= mesafe[-1]):
        print("hedefin arkasında")
        üst_sinir_hiz = üst_sinir_hiz - 100


    deneme_sayisi += 1

r = 500
daire_aci1 = np.linspace(0, 2 * np.pi, 360)
merkez1x = hedef_xaxis + r * np.cos(daire_aci1)
merkez1y = 0 + r * np.sin(daire_aci1)
plt.fill(merkez1x, merkez1y, color='green', alpha=1)


plt.plot(merkez1x, merkez1y)

plt.plot(mesafe, yükseklik)
plt.xlim(0,24000)
plt.ylim(0,10000)


plt.title('deneme sayisi' + str(deneme_sayisi))
plt.xlabel('mesafe (m)')
plt.ylabel('yükseklik (m)')
plt.grid(True)
plt.show()
    
    
    
    
    
    
        
        
    
    
    


















