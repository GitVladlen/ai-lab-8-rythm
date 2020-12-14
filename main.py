from collections import Counter
import statistics

rhythm1 = []
with open('Ритм 1.txt') as f:
    for line in f:
        rhythm1.append(float(line))

rhythm2 = []
with open('Ритм 2.txt') as f:
    for line in f:
        rhythm2.append(float(line))

f.close()
i = 0
tt = 0
t1 = []
while i < len(rhythm1):
    t1.append(tt)
    tt += 0.05
    i += 1
i = 0
tt = 0
t2 = []
while i < len(rhythm2):
    t2.append(tt)
    tt += 0.05
    i += 1

i = min(rhythm1) - 50
x1 = []
y1 = []
while i < max(rhythm1):
    x1.append(i)
    y1.append(i)
    i += 1

i = min(rhythm2) - 50
x2 = []
y2 = []
while i < max(rhythm2):
    x2.append(i)
    y2.append(i)
    i += 1

attr12 = sum(rhythm1) / len(rhythm1)
attr11 = 60000 / attr12
attr13 = statistics.stdev(rhythm1)
b = Counter(rhythm1)
attr14 = b.most_common(1)
attr15 = attr14[0][1] / len(rhythm1)
attr16 = max(rhythm1) - min(rhythm1)
a1 = attr15 / 60000
a2 = attr14[0][0] / 60000
a3 = attr16 / 60000
attr17 = a1 / (2 * a2 * a3)
attr22 = sum(rhythm2) / len(rhythm2)
attr21 = 60000 / attr22
attr23 = statistics.stdev(rhythm2)
b = Counter(rhythm2)
attr24 = b.most_common(1)
attr25 = attr24[0][1] / len(rhythm2)
attr26 = max(rhythm2) - min(rhythm2)
a1 = attr25 / 60000;
a2 = attr24[0][0] / 60000
a3 = attr26 / 60000
attr27 = a1 / (2 * a2 * a3)

# table
from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["Param", "Value"]
x.add_row(["ЧСС, уд/хв", attr11])
x.add_row(["NN, мс", attr12])
x.add_row(["SDNN, м", attr13])
x.add_row(["Mo, мс", attr14])
x.add_row(["AMo, %", attr15])
x.add_row(["MxDMn, мс", attr16])
x.add_row(["ИН", attr17])

print('Ритмограмма №1')
print(x)

print(['ЧСС, уд/хв', attr11])
print(['NN, мс', attr12])
print(['SDNN, мс', attr13])
print(['Mo, мс', attr14])
print(['AMo, %', attr15])
print(['MxDMn, мс', attr16])
print(['ИН', attr17], '\n')

print('Ритмограмма №2')
print(['ЧСС, уд/хв', attr21])
print(['NN, мс', attr22])
print(['SDNN, мс', attr23])
print(['Mo, мс', attr24])
print(['AMo, %', attr25])
print(['MxDMn, мс', attr26])
print(['ИН', attr27])


#
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])

print(x)


import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


root = tk.Tk()
root.title("Оцінка варіабельності серцевого ритму")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Ритм 1.txt')
tabControl.add(tab2, text ='Ритм 2.txt')
tabControl.pack(expand = 1, fill ="both")


def myplot(root, t, rhythm):
    fig = Figure(figsize=(5, 4), dpi=100)

    fig.subplots_adjust(hspace=0.5, wspace=0.5)

    p1 = fig.add_subplot(211)
    p1.set_title('Ритмограмма №1')
    p1.set_xlabel('t, мс')
    p1.set_ylabel('RRi, мс')
    p1.plot(t, rhythm)

    p2 = fig.add_subplot(223)
    p2.set_title('Скаттерограмма №1')
    p2.set_xlabel('RRi+1, мс')
    p2.set_ylabel('RRi, мс')
    p2.scatter(rhythm[1:len(rhythm)], rhythm[0:len(rhythm) - 1])

    p3 = fig.add_subplot(224)
    p3.set_title('Гистограмма №1')
    p3.set_xlabel('RRi, мс')
    p3.set_ylabel('К-во RR')
    p3.hist(rhythm, alpha=1)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


myplot(tab1, t1, rhythm1)
myplot(tab2, t2, rhythm2)

root.mainloop()
