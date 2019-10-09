def solution(arr):
    answer = []
    cnt = 0
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != answer[cnt]:
            answer.append(arr[i])
            cnt += 1

    return answer

arr = [1,1,3,3,0,1,1]
## arr = [4,4,4,3,3]

print(solution(arr))
# answer 이 [1,3,0,1] 이 되어야 한다.
## answer 이 [4,3] 이 되어야 한다.

'''
# 정확성 테스트에서 테스트 케이스는 전부 통과했지만,
# 효율성 테스트의 테스트 케이스는 전부 실패(시간 초과)
# 아마 반복문 2개를 써서 그런 것 같다

def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                arr[j] = 10
            elif arr[i] != arr[j]:
                break
    for k in range(len(arr)):
        if arr[k] != 10:
            answer.append(arr[k])
    return answer
'''