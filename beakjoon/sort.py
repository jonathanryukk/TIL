# 삽입정렬 #

import random

a = random.sample(range(1,10),5)

print(a)  

print('')

for i in range(1,len(a)):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
print(a)