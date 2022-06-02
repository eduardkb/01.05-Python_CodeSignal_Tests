# on a array of integers find the highest product
# and return the product
from MyModule import fClearConsole
fClearConsole()


def solution(inputArray):  # my solution
    iMax = inputArray[0] * inputArray[1]
    for i, elem in enumerate(inputArray):
        if i < len(inputArray) - 1 and iMax < elem * inputArray[i+1]:
            iMax = elem * inputArray[i+1]
    return iMax


def best_solution(inputArray):  # best solution
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])


inputArray = [3, 6, -2, -5, 7, 3]
inputArray = [-23, 4, -3, 8, -12]
print("Highest product is:", solution(inputArray))
