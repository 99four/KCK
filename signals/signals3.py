from __future__ import division

from pylab import *
from scipy import *
from numpy import angle


def main():
    T = 1
    w = 20
    n = T * w
    t = linspace(0, T, n, endpoint=False)

    # ********************************************************************************************************

    f = lambda tt: sin(2 * pi * tt) + sin(4 * pi * tt)
    signal = f(t)

    subplot(231)
    title("sin(2 * pi * tt) + sin(4 * pi * tt)")
    plot(t, signal, '*')

    subplot(232)
    title("Dziedzina czestotliwosci")
    freqs = linspace(0, w, n, endpoint=False)
    signal1 = fft(signal)
    z = angle(signal1)
    signal1 = (2 * abs(signal1)) / n
    stem(freqs, signal1, '-*')

    subplot(233)
    title("Faza")
    stem(freqs, z, '-*')

    # show()

    # ********************************************************************************************************

    f = lambda tt: sin(2 * pi * tt) + cos(4 * pi * tt)
    signal = f(t)

    subplot(234)
    title("sin(2 * pi * tt) + cos(4 * pi * tt)")
    plot(t, signal, '*')

    subplot(235)
    title("Dziedzina czestotliwosci")
    freqs = linspace(0, w, n, endpoint=False)
    signal1 = fft(signal)
    z = angle(signal1)
    signal1 = (2 * abs(signal1)) / n
    stem(freqs, signal1, '-*')

    subplot(236)
    title("Faza")
    stem(freqs, z, '-*')

    show()


if __name__ == "__main__":
    main()
