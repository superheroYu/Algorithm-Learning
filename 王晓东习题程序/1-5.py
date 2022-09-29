""" 最大间隙问题
"""

import time
import random
random.seed(2022)

if __name__ == "__main__":

    NUM = 1000
    test_list = [random.random() for _ in range(NUM)]  # 测试采用的list

    # 方案一：先排序再求最大间隙
    t1 = time.time()
    test_list_sorted = sorted(test_list)  # 采用快速排序对list进行排序
    # print(test_list_sorted)
    MAX = 0
    # 遍历求出最大间隙
    for i in range(NUM-1):
        tmp = test_list_sorted[i+1] - test_list_sorted[i]
        MAX = tmp if MAX < tmp else MAX
    t2 = time.time()
    print("最大间隙是：", MAX)
    print("排序法用时：", t2-t1)

    # 方案二：用桶排序的思想求最大间隙
    t3 = time.time()
    # step1：求出数组中最大值和最小值
    min_v = max_v = test_list[0]
    for i in range(1, NUM):
        tmp = test_list[i]
        min_v = tmp if tmp < min_v else min_v
        max_v = tmp if tmp > max_v else max_v

    # step2：初始化桶
    BUCKER_NUM = NUM + 1  # 桶的数量
    INF = 10**100  # 用一个超大的数表示桶是空的
    low_ls = [INF for _ in range(BUCKER_NUM)]
    high_ls = [-INF for _ in range(BUCKER_NUM)]

    # step3：将数字放入桶中，用low和high记录每桶中最小值和最大值
    for num in test_list:
        idx = int((num-min_v) / (max_v - min_v) * (BUCKER_NUM-1)) # 计算桶的编号
        if num < low_ls[idx]:
            low_ls[idx] = num
        if num > high_ls[idx]:
            high_ls[idx] = num

    MAX = 0
    # step4：遍历
    left = high_ls[0]
    for i in range(1, BUCKER_NUM):
        if low_ls[i] == INF: # 判断桶是否为空
            continue  
        right = low_ls[i]
        MAX = right - left if right - left > MAX else MAX
        left = high_ls[i]

    t4 = time.time()
    print("最大间隙是：", MAX)
    print("桶排序法用时：", t4-t3)
