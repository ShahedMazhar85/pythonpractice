import itertools

for i in itertools.count(10, 10):
    if i > 50:
        break
    else:
        print(i, end=" ")

import itertools
temp = 0
for i in itertools.cycle("12345"):
    if temp >= 10:
        break
    else:
        print(i, end=' ')
        temp = temp + 1
