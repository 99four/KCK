#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def mean(numbers):
    return float(sum([float(i) for i in numbers])) / len(numbers)

def load_data(lines_type, efforts_type, results_type):
    for i in range(1, len(lines_type)):
        line_values = lines_type[i].split(',')
        efforts_type.append(line_values[1])
        results_type.append(mean(line_values[2:]))

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

    load_data(lines_2cel, efforts_2cel, results_2cel)
    load_data(lines_2cel_res, efforts_2cel_rs, results_2cel_rs)
    load_data(lines_cel, efforts_cel, results_cel)
    load_data(lines_cel_rs, efforts_cel_rs, results_cel_rs)
    load_data(lines_rsel, efforts_rsel, results_rsel)

    plot_parameters = [
        [efforts_rsel, results_rsel, 'b', '1-Evol-RS'],
        [efforts_cel_rs, results_cel_rs, 'g', '1-Coev-RS'],
        [efforts_2cel_rs, results_2cel_rs, 'r', '2-Coev-RS'],
        [efforts_cel, results_cel, 'k', '1-Coev'],
        [efforts_2cel, results_2cel, 'm', '2-Coev']
    ]

    plt.figure(figsize=(8, 8))
    #
    for efforts, results, color, label in plot_parameters:
        plt.plot(efforts, results, color=color, label=label)
    plt.legend(loc=4)
    plt.xlim(xmax=500000)
    plt.xlabel('Rozegranych gier')
    plt.ylabel('Odsetek wygranych gier')
    plt.savefig('myplot.pdf')
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()