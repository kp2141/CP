
R = lambda : map(int,input().split())
def shrink(string):
    return "".join(sorted(list(set(string))))

def has_all_vowels(str1, str2):
    return set(str1+str2) == {'a','e','i','o','u'}

if __name__=="__main__":
    for i in range(int(input())):
        n = int(input())
        map = {}
        for i in range(n):
            string = input()
            if shrink(string) in map:
                map[shrink(string)]+=1
            else:
                map[shrink(string)] = 1
        ans = 0
        for i in map:
            for j in map:
                if i!=j and has_all_vowels(i,j):
                    ans += map[i]*map[j]

        ans //= 2
        # if "aeiou" in map:
        #     ans+=(map['aeiou']*(map['aeiou']-1))//2
        print(ans)
        # print(map)