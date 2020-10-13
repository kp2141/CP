# cook your dish here
from sys import stdin, stdout
import math
from itertools import permutations, combinations,permutations
from collections import defaultdict
from collections import Counter
from bisect import bisect_left
import sys
from queue import PriorityQueue
import operator as op
from functools import reduce

mod = 1000000007


def L():
    return list(map(int, stdin.readline().split()))


def In():
    return map(int, stdin.readline().split())


def I():
    return int(stdin.readline())


def printIn(ob):
    return stdout.write(str(ob) + '\n')


def powerLL(n, p):
    result = 1
    while (p):
        if (p & 1):
            result = result * n % mod
        p = int(p / 2)
        n = n * n % mod
    return result


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom
def solve_linear(equation,var='x'):
    expression = equation.replace("=","-(")+")"
    grouped = eval(expression.replace(var,'1j'))
    return -grouped.real/grouped.imag
def dfs(visited, graph, node):

    if node not in visited:
        # cnt+=1
        # print("hello")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return len(visited)
    


# --------------------------------------

def myCode():
    n = I()
    lst = L()
    d1  = {1:[],2:[],3:[],4:[],5:[]}
    # d2  = {1:[],2:[],3:[],4:[],5:[]}
    # max_plus = -sys.maxsize
    # max_minus = sys.maxsize
    # for i in range(len(lst)):
    #     s1 = f"{i+1}+{lst[i]}x"
    #     plus_count = 0
    #     minus_count  = 0
    #     for j in range(len(lst)):
    #         if i==j:
    #             continue
    #         s2 = f"{j+1}+{lst[j]}x"
    #         if lst[i]!=lst[j]:
    #             ans = solve_linear(s1+"="+s2)
    #             if ans>0.0:
    #                 plus_count+=1
    #                 d1[i+1].append(j+1)
    #             else:
    #                 minus_count+=1
    #                 d2[i+1].append(j+1)

    #             # d[i].append(ans)
    #         else:
    #             minus_count+=1
    #             d2[i+1].append(j+1)
        
                
    #     max_plus = max(max_plus,plus_count)
    #     max_minus =min(max_minus,minus_count)
    
    
    # # key_w = 0
   
    # # for i in d1:
    # #     if len(d1[i])>0:
    # #         key_w = i
    # #         break
    # # if key_w==0:
    # #     key_w = 1
    # min_len = sys.maxsize
    # cnt = n
    # for i in d1:
    #     if cnt==0:
    #         break
    #     cnt-=1
    #     min_len = min(len(d1[i]),min_len)
    # print(d1)
    # ans_w = -sys.maxsize
    # # ans_b = sys.maxsize
    # for i in d1:
    #     visited_w = set()
    #     ans_w = max(ans_w,dfs(visited_w, d1, i))
        # ans_b = min(ans_b,dfs(visited_w, d1, i))
    # # if max_minus==sys.maxsize:
    # #     max_minus = n
    # print(min_len+1,ans_w)
    # # print(d)
    # # print(d1)
    # # print(d2)
    for i in range(len(lst)):
        for j in range(0,i):
            if lst[j]>lst[i]:
                d1[i+1].append(j+1)

        for k in range(i+1,n):
            if lst[k]<lst[i]:
                d1[i+1].append(k+1)
    min_len = sys.maxsize
    cnt = n
    for i in d1:
        if cnt==0:
            break
        cnt-=1
        min_len = min(len(d1[i]),min_len)
    # print(d1)
    ans_w = -sys.maxsize
    # ans_b = sys.maxsize
    for i in d1:
        visited_w = set()
        ans_w = max(ans_w,dfs(visited_w, d1, i))
        # ans_b = min(ans_b,dfs(visited_w, d1, i))
    print(min_len+1, ans_w)
    
def main():
    for t in range(I()):
        myCode()

if __name__ == '__main__':
    # print(1000000000-1+1000000000-2+1000000000-4)
    main()


