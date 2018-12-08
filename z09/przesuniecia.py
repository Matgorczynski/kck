import numpy as np
import matplotlib.pyplot as plt

#przesunięcia fazowe

plt.plot()
plt.figtext(.50,.01, 'Rys.3. Przesunięcie fazowe to różnica faz drgania dwóch funkcji.', fontsize=10, ha='center')
f = 3
A = 1
t = np.linspace(0, 1, 256)

sygnal = A*np.sin(2*np.pi*f*t+np.pi/9)
plt.plot(t, sygnal, label=r'$\varphi$ = $\pi $/9 = 20°')

sygnal2 = A*np.sin(2*np.pi*f*t+np.pi/4)
plt.plot(t, sygnal2, label = r'$\varphi$ = $\pi $/4 = 45°')


sygnal3 = A*np.sin(2*np.pi*f*t+np.pi/2)
plt.plot(t,sygnal3, label = r'$\varphi$ = $\pi $/2 = 90°')

plt.legend(loc='upper right')
plt.ylabel('wartość amplitudy [-]')
plt.xlabel('czas [s]')

plt.show()
