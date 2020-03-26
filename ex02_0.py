from math import sqrt

def old_solution(n):
    count = 0
    lst0 = [[i] for i in range(int(sqrt(n * 2)), n)]
    lst = []
    while len(lst0):
        #print("------------------------------------------------")
        #print(lst0)
        #print(len(lst0))
        #print(" ")
        #while (sum(e) + j) < n and j < e[-1]:
        for e in lst0:
            #print(e)
            j = 0
            for j in range(1, min(e[-1], (n - sum(e)))):
                #print("j:" + str(j))
                if (j != 1):
                    lst.append(e + [j])
                    #print(e + [j])
            j = j + 1
            #print("jend: " + str(j))
            if (sum(e) + j) == n and j < e[-1]:
                count = count + 1
                #print("+")
            #print("----")
        lst0 = lst
        lst = []
    return(count)

def solution(n):
    dic = {}
    return(function(n, dic) - 1)
    

def function(n, dic):
    #print(dic)
    if (n < 0):
        return(0)
    if (n == 0):
        return(1)
    if n in dic:
        return(dic[n])
    ret = adj(n)
    k = 1
    #print("new----")
    #print("n: " + str(n))
    while (n - pent(k) >= 0):
        ret = ret + sign(k) * (function(n - pent(k), dic))
        k = k + 1
        #print(ret)
    dic[n] = ret
    return(ret)

def sign(n):
    k = int((n + 1) / 2) + 1
    return((-1)**k)

def pent(n):
    k = int((n + 1) / 2) * (-1)**(n+ 1)
    return((3*k**2 -k) / 2)

def adj(n):
    ret = 0
    i = -8
    while(i < 10):
        if (n == 3*i**2 - i):
            ret = 1
            break
        i = i + 1
    return(int(ret * (-1)**i))

print(solution(200))
#print(old_solution(22))
