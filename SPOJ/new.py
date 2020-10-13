def calc(a):
    ans = 0
    for i in range(len(a)-1,-1,-1):
        if (a[i]-(i+1)>2):
            print("Too chaotic")
            return
        for j in range(max(0,a[i]-2),i):
            if a[j]>a[i]:
                ans+=1
    print(ans)

for _ in range(int(input())):
    input()
    print(calc(list(map(int,input().split()))))