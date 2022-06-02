from asyncio.windows_events import NULL
import os
import datetime


def fClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    print("============================================")


"""
    1st call with no parameter
        EXAMPLE: sw = fStopWatch()
        - initiates the timer
    2nd call rerturns time delta
        EXAMPLE sw = fStopWatch(sw)
        - sw contains the execution time (delta)

"""


def fStopWatch(timer=NULL):
    if timer == 0 or timer == NULL:
        return datetime.datetime.now()
    else:
        return (datetime.datetime.now() - timer)
