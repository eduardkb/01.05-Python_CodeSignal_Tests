"""
After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, but there's a 
rumour that all the free rooms are haunted! Since the CodeBots are quite 
superstitious, they refuse to stay in any of the free rooms, or any of the rooms 
below any of the free rooms.
"""

from MyModule import fClearConsole, fStopWatch
fClearConsole()


def best_solution(matrix):
    r = len(matrix)
    c = len(matrix[0])
    total = 0
    for j in range(c):
        for i in range(r):
            if matrix[i][j] != 0:
                total += matrix[i][j]
            else:
                break
    return total


def solution(matrix):
    aIgnore = []
    iSum = 0
    for i, l in enumerate(matrix):
        for j, c in enumerate(l):
            if i == 0:
                aIgnore.append(False)
            if not aIgnore[j]:
                if c == 0:
                    aIgnore[j] = True
                else:
                    iSum += c
    return iSum


# input = [[0, 1, 1, 2],
#          [0, 5, 0, 0],
#          [2, 0, 3, 3]]      # result 9

input = [[1, 1, 1, 0],
         [0, 5, 0, 1],
         [2, 1, 3, 10]]      # result 9

# input = [[1, 1, 1],
#          [2, 2, 2],
#          [3, 3, 3]]      # result 18

sw = fStopWatch()
print("Start time:", sw)

# fRes = solution(input)
fRes = best_solution(input)

sw = fStopWatch(sw)
print("Execution time:", sw)
print(f'Result: {fRes}')
