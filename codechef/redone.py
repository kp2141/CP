m = 1000000007
list1 = [0]*10000001
list1[0] = 0
list1[1] = 1
for i in range(2,len(list1)):
    list1[i] = (list1[i-1] + i + ((list1[i-1])*(i)))%m
for i in range(int(input())):
    print(list1[int(input())])
