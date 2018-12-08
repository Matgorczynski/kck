import numpy as np
import matplotlib.pyplot as plt

#różne próbkowanie

plt.plot()
plt.figtext(.50,.01, 'Rys.4. Częstotliwość próbkowania to liczba pobrań wartości funkcji w ciągu określonego czasu.', fontsize=10, ha='center')


f = 5
t = np.linspace(0, 1, 256)
sygnal = np.sin(2*np.pi*f*t)
plt.plot(t, sygnal, label='fs = 256')

t = np.linspace(0, 1, 40)
sygnal = np.sin(2*np.pi*f*t)
plt.plot(t, sygnal, label='fs = 40')

t = np.linspace(0, 1, 10)
sygnal = np.sin(2*np.pi*f*t)
plt.plot(t, sygnal, label='fs = 10')

plt.ylabel('wartość amplitudy [-]')
plt.xlabel('czas [s]')

plt.legend(loc='upper right')



plt.show()
