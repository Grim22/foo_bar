def solution(xs):

    pos = [i for i in xs if i > 0]

    neg = [i for i in xs if i < 0]

    if len(pos) == 0:

        if len(neg) == 0:

            return (str(0))

        if len(neg) == 1:

            if 0 in xs:

                return (str(0))

            else:

                return(str(neg[0]))

    if len(pos) == 1:

        if len(neg) == 1:

            return (str(pos[0] * neg[0]))

        if len(neg) == 0:

            if 0 in xs:

                return(str(0))

            else:

                return(pos[0])

    ret = 1

    for i in pos:

        ret = ret * i

    neg.sort(reverse = True)

    for i in neg[len(neg) % 2::]:

        ret = ret * i

    print(pos)
    print(neg)
    print(neg[len(neg) % 2::])
    return (str(ret))

print(solution([1]))
