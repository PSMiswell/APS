def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        I = commands[x][0]
        J = commands[x][1]
        K = commands[x][2]
        slice = array[I-1:J]
        slice.sort()
        answer.append(slice[K-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array,commands))
# return 값이 [5,6,3] 이 되어야 한다.
