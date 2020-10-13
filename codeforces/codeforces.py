R = lambda : map(int,input().split())

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True):  
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    lst = []
    for p in range(2, n): 
        if prime[p]: 
            lst.append(p) 
    return lst
def isPrime(n) :  
    # Corner cases  
    if (n <= 1) :  
        return False
    if (n <= 3) :  
        return True
    
    # This is checked so that we can skip   
    # middle five numbers in below loop  
    if (n % 2 == 0 or n % 3 == 0) :  
        return False
    
    i = 5
    while(i * i <= n) :  
        if (n % i == 0 or n % (i + 2) == 0) :  
            return False
        i = i + 6
    
    return True

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:

        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


# print(lst)
p = input()
list_n = list(R())
lst_ans = []
for i in list_n:
    lst = SieveOfEratosthenes(i)
    lst_pow = [x for x in powerset(lst)]
    # print(lst_pow)
    cnt = 0
    cnt_first = 0
    prime_sum = 0

    for j in lst_pow:
        if isPrime(sum(j)):
            cnt+=1
    lst_ans.append(str(cnt))
print(' '.join(lst_ans))
   
        