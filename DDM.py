'''Hacker rank Designer Door Mate problem solution'''


a, b = [int(x) for x in input().split()]
str = '.|.'
const=1
flag=False
for i in range(a):
    if const==a:
        print(('WELCOME').center(b,'-'))
        flag=True
    else:
        print((const*str).center(b,'-'))
    if (flag):
        const-=2
    else:
        const+=2