testcase = int(input())
for _ in range(testcase):
    N, K = map(int,input().split())
    anger_list = list(map(int, input().split()))
    k=0
    for i in range(N):
        sum = 0
        temp = 1
        flag = False
        for j in range(i,N):
           sum+=int(anger_list[j]/temp)
           if(sum>K):
               flag = True
               break
           temp+=1
        if(flag==False ):
            print(i+1)
            break
        k+=1
    if(k==N):
        print(N+1)