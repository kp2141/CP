testcase = int(input())
for _ in range(0,testcase):
    N = int(input())
    part_list = map(int, input().split(' '))
    neg_sumcount= []
    pos_sumcount = []
    for i in part_list:
        if i>0 :
            pos_sumcount.append(i)
        if i<0 :
            neg_sumcount.append(i)

    if len(pos_sumcount)==0:
        print(len(neg_sumcount), len(neg_sumcount))
    elif len(neg_sumcount)==0:
        print(len(pos_sumcount), len(pos_sumcount))
    elif len(pos_sumcount)>len(neg_sumcount):
        print(len(pos_sumcount),len(neg_sumcount))
    else:
        print(len(neg_sumcount), len(pos_sumcount))