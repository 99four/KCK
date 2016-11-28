#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def mean(numbers):
    return float(sum([float(i) for i in numbers])) / len(numbers)

def main():
    efforts_2cel = []
    efforts_2cel_rs = []
    efforts_cel = []
    efforts_cel_rs = []
    efforts_rsel = []

    results_2cel = []
    results_2cel_rs = []
    results_cel = []
    results_cel_rs = []
    results_rsel = []

    with open('2cel.csv', 'r') as file_2cel, \
            open('2cel-rs.csv', 'r') as file_2cel_rs, \
            open('cel.csv', 'r') as file_cel, \
            open('cel-rs.csv', 'r') as file_cel_rs, \
            open('rsel.csv', 'r') as file_rsel:
        lines_2cel = file_2cel.readlines()
        lines_2cel_res = file_2cel_rs.readlines()
        lines_cel = file_cel.readlines()
        lines_cel_rs = file_cel_rs.readlines()
        lines_rsel = file_rsel.readlines()

    for i in range(1, len(lines_2cel)):
        line_values = lines_2cel[i].split(',')
        efforts_2cel.append(line_values[1])
        results_2cel.append(mean(line_values[2:]))

    for i in range(1, len(lines_2cel_res)):
        line_values = lines_2cel_res[i].split(',')
        efforts_2cel_rs.append(line_values[1])
        results_2cel_rs.append(mean(line_values[2:]))

    for i in range(1, len(lines_cel)):
        line_values = lines_cel[i].split(',')
        efforts_cel.append(line_values[1])
        results_cel.append(mean(line_values[2:]))

    for i in range(1, len(lines_cel_rs)):
        line_values = lines_cel_rs[i].split(',')
        efforts_cel_rs.append(line_values[1])
        results_cel_rs.append(mean(line_values[2:]))

    for i in range(1, len(lines_rsel)):
        line_values = lines_rsel[i].split(',')
        efforts_rsel.append(line_values[1])
        results_rsel.append(mean(line_values[2:]))


    plot_parameters = [
        [efforts_2cel, results_2cel, 'm'],
        [efforts_2cel_rs, results_2cel_rs, 'r'],
        [efforts_cel, results_cel, 'k'],
        [efforts_cel_rs, results_cel_rs, 'g'],
        [efforts_rsel, results_rsel, 'b']
    ]

    plt.figure(figsize=(6, 6))
    #
    for efforts, results, color in plot_parameters:
        plt.plot(efforts, results, color = color)
    plt.show()
    # plt.savefig('myplot.pdf')
    plt.close()

if __name__ == '__main__':
    main()