#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def main():
    plt.figure(figsize=(3, 3))

    plt.plot([100,200,300,400],[0.1,0.2,0.8,0.9])
    plt.show()
    plt.savefig('myplot.pdf')
    plt.close()

if __name__ == '__main__':
    main()