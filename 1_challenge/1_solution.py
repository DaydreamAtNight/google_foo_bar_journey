def solution(data,n):
    result = []
    for i in data:
        n_temp = 0
        for j in data:
            if i == j:
                n_temp = n_temp+1
        if n_temp <= n:
            result.append(i)
    return result


# main

print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5],1))


