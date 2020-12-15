from collections import Counter
import numpy as np

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from prettytable import PrettyTable

rhythm1 = []
with open('Ритм 1.txt') as f:
    for line in f:
        rhythm1.append(float(line))

rhythm2 = []
with open('Ритм 2.txt') as f:
    for line in f:
        rhythm2.append(float(line))

f.close()


def CHSS(signal):
    sec = 60000
    return sec / np.mean(signal)


def NN(signal):
    return 1 / CHSS(signal)


def SDNN(signal):
    return np.std(signal)


def Mo(signal):
    return Counter(signal).most_common(1)[0][0]


def AM0(signal):
    return Counter(signal).most_common(1)[0][1] / len(signal) * 100


def MxDMN(signal):
    return (max(signal) - min(signal))


def IH(signal):
    return AM0(signal) / (2 * Mo(signal) * MxDMN(signal))


rhythm1_params = [
    CHSS(rhythm1),
    NN(rhythm1),
    SDNN(rhythm1),
    Mo(rhythm1),
    AM0(rhythm1),
    MxDMN(rhythm1),
    IH(rhythm1),
]

rhythm2_params = [
    CHSS(rhythm2),
    NN(rhythm2),
    SDNN(rhythm2),
    Mo(rhythm2),
    AM0(rhythm2),
    MxDMN(rhythm2),
    IH(rhythm2),
]


# table
def makeTable(attrs):
    table = PrettyTable()

    table.field_names = ["Параметр", "Значення"]
    rows = ["ЧСС, уд/хв", "NN, мс", "SDNN, м", "Mo, мс", "AMo, %", "MxDMn, мс", "ИН"]
    for row, attr in zip(rows, attrs):
        table.add_row([row, "{:.7f}".format(attr)])

    return table


root = tk.Tk()
root.title("Оцінка варіабельності серцевого ритму")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Ритм 1.txt')
tabControl.add(tab2, text='Ритм 2.txt')
tabControl.pack(expand=1, fill="both")


def plot_rhytm(root, rhythm, index):
    fig = Figure(figsize=(12, 2), dpi=100)
    fig.subplots_adjust(hspace=0.5, wspace=0.5)

    p1 = fig.add_subplot(111)
    p1.set_title("Ритмограма №{}".format(index))
    p1.set_xlabel('t, мс')
    p1.set_ylabel('R-R[i], мс')
    p1.plot(rhythm)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def plot_scatter_and_hist(root, rhythm, index):
    fig = Figure(figsize=(8, 4), dpi=100)
    fig.subplots_adjust(hspace=0.5, wspace=0.5)

    p2 = fig.add_subplot(121)
    p2.set_title("Скатерограма №{}".format(index))
    p2.set_xlabel('R-R[i+1], мс')
    p2.set_ylabel('R-R[i], мс')
    p2.scatter(rhythm[1:len(rhythm)], rhythm[0:len(rhythm) - 1])

    p3 = fig.add_subplot(122)
    p3.set_title("Гістограма №{}".format(index))
    p3.set_xlabel('R-R[i], мс')
    p3.set_ylabel('К-во R-R')
    p3.hist(rhythm, alpha=1, bins=int(max(rhythm)/50))

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


# tab 1 content
panel1 = tk.PanedWindow(tab1)
panel1.configure(bg="white")
panel1.pack(fill=tk.BOTH, expand=1)

plot_rhytm(panel1, rhythm1, 1)
plot_scatter_and_hist(panel1, rhythm1, 1)

table1 = makeTable(rhythm1_params)
tk.Label(panel1, text=str(table1), font="Consolas 10", bg="white").pack(side=tk.LEFT, padx=5, pady=5)

# tab 2 content
panel2 = tk.PanedWindow(tab2)
panel2.configure(bg="white")
panel2.pack(fill=tk.BOTH, expand=1)

plot_rhytm(panel2, rhythm2, 2)
plot_scatter_and_hist(panel2, rhythm2, 2)

table2 = makeTable(rhythm2_params)
tk.Label(panel2, text=str(table2), font="Consolas 10", bg="white").pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
