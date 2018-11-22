import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import csv
import time

#kaavion tulostus        
x=[]    #aika
y=[]    #lämpötilaccc


with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    #print(plots)
    x.clear()
    y.clear()
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(int(row[0]))
        y.append(float(row[1]))
        

plt.plot(x,y,label="Bamberg Lämpötila,$^\circ$ C")
plt.xlabel("aika")
plt.ylabel("lämpötila,$^\circ$ C")
plt.title("lämpötila aika")
plt.legend()
plt.show()


with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()

    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(int(row[0]))
        y.append(int(row[2]))
        

plt.plot(x,y,label="Bamberg Kosteus, %")
plt.xlabel("aika")
plt.ylabel("Kosteus, %")
plt.title("kosteus, aika")
plt.legend()
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(int(row[0]))
        y.append(int(row[3]))
        

plt.plot(x,y,label="Bamberg Paine, hPa")
plt.xlabel("aika")
plt.ylabel("Paine, hPa")
plt.title("Paine, aika"+str(row[0]))
plt.legend()
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    #print(plots)
    x.clear()
    y.clear()
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(int(row[0]))
        y.append(float(row[6]))
        

plt.plot(x,y,label="Iitti Lämpötila,$^\circ$ C")
plt.xlabel("aika")
plt.ylabel("lämpötila,$^\circ$ C")
plt.title("lämpötila aika")
plt.legend()
plt.show()


with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()

    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(int(row[0]))
        y.append(int(row[7]))
        

plt.plot(x,y,label="Iitti Kosteus, %")
plt.xlabel("aika")
plt.ylabel("Kosteus, %")
plt.title("kosteus, aika")
plt.legend()
plt.show()

with open("tilastot_uusi.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
    x.clear()
    y.clear()
    #print(plots)
    for row in plots:
    #print(row[0])
    #print(row[1])
        x.append(int(row[0]))
        y.append(int(row[8]))
        

plt.plot(x,y,label="Iitti Paine, hPa")
plt.xlabel("aika")
plt.ylabel("Paine, hPa")
plt.title("Paine, aika"+str(row[0]))
plt.legend()
plt.show()
