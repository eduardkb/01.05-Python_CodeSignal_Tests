from MyModule import fClearConsole, fStopWatch
fClearConsole()


def best_solution(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


def fAlmostIncreasingFunc(sequence):
    for i in range(len(sequence)):
        alt = sequence.pop(i)
        bSeq = True
        if sequence == sorted(sequence):
            if len(sequence) == len(set(sequence)):
                return True
        sequence.insert(i, alt)
    return False


# aList = [1, 2, 3, 4, 5]         # TRUE
# aList = [1, 1, 2, 3, 4, 4]    # FALSE
aList = [1, 3, 2, 6, 8, 4, 10]    # FALSE
# aList = [1, 2, 3, 44, 4, 5, 22, 6]  # TRUE
# aList = [3, 5, 67, 98, 3]  # TRUE
# aList = list(range(20000))
# aList.insert(4900, 2)
# aList.insert(19999, 4)


sw = fStopWatch()
print("Start time:", sw)

# fRes = fAlmostIncreasingFunc(aList)
fRes = best_solution(aList)

sw = fStopWatch(sw)
print("Execution time:", sw)
print(f'Result: {fRes}')
