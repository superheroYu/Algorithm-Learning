'''
    字典序问题，求出字典序对应的编码
'''


def C(n: int, m: int) -> int:
    """求C_n^m
    """
    a, b = 1, 1
    for i in range(1, m+1):
        a *= n-i+1
        b *= i
    return int(a / b)


def N(s: str, i: int) -> sum:
    """ 计算字符长度为n时，字符串的编号增量
         s:字符串，i为确定首字母时要排除的字母个数
    """
    sum = 0
    n = len(s)
    if n < 1:
        return 0
    high = ord(s[0])
    for k in range(1, high-ord('a')-i+1):  # 按字母顺序遍历字符串第一位到a+(i)位
        sum += C(26-k-i, n-1)  # 计算这些字母带来的编号增量
    if n > 1:
        sum += N(s[1:], high-ord('a')+1)  # 递归计算s[1:]带来的编号增量
    return sum


if __name__ == '__main__':
    with open("./data/input1_2.txt", 'r') as f:
        slist = f.readlines()
    with open("./data/output1_2.txt", "a") as f:
        for s in slist:
            s = s.strip().replace("\n", "")
            sum = 0
            n = len(s)
            for j in range(n):  # 计算长度小于n的字典序的最大编号
                sum += C(26, j)
            result = sum + N(s, 0)
            print(s)
            print(result)

            f.write("%d\n" % result)
    # s = "abcd"
    # sum = 0
    # n = len(s)
    # for j in range(1, n): #计算长度小于n的字典序的最大编号
    #     sum += C(26, j)
    # result = sum + N(s, 0) + 1
    # print(result)
