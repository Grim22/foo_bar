def solution(n, b):
    h = []
    while (n not in h):
        h.append(n)
        l = list(n)
        y = sorted(l)
        x = sorted(l, reverse = True)
        z = [int(x[i]) - int(y[i]) for i in range(len(x))]
        k = len(z)
        for i in range(k -1, 0, -1):
            if z[i] < 0:
                z[i] = b + z[i]
                z[i - 1] = z[i - 1] - 1
        z = [str(i) for i in z]
        n = "".join(z)
    ret = len(h) - h.index(n)
    print(ret)
    return(ret)

solution("1211", 10)
solution("210022", 3)


    
