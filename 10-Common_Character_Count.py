"""
Given two strings, find the number of common characters between them.
Ex:
    For s1 = "aabcc" and s2 = "adcaa", the output should be
    solution(s1, s2) = 3.
    Strings have 3 common characters - 2 "a"s and 1 "c".
"""

from MyModule import fClearConsole, fStopWatch
fClearConsole()


def best_solution(s1, s2):
    com = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(com)


def solution(s1, s2):
    iCount = 0
    for elm in s1:
        pos = s2.find(elm)
        if pos >= 0:
            iCount += 1
            s2 = s2[0:pos:] + s2[pos+1::]

    return iCount


# s1 = "aabcc"
# s2 = "adcaa"  # result = 3

# s1 = "zzzz"
# s2 = "zzzzzzz"   # res = 4

s1 = "abca"
s2 = "xyzbac"    # res = 3

sw = fStopWatch()
print("Start time:", sw)

fRes = solution(s1, s2)
# fRes = best_solution(input)

sw = fStopWatch(sw)
print("Execution time:", sw)
print(f'Result: {fRes}')
