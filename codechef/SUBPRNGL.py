import copy
import atexit
import io
import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER
# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

def sub_lists(list1):
    sublist = [[]]
    temp = len(list1)
    for i in range(temp + 1):
        for j in range(i + 1, temp + 1):
            sub = list1[i:j]
            sublist.append(sub)
    return sublist

testcase = int(input())
for _ in range(testcase):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    S = sub_lists(A)

    S.remove([])
    # print(S)
    print(S)
    new_list = list(S)
    ans = 0
    for i in S:
        temp = len(i)

        if temp<K:
            # print("********")
            i.extend(i*(K-temp))

        print(S)
        list2 = new_list[S.index(i)]
        i.sort()
        X = i[K - 1]
        F=list2.count(X)
        if F in list2:
            ans+=1
    print(ans)