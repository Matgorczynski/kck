import numpy as np
import matplotlib.pyplot as plt

#czestotliwosci

plt.plot()
plt.figtext(.50,.01, 'Rys.2. Częstotliwość to liczba cykli, czyli pełnych amplitud lub drgań, w określonym czasie.', fontsize=10, ha='center')

f = 1
f2 = 5
f3 = 10
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)
plt.plot(t, sygnal, label='ν = 1 Hz')
sygnal2 = A*np.sin(2*np.pi*f2*t)
plt.plot(t, sygnal2, label='ν = 5 Hz')
sygnal3 = A*np.sin(2*np.pi*f3*t)
plt.plot(t, sygnal3, label='ν = 10 Hz')

plt.legend(loc='upper right')
plt.ylabel('wartość amplitudy [-]')
plt.xlabel('czas [s]')
plt.show()
