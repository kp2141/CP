list1 = [0]*101
list1[0] = 0
list1[1] = 0
list1[2] = 0
list1[3] = 1
for i in range(4,101):
    j=i-2
    temp = 0
    while(j>=0):
        temp = temp+j*(j+1)/2
        j-=2
    list1[i]=list1[i-1]+int(temp)

print(list1[int(input())])
