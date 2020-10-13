R = lambda:map(int,input().split())

for _ in range(int(input())):
    n,z = R()
    A = list(input().split())
    B = list(A)
    for i in range(z):
        for i in range(1,len(A)):
            if B[i-1]=='0' and B[i]=='1':
                A[i-1]=B[i]
                A[i]=B[i-1]

        B = list(A)

    print(" ".join(A))