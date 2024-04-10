liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
a=[[0.0 for _ in range(5)] for _ in range(5)]
b=[0 for _ in range(10)]
c=[0.0 for _ in range(10)]
a = [
    [0, 17, 11, 15, 21],
    [10, 0, 36, 13, 25],
    [7, 4, 0, 30, 10],
    [9, 6, 12, 0, 60],
    [5, 3, 8, 25, 0]
]
b = [1, 0, 2, 4, 3, 2, 1]
c[0] = 5.0
for i in range(1,7):
    x = a[b[i-1]][b[i]]
    y = a[b[i]][b[i-1]]
    c[i]=997*c[i-1]*y/(1000*x+997*c[i-1])
    a[b[i]][b[i-1]] -= c[i]
    a[b[i-1]][b[i]] += c[i-1]

if c[6]>20.0:
    print("path: ",end="")
    for i in range(6):
        print("token" + chr(ord('A') + b[i]), end="->")
    print("tokenB, tokenB balance=", end="")
    print(c[6])
    

