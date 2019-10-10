def solution(arr, divisor):
    answer = []
    check = 0
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
        else:
            check += 1

    if len(arr) != check:
        answer.sort()

    else:
        answer.append(-1)

    return answer

arr = [5,9,7,10]
divisor = 5

## arr = [2,36,1,3]
## divisor = 1

### arr = [3,2,6]
### divisor = 10

print(solution(arr, divisor))
# return 이 [5,10] 이 되어야 한다.
## return 이 [1,2,3,36] 이 되어야 한다.
### return 이 [-1] 이 되어야 한다.
