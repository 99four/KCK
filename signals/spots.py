#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

A = genfromtxt('spots.txt')
x = max(A)


w = 12          # częstotliwość próbkowania [Hz]
          # rozważany okres [s]

n = len(A)        # liczba próbek
T = n/w
t = linspace(0, T, n, endpoint=False)

f = lambda t :sin(2*pi*t) + sin(4*pi*t) # def. funkcji
signal = A

subplot(211)
plot(t, signal, '*')
#plot(t, signal1, 'd')
#plot(t, signal2, 'D')
xlabel('czas [s]', fontsize=10)
ylabel('amplituda', fontsize=10,)


signal1 = fft(A) 
signal1 = abs(signal1)        # moduł 

subplot(212)
xlabel('częstotliwość [Hz]', fontsize=10)
ylabel('amplituda', fontsize=10,)
freqs = linspace(0, w, n, endpoint=False)             # <-- ZACZNIJ TUTAJ. Użyj linspace
stem(freqs, signal1, '-*')
signal1[
show()
