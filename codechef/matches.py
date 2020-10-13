for _ in range(int(input())):
    a , b = map(int, input().split())
    cnt = 0
    while True:
        if a%b==0 or b%a==0:
            break
        if a//b>1:
            break
        if b//a>1:
            break
        elif a/b>1:
            # if a%b+1==b:
            #     a = a//b
            if a//b==1:
                a-=b
            # else:a -= b*(a//b-1)
        elif b/a>1:
            # if b%a+1==a:
            #     b = b//a
            if b//a==1:
                b-=a
            # else:b -= a*(b//a-1)
        cnt+=1
        # print(a,b)

    if cnt%2==0:
        print("Ari")
    else: print("Rich")





