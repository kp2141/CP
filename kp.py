if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([score, name])
    list.sort()
    last_value = float(list[0][0])
    # print(first_value)
    second_last_value = 0
    const = 0
    for i in list:

        if float(i[const]) > last_value:
            second_last_value = float(i[const])
            break
    lst = []
    # print(second_last_value)
    for i in list:
        if float(i[const]) == second_last_value:
            lst.append(i[1])
    lst.sort()
    for i in lst:
        print(i)
    # print(lst)
    # print(list)
