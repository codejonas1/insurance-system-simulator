import time

def getRandomNumber(start, end):
    r=end-start+1
    number = time.time_ns()%r+start

    return number

def getRandomBool():
    return bool(getRandomNumber(0,1))

def isProbability(n):
    x = getRandomNumber(0, 100)
    if(x<n): return True

    return False