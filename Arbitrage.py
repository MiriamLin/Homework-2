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
temp = [1, 0, 0, 0, 0, 0, 1]
temp2 = [[0 for _ in range(5)] for _ in range(5)]
for i in range(0,5):
    for j in range(0,5):
        for k in range(0,5):
            for l in range(0,5):
                for m in range(0,5):
                    if i==1 or j==1 or k==1 or l==1 or m==1:
                        continue
                    temp[1]=i
                    temp[2]=j
                    temp[3]=k
                    temp[4]=l
                    temp[5]=m
                    bb=1
                    for u in range(0,5):
                        for v in range(0,5):
                            temp2[u][v]=0
                    for u in range(0,6):
                        if temp[u]==temp[u+1]:
                            bb=0
                        temp2[temp[u]][temp[u+1]]+=1
                        temp2[temp[u+1]][temp[u]]+=1
                    for u in range(0,5):
                        for v in range(0,5):
                            if temp2[u][v]>1:
                                bb=0
                    if bb==0:
                        continue
                    now=5.0
                    for u in range(0,6):
                        now=997*now*a[temp[u+1]][temp[u]]/(1000*a[temp[u]][temp[u+1]]+997*now)
                    if now>20.0:
                        for u in range(0,7):
                            b[u]=temp[u]
                        break
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
    

