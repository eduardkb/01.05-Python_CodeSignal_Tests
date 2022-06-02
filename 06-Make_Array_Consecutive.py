"""
Ratiorg got statues of different sizes as a present from CodeMaster 
for his birthday, each statue having an non-negative integer size. 
Since he likes to make things perfect, he wants to arrange them from 
smallest to largest so that each statue will be bigger than the 
previous one exactly by 1. He may need some additional statues to be 
able to accomplish that. Help him figure out the minimum number of 
additional statues needed.

Example:
For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.
"""

from MyModule import fClearConsole
fClearConsole()


def solution(statues):
    statues.sort()
    iRes = 0
    for i in range(1, len(statues)):
        iRes += statues[i] - statues[i-1] - 1

    return iRes


def best_solution(statues):
    return max(statues) - min(statues) - len(statues) + 1


statues = [6, 2, 3, 8]
statues = [1]
statues = [5, 4, 6]
print("Resolution:", solution(statues))
