from collections import Counter
import statistics
import matplotlib.pyplot as plt

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
a1 = attr15 / 60000;
a2 = attr14[0][0] / 60000;
a3 = attr16 / 60000;
attr17 = a1 / (2 * a2 * a3)
attr22 = sum(rhythm2) / len(rhythm2)
attr21 = 60000 / attr22
attr23 = statistics.stdev(rhythm2)
b = Counter(rhythm2)
attr24 = b.most_common(1)
attr25 = attr24[0][1] / len(rhythm2)
attr26 = max(rhythm2) - min(rhythm2)
a1 = attr25 / 60000;
a2 = attr24[0][0] / 60000;
a3 = attr26 / 60000;
attr27 = a1 / (2 * a2 * a3)

plt.figure(1, figsize=(16, 4))
plt.subplot(2, 1, 1)
plt.title('Ритмограмма №1')
plt.xlabel('t, мс')
plt.ylabel('RRi, мс')
plt.plot(t1, rhythm1), plt.grid

plt.subplot(2, 1, 2)
plt.title('Ритмограмма №2')
plt.xlabel('t, мс')
plt.ylabel('RRi, мс')
plt.plot(t2, rhythm2, 'r'), plt.grid

plt.figure(2, figsize=(16, 10))
plt.subplot(2, 2, 1)
plt.title('Скаттерограмма №1')
plt.xlabel('RRi+1, мс')
plt.ylabel('RRi, мс')
plt.scatter(rhythm1[1:len(rhythm1)], rhythm1[0:len(rhythm1) - 1])
plt.subplot(2, 2, 2)
plt.title('Скаттерограмма №2')
plt.xlabel('RRi+1, мс')
plt.ylabel('RRi, мс')
plt.scatter(rhythm2[1:len(rhythm2)], rhythm2[0:len(rhythm2) - 1])
plt.subplot(2, 2, 3)
plt.title('Гистограмма №1')
plt.xlabel('RRi, мс')
plt.ylabel('К-во RR')
plt.hist(rhythm1, alpha=1)
plt.subplot(2, 2, 4)
plt.title('Гистограмма №2')
plt.xlabel('RRi, мс')
plt.ylabel('К-во RR')
plt.hist(rhythm2)
plt.show()

print('Ритмограмма №1')
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
