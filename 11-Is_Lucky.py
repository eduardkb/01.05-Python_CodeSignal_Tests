"""
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of 
the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.

example 2
134008
true
"""
from MyModule import fClearConsole, fStopWatch
fClearConsole()


def best_solution(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    # map = for each list item executes the function in first argument
    return sum(map(int, left)) == sum(map(int, right))


def solution(n):
    a = list(str(n))
    l1 = a[0:int(len(str(n))/2)]
    l2 = a[int(len(str(n))/2):len(str(n))]
    l1 = [int(x) for x in l1]
    l2 = [int(x) for x in l2]
    return True if sum(l1) == sum(l2) else False


# input = 1230    # result true
input = 239017  # result false
# input = 1  # result false
# input = 482905 # result true
# input = 134008 # result false
# input = 5134008 # result false


sw = fStopWatch()
print("Start time:", sw)

# fRes = solution(input)
fRes = best_solution(input)

sw = fStopWatch(sw)
print("Execution time:", sw)
print(f'Result: {fRes}')
