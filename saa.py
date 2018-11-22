import urllib.request
#import matplotlib.pyplot as plt
import csv
import time

def is_number1(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False                


i=0

#for i in range(210):
while True: 
        #tiedoston haku netista ja tiedostoon kirjoitus
    try:
        try:
            osoite_bamberg = "http://api.openweathermap.org/data/2.5/weather?id=2952984&appid=1788aeb8578afbe75f9947b527218d64&mode=xml"
            sivu = urllib.request.urlopen(osoite_bamberg)
            bamberg_apu =sivu.read()
            teksti =bamberg_apu.decode("UTF-8")
            tiedosto_bamberg = open("bamberg.txt","w")
            tiedosto_bamberg.write(teksti)
            tiedosto_bamberg.close()


            osoite_iitti = "http://api.openweathermap.org/data/2.5/weather?id=656808&appid=1788aeb8578afbe75f9947b527218d64&mode=xml"
            sivu = urllib.request.urlopen(osoite_iitti)
            iitti_apu =sivu.read()
            teksti =iitti_apu.decode("UTF-8")
            tiedosto_iitti = open("iitti.txt","w")
            tiedosto_iitti.write(teksti)
            tiedosto_iitti.close()

        except:
            virheet=open("virheet.txt","a")
            virheet.write(str(aika_apu)+",ei internetyhteytta\n")
            virheet.close()
                    
        #Tiedoston luku
        data=open("bamberg.txt","r")
        rivit_bamberg = str(data.readlines())
        data.close()

        data=open("iitti.txt","r")
        rivit_iitti = str(data.readlines())
        data.close()

        #tiedoston siivous
        sana = "temperature value"
        sana2 = "lastupdate value"
        sana3 = "humidity value"
        sana4 = "pressure value"
        #sana5="weather number"
                

        for alku in range(len(rivit_bamberg)):
            loppu=alku+len(sana)
            if rivit_bamberg[alku:loppu] ==sana:
                #print("loytyzi:",alku,loppu)
                alku= (rivit_bamberg[240:245])

                if is_number1(alku)==True:
                    ltila_bamberg_apu=alku
                else:
                    ltila_bamberg_apu=alku[:4]
                    
        for alku2 in range(len(rivit_bamberg)):
            loppu2=alku2+len(sana2)
            if rivit_bamberg[alku2:loppu2]==sana2:
                #print("loytyzi:",alku2,loppu2)
                aika_bamberg=(rivit_bamberg[(loppu2+2):(loppu2+2+19)])
                aika_bamberg_apu=(aika_bamberg[8:10]+aika_bamberg[11:13]+aika_bamberg[14:16])
                #print(aika_bamberg_apu)

        for alku3 in range(len(rivit_bamberg)):
            loppu3=alku3+len(sana3)
            if rivit_bamberg[alku3:loppu3]==sana3:
                #print("loytyzi:",alku2,loppu2)
                siirto_bamberg=(rivit_bamberg[(loppu3+2):(loppu3+2+2)])
                if is_number1(siirto_bamberg)==True:
                    kosteus_bamberg=siirto_bamberg
                else:
                    kosteus_bamberg=siirto[:1]
                    
                #print(apu)

            
        for alku4 in range(len(rivit_bamberg)):
            loppu4=alku4+len(sana4)
            if rivit_bamberg[alku4:loppu4]==sana4:
                #print("loytyzi:",alku2,loppu2)
                paine_bamberg_apu=(rivit_bamberg[(loppu4+2):(loppu4+2+4)])
                if is_number1(paine_bamberg_apu)==True:
                    paine_bamberg=paine_bamberg_apu
                else:
                    paine_bamberg=paine_bamberg_apu[:3]
                        
                    #print(apu)
                    
                                
                #print(is_number1(s))
                #print(is_number2(t))

        if is_number1(ltila_bamberg_apu) == True & is_number1(kosteus_bamberg)== True & is_number1(aika_bamberg_apu)==True & is_number1(paine_bamberg)==True:
            ltila_bamberg_apu2=float(ltila_bamberg_apu)
            ltila_bamberg=ltila_bamberg_apu2-273.15
            ltila_bamberg=round(ltila_bamberg,2)
                    
        #iittin tiedoston kasittely
        for alkuk in range(len(rivit_iitti)):
            loppuk=alkuk+len(sana)
            if rivit_iitti[alkuk:loppuk] ==sana:
         #       print("ltila:",alkuk,loppuk)
                alkuk= (rivit_iitti[237:243])

                if is_number1(alkuk)==True:
                    ltila_iitti_apu=alkuk
                else:
                    ltila_iitti_apu=alkuk[:4]
                #print(ltila_iitti_apu)
                
        for alku2k in range(len(rivit_iitti)):
            loppu2k=alku2k+len(sana2)
            if rivit_iitti[alku2k:loppu2k]==sana2:
             #       print("aika:",alku2k,loppu2k)
                aika_iitti_apu=(rivit_iitti[(loppu2k+2):(loppu2k+2+19)])
                aika_apu_iittik=(aika_iitti_apu[8:10]+aika_iitti_apu[11:13]+aika_iitti_apu[14:16])
                #print(aika_apu_iittik)

        for alku3k in range(len(rivit_iitti)):
            loppu3k=alku3k+len(sana3)
            if rivit_iitti[alku3k:loppu3k]==sana3:
                # print("kosteus:",alku3k,loppu3k)
                kosteus_iitti_apu=(rivit_iitti[(loppu3k+2):(loppu3k+2+2)])
                if is_number1(kosteus_iitti_apu)==True:
                    kosteus_iitti=kosteus_iitti_apu
                else:
                    kosteus_iitti=kosteus_iitti_apu[:1]
                    
                #print(kosteus_iitti)

            
        for alku4k in range(len(rivit_iitti)):
            loppu4k=alku4k+len(sana4)
            if rivit_iitti[alku4k:loppu4k]==sana4:
                #print("paine:",alku4k,loppu4k)
                paine_iitti_apu=(rivit_iitti[(loppu4k+2):(loppu4k+2+4)])
                if is_number1(paine_iitti_apu)==True:
                    paine_iitti=paine_iitti_apu
                else:
                    paine_iitti=paine_iitti_apu[:3]
                        
                #print(paine_iitti)
                    
                     



            
                #print(is_number1(s))
                #print(is_number2(t))

        if is_number1(ltila_iitti_apu) == True & is_number1(kosteus_iitti)== True & is_number1(aika_apu_iittik)==True & is_number1(paine_iitti)==True:
            ltila_iitti_apu2=float(ltila_iitti_apu)
            ltila_iitti_apu2=ltila_iitti_apu2-273.15
            ltila_iitti=round(ltila_iitti_apu2,2)



        #loppu sleeppi
            tulokset=open("tilastot_uusi.txt","a") 
                    #print(ltila_bamberg_apu)

            tulokset.write(str(aika_bamberg_apu)+" "+str(ltila_bamberg)+" "+str(kosteus_bamberg)+" "+str(paine_bamberg)+" "+" "+" "+str(ltila_iitti)+" "+str(kosteus_iitti)+" "+str(paine_iitti)+ "\n")
                
            tulokset.close()
        else:
            virheet=open("virheet.txt","a")
            virheet.write(str(aika_bamberg_apu)+", Virheellinen arvo tiedostossa\n")
            virheet.close()


            
    except:
        virheet=open("virheet.txt","a")
        virheet.write(str(aika_apu)+",ei internetyhteytta\n")
        virheet.close()

    i=i+1
    time.sleep(1800)
    
