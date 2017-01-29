#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

w = 100           # częstotliwość próbkowania [Hz]
T = 1            # rozważany okres [s]

n = T * w        # liczba próbek
t = linspace(0, T, n, endpoint=False) # punkty na osi OX [s]

fb = lambda t : sin(2*pi*t) + 2 * sin(4*pi*t)
fc = lambda t : sin(4*2*pi*t) + 0.5*random.random(n)
fd = lambda t : 2.3 + sin(2*pi*t)
fe = lambda t : sin(2*pi*t + pi/4)
f = lambda t : sin(2*pi*t)    # def. funkcji
f1 = lambda t : 2*sin(2*pi*t)    # def. funkcji
f2 = lambda t : 3*sin(2*pi*t)    # def. funkcji
signal = f(t)                 # funkcja spróbkowana

subplot(211)
xlabel('czas [s]', fontsize=10)
ylabel('amplituda', fontsize=10)
plot(t, signal, '*')

signal1 = fft(signal)
signal2 = ifft(fft(2*signal/n))
signal1 = abs(signal1)        # moduł

subplot(212)
freqs = range(n)              # <-- ZACZNIJ TUTAJ. Użyj linspace
freqs = linspace(0, w, n, endpoint=False)
xlabel('czestotliwosc [Hz]', fontsize=10)
ylabel('amplituda', fontsize=10)
stem(freqs, signal2, '-*')

show()
