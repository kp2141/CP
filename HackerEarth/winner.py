R = lambda:map(int,input().split())
for _ in range(int(input())):
    n,k = R()
    if n%(k+1)==0:
        print("Dishant")
    else:
        print("Arpa")