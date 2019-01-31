import aseegg as ag
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

data = pd.read_csv('sub1trial8.csv', delimiter=',', engine='python')
data.columns = ['-','kanal1', 'kanal2', 'kanal3', 'kanal4','cyfra' ]
fs=200
dlugosc = data['-']
kanal1=data['kanal1']
#print(kanal1)
t = 7589/fs
t = int(t)
x =np.linspace(0,t,t*fs)
filtrowaniezaporowe = ag.pasmowozaporowy(kanal1, fs, 49, 51)
filtrowanieprzepustowe = ag.pasmowoprzepustowy(filtrowaniezaporowe, fs, 1, 50)
#oprócz starej pętli mógłbym spróbować zrobić coś z tej, która printuje czas, w którym osoba mrugnęła i dopasować go do cyfry, jednak nie mam czasu z związku z sesją
#licznik=0
#z = 0
#czasmrugania = []
#for i in filtrowanieprzepustowe:
#    if i>=0.10 and z<0.10:
    #    czasmrugania.append([licznik/200])

#    z=i
#    licznik+=1
#print(czasmrugania)
licznik=0
z = 0
mrugane = []
for i in filtrowanieprzepustowe:
    if i>=0.10 and z<0.10:
        mrugane.append(data['cyfra'][licznik])
    z=i
    licznik+=1
print(mrugane)
plt.plot(x,filtrowanieprzepustowe[0:t*fs], label ='sygnał')
plt.ylabel('mikrowolty [mV]')
plt.xlabel('czas [s]')
plt.legend(loc='upper right')
plt.show()
plt.plot(x,kanal1[0:t*fs],label ='sygnał')
plt.ylabel('mikrowolty [mV]')
plt.xlabel('czas [s]')
plt.legend(loc='upper right')
plt.show()
