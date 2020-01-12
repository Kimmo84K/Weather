import urllib.request
#import matplotlib.pyplot as plt
import csv
import time
import json

def is_number1(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False                


#for i in range(210):
while True: 
        #tiedoston haku netista ja tiedostoon kirjoitus

        urlb = "http://api.openweathermap.org/data/2.5/weather?id=2952984&appid=1788aeb8578afbe75f9947b527218d64&mode=json"
        reqb = urllib.request.Request(urlb)

        rb = urllib.request.urlopen(reqb).read()
        bamberg = json.loads(rb.decode('utf-8'))
        headers_b = urllib.request.urlopen(reqb).headers

        #print(headers_b['date'])
        #print(bamberg['main']['temp'])
        #print(bamberg['main']['pressure'])         
        #print(bamberg['main']['humidity']) 

        urli = "http://api.openweathermap.org/data/2.5/weather?id=656808&appid=1788aeb8578afbe75f9947b527218d64&mode=json"
        reqi = urllib.request.Request(urli)
        ri = urllib.request.urlopen(reqi).read()
        iitti = json.loads(ri.decode('utf-8'))
            
        
        #print(iitti['main']['temp'])
        #print(iitti['main']['pressure'])         
        #print(iitti['main']['humidity']) 
                    
        urlh = "http://api.openweathermap.org/data/2.5/weather?id=658226&appid=1788aeb8578afbe75f9947b527218d64&mode=json"
        reqh = urllib.request.Request(urlh)
        rh = urllib.request.urlopen(reqh).read()
        helsinki = json.loads(rh.decode('utf-8'))
            
        
        #print(iitti['main']['temp'])
        #print(iitti['main']['pressure'])         
        #print(iitti['main']['humidity']) 
                    

        
        #bamberg   
        ltila_bamberg=round(bamberg['main']['temp']-272.15,2)
        #print(ltila_bamberg)
        kosteus_bamberg=bamberg['main']['humidity']
        tuuli_nopeus_bamberg=bamberg['wind']['speed']
        tuuli_suunta_bamberg=bamberg['wind']['deg']
        paine_bamberg=bamberg['main']['pressure']      
        #iitti
        ltila_iitti=round(iitti['main']['temp']-272.15,2)
        kosteus_iitti=iitti['main']['humidity']
        paine_iitti=iitti['main']['pressure']
        tuuli_nopeus_iitti=iitti['wind']['speed']
        tuuli_suunta_iitti=iitti['wind']['deg']
        #helsinki
        ltila_helsinki=round(helsinki['main']['temp']-272.15,2)
        #print(ltila_helsinki)
        kosteus_helsinki=helsinki['main']['humidity']
        print(kosteus_helsinki)
        paine_helsinki=helsinki['main']['pressure']
        print(paine_helsinki)
        tuuli_nopeus_helsinki=helsinki['wind']['speed']
        print(tuuli_nopeus_helsinki)
        tuuli_suunta_helsinki=helsinki['wind']['deg']
        print(tuuli_suunta_helsinki)
        aika = headers_b['date']
        #print(aika)
        #loppu sleeppi
        print(str(aika)+" "+str(ltila_bamberg)+" "+str(kosteus_bamberg)+" "+str(paine_bamberg)+" "+str(tuuli_nopeus_bamberg)+" "+str(tuuli_suunta_bamberg)
              +" "+" "+str(ltila_iitti)+" "+str(kosteus_iitti)+" "+str(paine_iitti)+" "+str(tuuli_nopeus_iitti)+" "+str(tuuli_suunta_iitti)
              +" "+" "+str(ltila_helsinki)+" "+str(kosteus_helsinki)+" "+str(paine_helsinki)+" "+str(tuuli_nopeus_helsinki)+" "+str(tuuli_suunta_helsinki)+"\n")
            
        try:
            tulokset=open("tilastot_uusi.txt","a") 
                
            tulokset.write(str(aika)+" "+str(ltila_bamberg)+" "+str(kosteus_bamberg)+" "+str(paine_bamberg)+" "+str(tuuli_nopeus_bamberg)+" "+str(tuuli_suunta_bamberg)
                           +" "+" "+str(ltila_iitti)+" "+str(kosteus_iitti)+" "+str(paine_iitti)+" "+str(tuuli_nopeus_iitti)+" "+str(tuuli_suunta_iitti)
                           +" "+" "+str(ltila_helsinki)+" "+str(kosteus_helsinki)+" "+str(paine_helsinki)+" "+str(tuuli_nopeus_helsinki)+" "+str(tuuli_suunta_helsinki)+"\n")
                
            tulokset.close()

            
        except:
            virheet=open("virheet.txt","a")
            virheet.write(str(aika)+",virhe arvoissa\n")
            virheet.close()

        try:
            js_tulokset = {}
            js_tulokset['bamberg']=[]
            js_tulokset['bamberg'].append({
                'ltila':ltila_bamberg,
                'kosteus':kosteus_bamberg,
                'paine':paine_bamberg,
                'tuuli_nopeus':tuuli_nopeus_bamberg,
                'tuuli_suunta':tuuli_suunta_bamberg,
                'aika': aika
                })
            js_tulokset['iitti']=[]
            js_tulokset['iitti'].append({
                'ltila':ltila_iitti,
                'kosteus':kosteus_iitti,
                'paine':paine_iitti,
                'tuuli_nopeus':tuuli_nopeus_iitti,
                'tuuli_suunta':tuuli_suunta_iitti,
                'aika': aika
                })
            js_tulokset['helsinki']=[]
            js_tulokset['helsinki'].append({
                'ltila':ltila_helsinki,
                'kosteus':kosteus_helsinki,
                'paine':paine_helsinki,
                'tuuli_nopeus':tuuli_nopeus_helsinki,
                'tuuli_suunta':tuuli_suunta_helsinki,
                'aika': aika
                })
            with open('js_tilastot.txt','a') as outfile:
                json.dump(js_tulokset,outfile, indent=2)
                
        except:
            print("virhe")
            
        time.sleep(1800)
    
