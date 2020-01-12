import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import csv
import time
from matplotlib.ticker import MaxNLocator

#kaavion tulostus        
x=[]    #aika
y=[]    #lämpötilaccc


with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    #print(plots)
    x.clear()
    y.clear()
    for row in plots:
        #print(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(float(row[6]))
        

plt.plot(x,y,label="Bamberg Lämpötila,$^\circ$ C")
plt.xlabel("aika")
plt.ylabel("lämpötila,$^\circ$ C")
plt.title("lämpötila aika")
plt.legend()
plt.xticks(rotation='vertical')

plt.show()


with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()

    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(int(row[7]))
        

plt.plot(x,y,label="Bamberg Kosteus, %")
plt.xlabel("aika")
plt.ylabel("Kosteus, %")
plt.title("kosteus, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(int(row[8]))
        

plt.plot(x,y,label="Bamberg Paine, hPa")
plt.xlabel("aika")
plt.ylabel("Paine, hPa")
plt.title("Paine, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(float(row[9]))
        

plt.plot(x,y,label="Bamberg tuuli nopeus, m/s")
plt.xlabel("aika")
plt.ylabel("tuuli nopeus, m/s")
plt.title("Tuuli, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(int(row[10]))
        

plt.plot(x,y,label="Bamberg tuuli suunta, asteet")
plt.xlabel("aika")
plt.ylabel("tuuli suunta, asteet")
plt.title("Tuuli suunta, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()
#Iitti
with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    #print(plots)
    x.clear()
    y.clear()
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(float(row[12]))
        

plt.plot(x,y,label="Iitti Lämpötila,$^\circ$ C")
plt.xlabel("aika")
plt.ylabel("lämpötila,$^\circ$ C")
plt.title("lämpötila aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()


with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()

    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(int(row[13]))
        

plt.plot(x,y,label="Iitti Kosteus, %")
plt.xlabel("aika")
plt.ylabel("Kosteus, %")
plt.title("kosteus, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(int(row[14]))
        

plt.plot(x,y,label="Iitti Paine, hPa")
plt.xlabel("aika")
plt.ylabel("Iitti Paine, hPa")
plt.title("Iitti Paine, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(float(row[15]))
        

plt.plot(x,y,label="Iitti tuuli nopeus, m/s")
plt.xlabel("aika")
plt.ylabel("tuuli nopeus, m/s")
plt.title("Tuuli, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(int(row[16]))
        

plt.plot(x,y,label="Iitti tuuli suunta, asteet")
plt.xlabel("aika")
plt.ylabel("tuuli suunta, asteet")
plt.title("Tuuli suunta, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

#Helsinki
with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    #print(plots)
    x.clear()
    y.clear()
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(float(row[18]))
        
plt.plot(x,y,label="Helsinki Lämpötila,$^\circ$ C")
plt.xlabel("aika")
plt.ylabel("lämpötila,$^\circ$ C")
plt.title("lämpötila aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()


with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()

    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(float(row[19]))
        

plt.plot(x,y,label="Helsinki Kosteus, %")
plt.xlabel("aika")
plt.ylabel("Kosteus, %")
plt.title("kosteus, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(int(row[20]))
        

plt.plot(x,y,label="Helsinki Paine, hPa")
plt.xlabel("aika")
plt.ylabel("Helsinki Paine, hPa")
plt.title("Helsinki Paine, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(float(row[21]))
        

plt.plot(x,y,label="Helsinki tuuli nopeus, m/s")
plt.xlabel("aika")
plt.ylabel("tuuli nopeus, m/s")
plt.title("Tuuli, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(row[0]+row[1]+row[2]+row[3]+" - "+row[4])
        y.append(int(row[22]))
        

plt.plot(x,y,label="Helsinki tuuli suunta, asteet")
plt.xlabel("aika")
plt.ylabel("tuuli suunta, asteet")
plt.title("Tuuli suunta, aika")
plt.legend()
plt.xticks(rotation='vertical')
plt.show()


