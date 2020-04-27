import random

def nb_div(elem, div):
    count = 0
    for i in div:
        if elem in i:
            count = count + 1
    return(count)

def solution(l):
    j = 0
    div = []
    div_num = []
    for e in l:
        le = [i for i in range(1, e + 1) if e % i == 0 and i in l[:j]]
        num = 0
        for i in le:
            num = num + l[:j].count(i)
        j = j + 1
        div.extend([le])
        div_num.extend([num])

    res = 0
    i = 0
    for i in range(0, len(l)):
        len_d = div_num[i]
        if len_d == 0:
            sub = 0
        else:
            sub = len_d * nb_div(l[i], div[i + 1:])
        res = res + sub
        i = i + 1
    
    return(res)

num = 20
max_int = 10

lst = []
for i in range(1, num + 1):
    lst.extend([random.randint(1, max_int)])
#print(lst)
print(solution([1,2,3,4,5,6]))