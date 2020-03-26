def solution(data, n):

    data = [i for i in data if data.count(i) <= n]

    return (data)

lst = [1, 2, 3, 3, 1, 4, 5, 3, 1, 1, 2, 6, 7, 2, 8, 7, 7]
n = 3

print(solution(lst, n))
