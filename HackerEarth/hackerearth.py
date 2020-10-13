n, h1, h2, a, b, c = map(int,input().split())
count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if h2-h1==a+b+c:
                count+=1
print(count)