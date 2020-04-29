def solution2(x, y):
    x = int(x)
    y = int(y)
    count = 0
    while(x != 1 or y != 1):
        if x == y:

            return("impossible")
        elif x > y:
            x = x - y
        else:
            y = y - x
        count = count + 1
    return(str(count))

def solution(x, y):
    x = int(x)
    y = int(y)
    x_tmp = x
    x = max(x,y)
    y = min(x_tmp,y)
    count = 0
    while(y != 1):
        if x % y == 0:
            return("impossible")
        count = count + x/y
        x = x - y * int(x/y)
        x_tmp = x
        x = max(y,x)
        y = min(y,x_tmp)
    count = count + x -1
    return(str(count))

a = str(1 * 10**50)
b = '333'
print("new " + solution(a, b))
#print("old " + solution2(a,b))