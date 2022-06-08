from MyModule import fClearConsole, fStopWatch
fClearConsole()


def best_solution(input):
    return False


def solution(input):
    return False


input = 0

sw = fStopWatch()
print("Start time:", sw)

fRes = solution(input)
# fRes = best_solution(input)

sw = fStopWatch(sw)
print("Execution time:", sw)
print(f'Result: {fRes}')

print("---\nEND")
