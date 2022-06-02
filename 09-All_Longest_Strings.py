"""
Given an array of strings, return another array containing all of its longest strings.
Ex:
    For inputArray = ["aba", "aa", "ad", "vcd", "aba"], 
    the output should be solution(inputArray) = ["aba", "vcd", "aba"].
"""

from MyModule import fClearConsole, fStopWatch
fClearConsole()


def best_solution(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r


def solution(inputArray):
    res = []
    maxLen = 0
    for elm in inputArray:
        if len(elm) > maxLen:
            maxLen = len(elm)
            res = []
            res.append(elm)
        elif len(elm) == maxLen:
            res.append(elm)
    return res


# input = ["aba", "aa", "ad", "vcd", "aba"]  # out = ["aba", "vcd", "aba"]
# input = ["a",  "abc",  "cbd",  "zzzzzz",  "a",  "abcdef",
#          "asasa",  "aaaaaa"]  # out = ["zzzzzz", "abcdef", "aaaaaa"]
input = ["enyky",  "benyky",  "yely",  "varennyky"] # out = ["varennyky"]

sw = fStopWatch()
print("Start time:", sw)

fRes = solution(input)
# fRes = best_solution(input)

sw = fStopWatch(sw)
print("Execution time:", sw)
print(f'Result: {fRes}')
