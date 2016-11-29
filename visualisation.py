import matplotlib.pyplot as plt

def load_data(lines_type, eff, res):
    for i in range(1, len(lines_type)):
        line_values = lines_type[i].split(',')
        eff.append(line_values[1])
        res.append(sum([float(i) for i in line_values[2:]]) / len(line_values[2:]))

def main():
    efforts = [[], [], [], [], []]
    results_types = [[], [], [], [], []]

    for i, file_name in enumerate(['rsel.csv', 'cel-rs.csv','2cel-rs.csv', 'cel.csv', '2cel.csv']):
        with open(file_name, 'r') as file:
            load_data(file.readlines(), efforts[i], results_types[i])

    plt.figure(figsize=(6, 6))
    plt_params = [
        ['b', '1-Evol-RS'],
        ['g', '1-Coev-RS'],
        ['r', '2-Coev-RS'],
        ['k', '1-Coev'],
        ['m', '2-Coev']
    ]
    for i, param in enumerate(plt_params):
        plt.plot(efforts[i], results_types[i], color=param[0], label=param[1])

    plt.legend(loc=4)
    plt.xlim(xmax=500000)
    plt.xlabel('Rozegranych gier')
    plt.ylabel('Odsetek wygranych gier')
    plt.savefig('myplot.pdf')
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()