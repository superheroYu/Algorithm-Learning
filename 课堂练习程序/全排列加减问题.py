class PermutationNum:
    """ 全排列数类
    """
    def __init__(self, pmn_list:list):
        """ pmn_list：输入一个全排列数（以列表形式给出）；
            可以对全排列数进行加减整数的运算，超过范围后默认返回最小/最大的排列数对象
        """
        self.__ifDuplicate(pmn_list) # 判断组合数是否递增排列
        self.pmn = pmn_list
        
    def __add__(self, add_num:int): # 加整数的操作
        ls = self.pmn.copy()
        for i in range(add_num): # 依次+1
            self.__add_1(ls)
        return PermutationNum(ls)
    
    def __sub__(self, sub_num:int): # 减整数的操作
        ls = self.pmn.copy()
        for i in range(sub_num): # 依次-1
            self.__sub_1(ls)
        return PermutationNum(ls)
    
    def __str__(self): # 打印的格式
        return str(self.pmn)
        
    def __ifDuplicate(self, ls): # 判断全排列数列表是否重复的方法
        tmp = list(set(ls))
        assert len(tmp) == len(ls), "全排列数列表不能有重复数字"
    
    def __add_1(self, ls): # +1方法
        for i in range(len(ls)-1, -1, -1):
            k = i # 记录后面大于该位，且是后面中大于该位数最小的数的索引
            tmpmax = max(ls)
            for j in range(i+1, len(ls)):
                if ls[j] > ls[i] and ls[j] <= tmpmax:
                    k = j
                    tmpmax = ls[j]
            if k != i: # 如果发现交换了，就交换，将后面的数按大小顺序排列，并停止循环
                self.__swap(ls, k, i) # 交换该位与后面中大于该位数最小的数
                self.__sort(ls, i)
                break
            
            
    def __sub_1(self, ls): # -1方法
        for i in range(len(ls)-1, -1, -1):
            k = i # 记录后面小于该位，且是后面中小于该位数最大的数的索引
            tmpmin = min(ls)
            for j in range(i+1, len(ls)):
                if ls[j] < ls[i] and ls[j] >= tmpmin:
                    k = j
                    tmpmin = ls[j]
            if k != i: # 如果发现交换了，就交换，将后面的数按大小顺序反向排列，并停止循环
                self.__swap(ls, k, i) # 交换该位与后面中小于该位数最da的数
                self.__sort(ls, i, reverse=True)
                break
    
    def __swap(self, ls, k, j): 
        # 交换元素
        tmp = ls[k]
        ls[k] = ls[j]
        ls[j] = tmp 
    
    def __sort(self, ls, k, reverse=False):
        # 对列表ls第k位之后的元素进行排列，reverse=True表示反向排列
        tmp = sorted(ls[k+1:], reverse=reverse)
        for i in range(k+1, len(ls)):
            ls[i] = tmp[i-k-1]
    
    def __len__(self):
        return len(self.pmn)
    
    @staticmethod
    def A(n):
        # 计算全排列的数量
        a = 1
        for i in range(1, n+1):
            a *= i
        return a
    
if __name__ == "__main__":
    test_list = [2, 3, 4, 10]
    pmn = PermutationNum(test_list) # 实例化
    for i in range(PermutationNum.A(len(pmn))):
        print(pmn+i)
    print()
    test_list.reverse()
    pmn = PermutationNum(test_list) # 实例化
    for i in range(PermutationNum.A(len(pmn))):
        print(pmn-i)