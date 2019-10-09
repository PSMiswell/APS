def solution(s):
    length = len(s)
    mid = length//2
    answer = ''
    if length % 2:
        answer = s[mid]
    else:
        answer = s[mid-1:mid+1]
    return answer

s = "abcde"
## s = "qwer"

print(solution(s))
# return 값이 "c" 가 되어야 한다.
## return 값이 "we" 가 되어야 한다.