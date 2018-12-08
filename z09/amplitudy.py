import numpy as np
import matplotlib.pyplot as plt

#amplitudy
#https://matplotlib.org/users/text_intro.html
#https://stackoverflow.com/questions/11143619/add-graph-description-under-graph-in-pylab
#strona tytułowa - sprawdzić wzór
#nazwy zgodne w legendzie odpalić mail i przekopiować
#przesunięcie fazowe z odpowiednim znakiem pi


plt.plot()
plt.figtext(.50,.01, 'Rys.1. Amplituda to największe wychylenie funkcji. Jest to liczba bezwględna  z wartości punktu o największym wychyleniu na osi y, licząc od 0. ', fontsize=10, ha='center')




f = 1
A = 1
A2 = 4
A3 = 10
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)
plt.plot(t, sygnal, label='A = 1')
sygnal2 = A2*np.sin(2*np.pi*f*t)
plt.plot(t, sygnal2, label='A = 4')
sygnal3 = A3*np.sin(2*np.pi*f*t)
plt.plot(t, sygnal3, label='A = 10')

plt.legend(loc='upper right')
plt.ylabel('wartość amplitudy [-]')
plt.xlabel('czas [s]')
plt.show()
