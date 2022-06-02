import re
from MyModule import fClearConsole
fClearConsole()


def solution(inputString):  # my solution (accepts phrases)
    inputString = (re.sub('\W+', '', inputString)).lower()
    sInv = ''
    for i in range(len(inputString) - 1, -1, -1):
        sInv += inputString[i]

    return True if inputString == sInv else False


def best_solution(inputString):  # best solution (input must not be phrases)
    return inputString.lower() == inputString[::-1].lower()


inputString = "Omissíssimo"
#inputString = "Anotaram a data da maratona."

print("Is {} a palindrome? {}".format(inputString, solution(inputString)))
