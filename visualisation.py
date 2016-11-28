#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def mean(numbers):
    return float(sum([float(i) for i in numbers])) / len(numbers)

def main():
    efforts_2cel = []
    efforts_2cel_rs = []
    results_2cel = []
    results_2cel_rs = []

    with open('2cel.csv', 'r') as file_2cel, open('2cel-rs.csv', 'r') as file_2cel_rs:
        lines_2cel = file_2cel.readlines()
        lines_2cel_res = file_2cel_rs.readlines()

    for i in range(1, len(lines_2cel)):
        line_values = lines_2cel[i].split(',')
        efforts_2cel.append(line_values[1])
        # results_2cel.append()
        results_2cel.append(mean(line_values[2:]))

    for i in range(1, len(lines_2cel_res)):
        line_values = lines_2cel_res[i].split(',')
        efforts_2cel_rs.append(line_values[1])
        # results.append()
        results_2cel_rs.append(mean(line_values[2:]))

    plt.figure(figsize=(6, 6))
    #
    plt.plot(efforts_2cel, results_2cel)
    plt.show()
    # plt.savefig('myplot.pdf')
    plt.close()

if __name__ == '__main__':
    main()