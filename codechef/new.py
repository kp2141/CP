# cook your dish here
from sys import stdin, stdout
import math
from itertools import permutations, combinations
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
def solve_linear(equation,var='x'):
    expression = equation.replace("=","-(")+")"
    grouped = eval(expression.replace(var,'1j'))
    return -grouped.real/grouped.imag


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


# --------------------------------------

def myCode():
    l = L()
    print(max(l[0],l[1],l[2],))
    
def main():
    for t in range(I()):
        myCode()
    
if __name__ == '__main__':
    
    main()




