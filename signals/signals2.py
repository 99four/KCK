#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

w = 50           # czÄ™stotliwoÅ›Ä‡ prÃ³bkowania [Hz]
T = 1           # rozwaÅ¼any okres [s]
spektrum=[]
n = T * w        # liczba prÃ³bek
t = linspace(0, T, n, endpoint=False) # punkty na osi OX [s]
f = lambda t : sin(2*pi*t)    # def. funkcji
signal = f(t)                 # funkcja sprÃ³bkowana
plt.figure("slonce")
array = genfromtxt('spots.txt')
t=linspace(0,len(array),len(array))
print(array)
subplot(211)

plot(t, array)
print(n)
#for i in range(1,4):
#	signal_temp=signal*i
#	signal1 = fft(signal_temp)
#	signal1 = abs(signal1)        # moduÅ‚
#	spektrum.append(signal1)

plt.xlabel('n')
plt.ylabel('aktywnosc')
subplot(212)
freqs = len(array)


#freqs=np.linspace(0,w,signal1.size)            # <-- ZACZNIJ TUTAJ. UÅ¼yj linspace
#for x in range(0,3):
#	stem(freqs, spektrum[x], '-*')
#fs=(i*w)/N
N=len(spektrum)
w=12
spektrum=abs(fft(array))
N=len(spektrum)
w=12
#freq = [v * samplingFrequency / len(dataFinal[0]) for v in ind]
freqs1=np.linspace(0,w,len(spektrum))
#freqs1=12*freqs1
#stem(freqs,spektrum)
plt.hold(True)
stem(freqs1,spektrum,'r')
spektrum[0]=0
maxf=freqs1[argmax(spektrum)]
maxf1=(argmax(spektrum)*w)/len(spektrum)

print("czestotliwosc czytana  ",maxf)
print("czesttotliwosc liczona ",maxf1)


plt.xlabel('freqs')
plt.ylabel('spektrum')
show()
#plt.pause(3)
#input()
#close()
figure("sinusy z usunienta 2hz")
T=1
w=20
n = T * w        # liczba prÃ³bek
t = linspace(0, T, n, endpoint=False) # punkty na osi OX [s]
f = lambda t : sin(2*pi*t)+sin(4*pi*t)
f1=lambda t : sin(2*pi*t)
f2=lambda t : sin(4*pi*t)
subplot(311)
plt.hold(True)
signal=f(t)
signal1=f1(t)
signal2=f2(t)
legend(['f', 'f1', 'f2'])
plot(t,signal)
plot(t,signal1)
plot(t,signal2)
subplot(312)
signal1 = fft(signal)
signal1 = abs(signal1)

signal1[1]=0
signal1[19]=0
#signal1[18]=0
print(np.around(signal1))
f2=ifft(np.around(signal1) )
plot(t,f2)
subplot(313)
freqs=np.linspace(0,w,signal1.size)
stem(freqs,signal1)
show()
