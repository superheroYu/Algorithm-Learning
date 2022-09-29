class CombinationNum:
    """ 按顺序从大到小构成的组合数类
    """
    def __init__(self, cbn_list:list, num_range:list):
        """ cbn_list：输入一个顺序组合数（以列表形式给出）；
            num_range：组合数的取值范围列表
            可以对组合数进行加减整数的运算，当超过或小于最小/最大的整数时默认返回最小/最大的组合数
        """
        assert len(cbn_list) < num_range[1] - num_range[0] + 1, "组合数的个数超过了范围"
        self.__ifIncremental(cbn_list) # 判断组合数是否递增排列
        assert cbn_list[0] >= num_range[0] and cbn_list[-1] <= num_range[-1], "组合数必须在输入范围之内"
        self.cbn = cbn_list
        self.range = num_range
        
    def __add__(self, add_num:int): # 加整数的操作
        ls = self.cbn.copy()
        for i in range(add_num): # 依次+1
            self.__add_1(ls)
        return CombinationNum(ls, self.range)
    
    def __sub__(self, sub_num:int): # 减整数的操作
        ls = self.cbn.copy()
        for i in range(sub_num): # 依次-1
            self.__sub_1(ls)
        return CombinationNum(ls, self.range)
    
    def __str__(self): # 打印的格式
        return str(self.cbn)
        
    def __ifIncremental(self, ls): # 判断组合数列表是否递增的方法
        tmp = ls[0]
        for n in ls[1:]:
            assert tmp < n, "组合数列表必须严格递增"
            tmp = n
    
    def __add_1(self, ls): # +1方法
        maxv = self.range[1]
        length = len(ls)
        k = length # 进位位
        for i in range(length-1, -1, -1):
            tmpmax = maxv - length + i + 1 # 每一位的最大值
            tmp = ls[i] + 1
            if tmp <= tmpmax: # 如果没有进位，让该位+1，结束循环
                ls[i] = tmp 
                k = i+1
                break
        for j in range(k,length): # 对于进位后的所有数位每位等于前一位+1
            ls[j] = ls[j-1] + 1
            
    def __sub_1(self, ls): # -1方法
        maxv = self.range[1]
        minv = self.range[0]
        length = len(ls)
        k = length # 退位位
        for i in range(length-1, -1, -1):
            tmp = ls[i] - 1
            if tmp > ls[i-1]: # 如果不用退位，就把当前位减一，结束循环
                ls[i] = tmp 
                k = i + 1
                break
            if i == 0 and ls[i] > minv: # 如果到首位，就将首位减一
                ls[i] -= 1
                k = i + 1
        for j in range(k, length): # 将退位位后每一位，置位成那一位的最大值
             ls[j] = maxv - length + j + 1
             
    def __len__(self):
        return len(self.cbn)

    @staticmethod
    def C(n: int, m: int) -> int:
        """求C_n^m
        """
        a, b = 1, 1
        for i in range(1, m+1):
            a *= n-i+1
            b *= i
        return int(a / b)
    
if __name__ == "__main__":
    C = CombinationNum.C
    cbn = [2, 3, 4, 5]
    cbn_range = [2, 7]
    n = cbn_range[1] - cbn_range[0] + 1
    m = len(cbn)
    test_cbn = CombinationNum(cbn, cbn_range) # 实例化
    for i in range(0, C(n, m)):
        tmp = test_cbn+i
        print(tmp, tmp-i)
    print()


    cbn = [4, 5, 6, 7]
    cbn_range = [2, 7]
    n = cbn_range[1] - cbn_range[0] + 1
    m = len(cbn)
    test_cbn = CombinationNum(cbn, cbn_range) # 实例化
    for i in range(0, C(n, m)):
        tmp = test_cbn-i
        print(tmp, tmp+i)
