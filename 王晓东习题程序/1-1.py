'''
    输入总页数，获得所有页数的0-9数量
'''

def f(n): return n*(10**(n-1))  # 计算所有n位组成页码每个数字的个数


def cal_zeroCount(n: int) -> int:
    # 计算多余的0数量
    zeroCount = 0
    zeroCount += n-1  # 第一排
    for i in range(1, n):
        zeroCount += (n-i) * 9 * (10**(i-1))
    return zeroCount


def re_num(ls: list) -> int:
    # 解码整数，如将[4, 3, 5]解码为整数534
    real_num = 0
    for digit, num in enumerate(ls):
        real_num += num * (10 ** digit)
    return real_num


def dis_num(num: int) -> list:
    # 分解整数，如将534分解为列表[4, 3, 5]
    maxdigit = 0
    dis_num = []
    while True:
        maxdigit += 1
        if (num - (10**maxdigit) < 0):
            break
    for digit in range(maxdigit-1, -1, -1):
        quetient, num = divmod(num, 10**digit)
        dis_num.append(quetient)
    return dis_num[::-1]


def cal_numCount(d_num: list, numCountList: list) -> None:
    # 计算所有页码0-9的数量
    digit_count = len(d_num)  # 获取需要计算数的总位数
    for digit, num in enumerate(d_num):
        if digit == 0:  # 处理个位
            for n in range(num+1):
                numCountList[n] += 1
            continue
        # 处理其他位
        tmp = f(digit)  # 计算当前数位对应的f
        for n in range(num):  # 对0到num-1进行循环
            for i in range(10):  # 首先将0-9每个数量增加f(digit)
                numCountList[i] += tmp
            if n > 0:  # 如果n在1到num-1之间，就把n的数量加上10^(digit)
                numCountList[n] += 10**digit
        if (num != 0) and (digit != digit_count - 1):  # 若当前位数的值不是0，且当前位数不是首位，就把0的数量加上10^(digit)
            numCountList[0] += 10**(digit)
        numCountList[num] += re_num(d_num[:digit]) + 1  # 补增当前位的个数

    if digit_count > 1:
        numCountList[0] -= cal_zeroCount(digit_count-1)  # 除去多余的0


if __name__ == '__main__':
    import time
    NUM = int(input("请输入总页数n："))

    t1 = time.time()
    A = ["{}".format(k) for k in range(NUM+1)]
    count = [0] * 10
    for s in A:
        for j in s:
            count[int(j)] += 1
    t2 = time.time()
    print("使用循环计算得到正确解：0有{}个，1有{}个，2有{}个，3有{}个，4有{}个，5有{}个，6有{}个，7有{}个，8有{}个，9有{}个".format(*count))
    print("耗时：%.6f" % (t2-t1))

    t3 = time.time()
    numCountList = [0] * 10
    cal_numCount(dis_num(NUM), numCountList)
    numCountList = list(map(lambda x: int(x), numCountList))
    t4 = time.time()
    print("使用本算法计算得到正确解：0有{}个，1有{}个，2有{}个，3有{}个，4有{}个，5有{}个，6有{}个，7有{}个，8有{}个，9有{}个".format(
        *numCountList))
    print("耗时：%.6f" % (t4-t3))
