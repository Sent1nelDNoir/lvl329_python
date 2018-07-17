def makeMove(sticks):
    print(sticks)
    return sticks % 4 if sticks % 4 != 0 else 1
