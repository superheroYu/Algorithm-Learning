def insertion_sort(A:list)->None:
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0:
            if A[j] <= key: break
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        

import random
list1 = list(range(1, 10))
random.shuffle(list1)
print(list1)
insertion_sort(list1)
print(list1)