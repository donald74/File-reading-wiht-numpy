#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:57:09 2021

@author: RUTH
"""
#import der library numpy mit bevor nutzung
import numpy as np

#Erste array um die ganze csv datei zu speichern
data = []

#Zwei array um Sensor-A und Sensor-B zu speichern
baroA = []
baroB = []

#lesung der Datei mit numpy function genfromtxt
csv_file = np.genfromtxt('Barometermesswerte.csv', delimiter=',', dtype = None, encoding = None)

#benutzung der for Schleife um die Datei von Sensor-A un B zu speichern
#in array data[]
for row in csv_file:
    data.append(row)
    


#index für dieh while Schleife
i = 0
j = 0

#Sortieren der Daten, um sie in das entsprechende Array zu legen
while(i< len(data)):
    j = 0
    if data[i][j] == 'Sensor-A':
       baroA.append(data[i][j+1])
       i +=1
       j +=1
    else:
        baroB.append(data[i][j+1])
        i +=1
        
#Sie haben Zugriff auf dem Array entsprechenden Wert 
#mit dem Namen des Arrays und der Nummer des Index
#hier print array nur nummer 0, baroA[1] für die zweite Datei 
print("baroA value", baroA[0])
print("baroB value",baroB[0])

    
