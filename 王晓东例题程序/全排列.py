def swap(ls, idx1, idx2):
    tmp = ls[idx1]
    ls[idx1] = ls[idx2]
    ls[idx2] = tmp

def perm(ls, k:int, m:int):
    if k==m:
        print(ls)
        # for i in range(m+1):
        #     print(ls[i], end='')
        # print()
    else:
        for i in range(k, m+1):
            swap(ls, k, i)
            perm(ls, k+1, m)
            swap(ls, k, i)

ls = [1, 2, 3, 4]
perm(ls, 0, 3)