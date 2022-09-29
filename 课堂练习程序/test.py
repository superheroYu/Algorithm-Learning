from dataclasses import replace


a = [1, 2, 3, 6, 2, 1]
b = a[3:]
b[0] = 1
print(a)