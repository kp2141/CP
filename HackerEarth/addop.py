# from math import gcd
# for _ in range(int(input())):
#     n = int(input())
#     sum = 0
#     for i in range(1,n+1):
#         for j in range(i+1,n+1):
#             for k in range(j+1,n+1):
#                 for l in range(k+1,n+1):
#                     sum=gcd(gcd(i,j),gcd(k,l))
#                     print(sum)
#
#
#     print("so the answer of the gcd is:"+str(sum))




t = int(input())
import math

M = 10 ** 9 + 7
m = {}
def meth(x):
    if x < 4:
        return 0
    print(x)
    val = 0
    """
    count=1
    for i in range(x-3,0,-1):
        res=0
        for j in range(1,i+1):
            res+=j
        val+=(res*count)
        val%=M
        count+=1
    """
    csum = ((x - 2) * (x - 3)) // 2
    nsum = 0
    for i in range(1, x - 3 + 1):
        val += i * (csum - nsum)
        val %= M
        nsum += (x - 3 - i + 1)

    # print(val)
    for i in range(x, 1, -1):
        if x // i in m:
            val -= m[x // i]
        else:
            val1 = meth(x // i)
            val1 %= M
            m[x // i] = val1
            val -= val1
    return val
for i in range(t):
    n = int(input())
    if n < 4:
        print(0)
        continue
    val = 0
    for j in range(n, 0, -1):
        if n // j in m:
            val += pow(j, 4, M) * m[n // j]
            val %= M
            print("hello")
        else:
            val1 = meth(n // j)
            val1 %= M
            m[n // j] = val1
            val += pow(j, 4, M) * val1
            val %= M
    print(val)
