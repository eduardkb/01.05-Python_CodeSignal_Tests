# an n-interesting polygon. Your task is to find the area of a polygon for a given n.
# For n = 2, the output should be
#   solution(n) = 5;
# For n = 3, the output should be
#   solution(n) = 13.
# for 4 = 25
# for 5 = 41

# on a array of integers find the highest product
# and return the product
from MyModule import fClearConsole
fClearConsole()


def solution(n):  # my solution
    area = 1
    added = 0

    for i in range(1, n+1):
        if i > 1:
            added = (added - 4) + (4 * 2)
            area += added
    return area


def best_solution(n):
    return n**2 + (n-1)**2


n = 5
print("Area is:", solution(n))
