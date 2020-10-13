testcase = int(input())
for _ in range(testcase):
    N, d = input().split(' ')
    list1 = [int(y) for y in N]
    len_list1 = len(list1)
    i=0
    while i<len(list1):
        for j in list1[i+1:]:
            if list1[i]>int(d) or (list1[i]>j):
                # print(list1[i],end="")
                list1.remove(list1[i])
                list1.append(int(d))
                i-=1
                break
        if (i==len(list1)-1) and list1[i]>int(d):
            list1.remove(list1[i])
            list1.append(int(d))
        i+=1
    print("".join(map(str,list1)))


