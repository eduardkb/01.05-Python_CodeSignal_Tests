# century calculator
#   year 23 = century 1
#   100 = century 1
#   101 = cen 2
#   2000 = cen 20
#   2001 = cen 21
from MyModule import fClearConsole
fClearConsole()


def solution(year):  # my solution
    i = int(year/100)
    return i if year % 100 == 0 else i+1


def best_solution(year):  # best solution
    return (year + 99) // 100


year = 2022
print("century of {} is {}".format(year, solution(year)))
