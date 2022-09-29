def q(n, m):
    if n < 1 or m < 1:
        return 0
    elif n == 1 or m == 1:
        return 1
    elif n < m:
        return q(n, n)
    elif n==m:
        return 1+q(n,n-1)
    elif n>m and m >1:
        return q(n, m-1)+q(n-m, m)
print(q(6, 10))


        
        
        