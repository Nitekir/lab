import random

print('Задание 1')
a = [random.randint(2, 103) for _ in range(10)]
print("До:   ", a)

for i in range(len(a) - 1):
    m = i
    for j in range(i + 1, len(a)):
        if a[j] < a[m]:
            m = j
    a[i], a[m] = a[m], a[i]

print("После:", a)

print('Задание 2')

b = [random.randint(0, 100) for _ in range(10)]
print("До:   ", b)

for i in range(len(b) - 1):
    m = i
    for j in range(i + 1, len(b)):
        if b[j] > b[m]:
            m = j
    b[i], b[m] = b[m], b[i]

print("После:", b)

print('Задание 3')

phones = ["23-45-67", "12-34-56", "89-01-23", "12-30-99", "05-55-55"]
print("До:   ", phones)

for i in range(len(phones) - 1):
    m = i
    for j in range(i + 1, len(phones)):
        if phones[j] < phones[m]:
            m = j
    phones[i], phones[m] = phones[m], phones[i]

print("После:", phones)
