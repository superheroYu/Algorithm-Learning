def move(n, a, b):
    print("%d: %s-->%s" % (n, a, b))

def hanoi(n:int, a:str, b:str, c:str):
    # 把编号1到n从a移到b，c为辅助柱
    if n == 1: move(n, a, b) 
    else:
        hanoi(n-1, a, c, b) # 把编号1到n-1的从a移到c，b为辅助柱
        move(n, a, b) # 把编号n从a移到b
        hanoi(n-1, c, b, a) # 把把编号1到n-1由c柱移到b柱子，a为辅助柱
hanoi(8, 'A', 'B', 'C')
    