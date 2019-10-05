from tkinter import Tk, Button
from math import pow, sqrt
count = 0
startingPoint = 0
destPoint = 0
openPaths = []
uniqueCheck = set()
def checkRepInNp(lst):
    prevLen = len(uniqueCheck)
    str1 = str(lst[len(lst)-1][0] + lst[len(lst)-1][1])
    str2 = str(lst[len(lst)-2])
    uniqueCheck.add(str1 + str2)
    if len(uniqueCheck) == prevLen:
        return False
    return True

def checkRep(lst):
    target = lst[len(lst)-1]
    for i in lst[:-1]:
        if i == target:
            return False
    return True

def computeCost(lst, currCost):
    G = sqrt(pow(lst[len(lst)-1][0] - lst[len(lst)-2][0], 2) + pow(lst[len(lst)-1][1] - lst[len(lst)-2][1], 2))
    H = sqrt(pow(lst[len(lst)-1][0] - destPoint[0], 2) + pow(lst[len(lst)-1][1] - destPoint[1], 2))
    lst.append([G+currCost[0], H]) 

def reset(event):
    global count
    count = 0
    openPaths.clear()
    uniqueCheck.clear()
    for i in range(maxRows):
        for j in range(maxCols):
            arr[i][j].configure(bg = 'grey')
    root.title('SELECT A STARTING POINT')

def findPath(event):
    x = startingPoint[0]
    y = startingPoint[1]
    targetPoint = [[x,y], [0,0]]
    while True:
        costAtTp = targetPoint.pop()
        if y != 0:
            if arr[y-1][x].cget('bg') != 'red':
                tmp = []
                tmp.extend(targetPoint)
                tmp.append([x, y-1])
                if checkRep(tmp):
                    computeCost(tmp, costAtTp)
                    if checkRepInNp(tmp):
                        openPaths.append(tmp)
            if arr[y-1][x+1].cget('bg') != 'red' and x != maxCols - 1:
                tmp = []
                tmp.extend(targetPoint)
                tmp.append([x+1, y-1])
                if checkRep(tmp):
                    computeCost(tmp, costAtTp)
                    if checkRepInNp(tmp):
                        openPaths.append(tmp)
            if arr[y-1][x-1].cget('bg') != 'red' and x != 0:
                tmp = []
                tmp.extend(targetPoint)
                tmp.append([x-1, y-1])
                if checkRep(tmp):
                    computeCost(tmp, costAtTp)
                    if checkRepInNp(tmp):
                        openPaths.append(tmp)
        if y != maxRows - 1:
            if arr[y+1][x].cget('bg') != 'red':
                tmp = []
                tmp.extend(targetPoint)
                tmp.append([x, y+1])
                if checkRep(tmp):
                    computeCost(tmp, costAtTp)
                    if checkRepInNp(tmp):
                        openPaths.append(tmp)
            if arr[y+1][x+1].cget('bg') != 'red' and x != maxCols - 1:
                tmp = []
                tmp.extend(targetPoint)
                tmp.append([x+1, y+1])
                if checkRep(tmp):
                    computeCost(tmp, costAtTp)
                    if checkRepInNp(tmp):
                        openPaths.append(tmp)
            if arr[y+1][x-1].cget('bg') != 'red' and x != 0:
                tmp = []
                tmp.extend(targetPoint)
                tmp.append([x-1, y+1])
                if checkRep(tmp):
                    computeCost(tmp, costAtTp)  
                    if checkRepInNp(tmp):
                        openPaths.append(tmp)
        if arr[y][x+1].cget('bg') != 'red' and x != maxCols - 1:
            tmp = []
            tmp.extend(targetPoint)
            tmp.append([x+1, y])
            if checkRep(tmp):
                computeCost(tmp, costAtTp)
                if checkRepInNp(tmp):
                    openPaths.append(tmp)
        if arr[y][x-1].cget('bg') != 'red' and x != 0:
            tmp = []
            tmp.extend(targetPoint)
            tmp.append([x-1, y])
            if checkRep(tmp):
                computeCost(tmp, costAtTp)
                if checkRepInNp(tmp):
                    openPaths.append(tmp)
        
        minVal = float('inf')
        indexes = []
        for ind, item in enumerate(openPaths):    
            cost = item[len(item)-1]
            fVal = cost[0] + cost[1]
            if fVal < minVal:
                minVal = fVal
                indexes.clear()
                indexes.append([ind, cost[1]])
            elif fVal == minVal:
                indexes.append([ind, cost[1]])
        minH = float('inf')
        index = -1
        for i in indexes:
            if i[1] < minH:
                minH = i[1]
                index = i[0]
        x = openPaths[index][len(openPaths[index])-2][0]
        y = openPaths[index][len(openPaths[index])-2][1]
        targetPoint.clear()
        targetPoint.extend(openPaths[index])
        print(targetPoint)
        del openPaths[index]
        if x == destPoint[0] and y == destPoint[1]:
            break
    for i in targetPoint[:-1]:
        arr[i[1]][i[0]].configure(bg = 'black')
    root.title('ENTER TO RESET')
    root.bind('<Return>', reset)

def onClick(row, col):
    global count
    count += 1
    if count == 1:
        arr[row][col].configure(bg = 'blue')
        global startingPoint
        startingPoint = [col, row]
        root.title('SELECT A DESTINATION')
    elif count == 2:
        arr[row][col].configure(bg = 'purple')
        global destPoint
        destPoint = [col, row]
        root.title('SELECT OBSTACLES AND PRESS ENTER')
    else:
        arr[row][col].configure(bg = 'red')
        if count == 3:
            root.bind('<Return>', findPath)
            
root = Tk()
# root.state('zoomed')
# maxHeight = root.winfo_screenheight()
# maxWidth = root.winfo_screenwidth()
maxRows = 20 # int(maxHeight / 28)
maxCols = 20 # int(maxWidth / 23)
arr = [[Button(root, bg = 'grey', height=1, width=2, command = lambda r = j, c = i: onClick(r, c)) for i in range(maxCols)] for j in range(maxRows)]
for i in range(maxRows):
    for j in range(maxCols):
        arr[i][j].grid(row = i, column = j)
root.title('SELECT A STARTING POINT')
root.mainloop()