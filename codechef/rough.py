def pow(a,b):
    print(b)
    if b==0:
        return 1
    elif b%2==0:
        return pow(a,b//2)**2
    else:
        return a*pow(a,b//2)**2

print(pow(2,1000))
        