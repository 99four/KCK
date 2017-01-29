#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

w = 50
T = 1
spektrum=[]
n = T * w
t = linspace(0, T, n, endpoint=False)
f = lambda t : sin(2*pi*t)
signal = f(t)
plt.figure("slonce")
array = genfromtxt('spots.txt')
t=linspace(0,len(array),len(array))
print(array)
subplot(211)

plot(t, array)
print(n)
plt.xlabel('n')
plt.ylabel('aktywnosc')
subplot(212)
freqs = len(array)


N=len(spektrum)
w=12
spektrum=abs(fft(array))
N=len(spektrum)
w=12
freqs1=np.linspace(0,w,len(spektrum))
plt.hold(True)
stem(freqs1,spektrum,'r')
spektrum[0]=0
maxf=freqs1[argmax(spektrum)]

print("czestotliwosc ",maxf)

plt.xlabel('freqs')
plt.ylabel('spektrum')
show()
figure("sinusy z usunienta 2hz")
T=1
w=20
n = T * w
t = linspace(0, T, n, endpoint=False)
f = lambda t : sin(2*pi*t)+sin(4*pi*t)
f1=lambda t : sin(2*pi*t)
subplot(311)
plt.hold(True)
signal=f(t)
legend(['f', 'f1', 'f2'])
plot(t,signal)
subplot(312)
signal1 = fft(signal)
signal1 = signal1

signal1[2]=0
signal1[18]=0
print(np.around(signal1))
f2=ifft(np.around(signal1) )
plot(t,f2)
subplot(313)
freqs=np.linspace(0,w,signal1.size)
stem(freqs,signal1)
show()
