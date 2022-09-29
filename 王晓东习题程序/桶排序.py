""" 桶排序
"""

import random
random.seed(2022)
import time
import numpy as np

NUM = 1000000
scale = 0.5


test_list = [random.random() for _ in range(NUM)]

t1 = time.time()
test_list_sorted = sorted(test_list)
t2 = time.time()
# print(test_list_sorted)
print("快速排序法用时：", t2-t1)

t3 = time.time()
min_v = max_v = test_list[0]
for i in range(1, NUM):
    tmp = test_list[i]
    min_v = tmp if tmp < min_v else min_v
    max_v = tmp if tmp > max_v else max_v
# max_v = max(test_list)
# min_v = min(test_list)

BUCKER_NUM = int(NUM * scale)

# bucker_counts = [0 for _ in range(BUCKER_NUM)]
# for num in test_list:
#     idx = int((num-min_v) / (max_v-min_v) * BUCKER_NUM * (1-1e-10))
#     bucker_counts[idx] += 1
# buckers = [([0] * i) for i in bucker_counts] 
# ks = [0 for _ in range(BUCKER_NUM)]
# for num in test_list:
#     idx = int((num-min_v) / (max_v-min_v) * BUCKER_NUM * (1-1e-10))
#     buckers[idx][ks[idx]] = num
#     ks[idx] += 1

buckers = [[] for _ in range(BUCKER_NUM)]
for num in test_list:
    idx = int((num-min_v) / (max_v-min_v) * BUCKER_NUM * (1-1e-10))
    buckers[idx].append(num)
    
sorted_list = []
for bucker in buckers:
    sorted_list.extend(sorted(bucker))

t4 = time.time()
# print(sorted_list)
print("桶排序法用时：", t4-t3)

    

