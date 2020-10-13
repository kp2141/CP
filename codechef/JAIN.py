
testcase = int(input())
for _ in range(testcase):
    tot_dishes = int(input())
    list1 = []
    list2 = [0]*30
    for _ in range(tot_dishes):
        mask = 0
        unordered_set = set()
        string = input()
        for j in string:
            if (j== 'a'):
                unordered_set.add(0)
            elif (j== 'e'):
                unordered_set.add(1)
            elif (j == 'i'):
                unordered_set.add(2)
            elif (j == 'o'):
                unordered_set.add(3)
            else:
                unordered_set.add(4)
        for i in unordered_set:
            mask+=(1<<i)
        list2[mask ] =list2[mask ] +1
    ans = 0
    for i in range(1 ,32):
        for j in range(1 ,32):
            if( i|j )==((1<<5)-1):
                if( i==j):
                    ans+=(list2[i]*(list2[i]-1))
                else:
                    ans+=(list2[i]*list2[j])

    print(int(ans/2))















