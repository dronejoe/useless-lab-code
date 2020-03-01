from math import pow

cases = {}
lines = []

inputFile = input("What is the name of the file?")

def createBoard(n,r):
    power = 0
    board = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                board[0].append(1)
            else:
                board[i].append(r**power)

            power += 1

    return board

def sumOfBoard(arr):
    sum = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            sum += arr[i][j]

    return sum

with open(inputFile) as f:
    for line in f:
        lines.append([int(x) for x in line.split()])

for i in range(lines[0][0]): #range(lines[0][0]) = T (number of test cases)

    r = lines[i+1][0]
    n = lines[i+1][1]
    m = lines[i+1][2]

    currentBoard = createBoard(n,r)
    remainder = sumOfBoard(currentBoard) % m

    cases.update({i+1:remainder})

with open("outputFile.txt","w") as out:
    out.truncate(0)
    for i in cases:
        out.write("Case #%s: %s\n" % (i,int(cases.get(i))))
