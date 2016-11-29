#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def mean(numbers):
    return float(sum([float(i) for i in numbers])) / len(numbers)

def load_data(lines_type, eff, res):
    for i in range(1, len(lines_type)):
        line_values = lines_type[i].split(',')
        eff.append(line_values[1])
        res.append(mean(line_values[2:]))

def main():
    efforts = [[], [], [], [], []]
    results_types = [[], [], [], [], []]

    i = 0
    for file_name in ['rsel.csv', 'cel-rs.csv','2cel-rs.csv', 'cel.csv', '2cel.csv']:
        with open(file_name, 'r') as file:
            load_data(file.readlines(), efforts[i], results_types[i])
            i += 1

    plot_parameters = [
        ['b', '1-Evol-RS'],
        ['g', '1-Coev-RS'],
        ['r', '2-Coev-RS'],
        ['k', '1-Coev'],
        ['m', '2-Coev']
    ]
    plt.figure(figsize=(8, 8))

    i = 0
    for color, label in plot_parameters:
        plt.plot(efforts[i], results_types[i], color=color, label=label)
        i += 1

    plt.legend(loc=4)
    plt.xlim(xmax=500000)
    plt.xlabel('Rozegranych gier')
    plt.ylabel('Odsetek wygranych gier')
    plt.savefig('myplot.pdf')
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()