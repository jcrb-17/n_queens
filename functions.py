from classes import *
import random
import itertools
import time
import multiprocessing
from multiprocessing import Process,Manager
from ast import literal_eval

def createBoxes(boxesWidthHeight,boardSatisfy,dimensions,offsetX=0,offsetY=0,):
    arr = []
    if dimensions % 2 == 0:
        for i in range(dimensions):
            for j in range(dimensions):
                if (i+j) %2 == 0:
                    colorBg = (72,50,33)
                elif (i+j) %2 != 0:
                    colorBg = (186,186,186)
                box = Box(boardSatisfy[i][j],(i*boxesWidthHeight)+offsetX, (j*boxesWidthHeight)+offsetY, boxesWidthHeight,colorBg)
                arr.append(box)

    else:
        for i in range(dimensions):
            for j in range(dimensions):
                if (i+j) %2 == 0:
                    colorBg = (72,50,33)
                elif (i+j) %2 != 0:
                    colorBg = (186,186,186)
                box = Box(boardSatisfy[i][j],(i*boxesWidthHeight)+offsetX, (j*boxesWidthHeight)+offsetY, boxesWidthHeight,colorBg)
                arr.append(box)
    return arr
def drawBoxes(arrBoxes,screen,img):
    for i in arrBoxes:
        i.draw(screen,img)

#---

def createArray(n):
    arr = []
    for i in range(n):
        arr2 = [0] * n
        arr.append(arr2)
    # arr[0][1] = 2
    # print(arr)
    return arr

#creates a random matrix, only a 1 is in a column and in a row
def createGrid(n):
    grid = createArray(n)

    #to keep track of wheter that position has been already used
    positions = []

    #it places n-1 queens, because placing n queens gets a collision
    for i in range(len(grid)-1):
        guess = random.randint(0,n-1)

        while guess in positions:
            guess = random.randint(0,n-1)

        grid[i][guess] = 1
        positions.append(guess)
    """
    for i in grid:
        print(i)
    """
    return grid

#given an n*n grid it tells wheter there is a conflict
#it detects diagonal collisions
#it detects if 2 queens collide
def verify(grid):
    #the grid contains the size n*n

    #it prints the first n upper diagonals
    for i in range(len(grid)):
        flag = 0
        for j in range(i+1):
            if i == 0 and j == 0:
                continue
            if flag == 0 and grid[j][i-j] == 1:
                flag = 1
            elif flag == 1 and grid[j][i-j] == 1:
                return
            #print("i",i,"j",j," = ",grid[j][i-j])
        #print()

    #it prints the down n-1 down diagonals
    aux = 0
    for i in range(len(grid)-1,0,-1):
        aux += 1
        flag = 0
        for j in range(i,0,-1):
            if i == 1 and j == 1:
                continue
            if flag == 0 and grid[i-j+aux][j+aux-1] == 1:
                flag = 1
            elif flag == 1 and grid[i-j+aux][j+aux-1] == 1:
                return
            #print("i",i,"j",j,"i-j+aux",i-j+aux,"j+aux-1",j+aux-1," = ",grid[i-j+aux][j+aux-1])
        #print()

    #it prints the first n diagonals, from left to right
    aux = len(grid)+1
    for i in range(len(grid)+1):
        aux -= 1
        flag = 0
        for j in range(i,0,-1):
            if i == 1 and j == 1:
                continue
            if flag == 0 and grid[i-j][i-j+aux] == 1:
                flag = 1
            elif flag == 1 and grid[i-j][i-j+aux] == 1:
                return
            #print("i",i,"j",j,"i-j+aux",i-j+aux,"aux ",aux,"i-j",i-j, " = ",grid[i-j][i-j+aux], " ---",i-j,i-j+aux)
        #print()

    #prints the other diagonal
    aux = 0
    for i in range(len(grid)-1,-1,-1):
        aux += 1
        aux2 = 0
        flag = 0
        for j in range(i,0,-1):
            if i == 1 and j == 1:
                continue
            if flag == 0 and grid[i-j+aux][aux2]== 1:
                flag = 1
            elif flag == 1 and grid[i-j+aux][aux2] == 1:
                return
            #print(i-j+aux,aux2,grid[i-j+aux][aux2],i,j)
            aux2 += 1
        #print()
    #print(grid)
    return grid

#given various grids it verifies them
def verify2(grids,L):
    for i in grids:
        if verify(i) == None:
            continue
        else:
            L.append(i)

def writeFile(data):
    with open('data', 'w') as f:
        f.write(str(data))

def readFile():
    with open('data', 'r') as f:
        x = f.read()

        #converts to array
        return literal_eval(x)
def begin(n,num_processors):
    #try:
    if n > 10 and n <= 15:
        with Manager() as manager:
            L = manager.list()
            A = createGrid(n)
            start = time.time()
            counter = -1
            perm = [0]*100001
            for i in itertools.permutations(A):
                #print(counter)
                counter += 1
                if counter >100000-1:
                    break
                perm[counter] = i
            process1 = Process(target=verify2, args=(perm[0:10000],L))
            process2 = Process(target=verify2, args=(perm[10000:20000],L))
            process3 = Process(target=verify2, args=(perm[20000:30000],L))
            process4 = Process(target=verify2, args=(perm[30000:40000],L))
            process5 = Process(target=verify2, args=(perm[40000:50000],L))
            process6 = Process(target=verify2, args=(perm[50000:60000],L))
            process7 = Process(target=verify2, args=(perm[60000:70000],L))
            process8 = Process(target=verify2, args=(perm[70000:80000],L))
            process9 = Process(target=verify2, args=(perm[80000:90000],L))
            process10 = Process(target=verify2, args=(perm[90000:100000],L))

            process1.start()
            process2.start()
            process3.start()
            process4.start()
            process5.start()
            process6.start()
            process7.start()
            process8.start()
            process9.start()
            process10.start()

            process1.join()
            process2.join()
            process3.join()
            process4.join()
            process5.join()
            process6.join()
            process7.join()
            process8.join()
            process9.join()
            process10.join()
            writeFile(L)
        #print("ellapsed",time.time()-start)
        return readFile(),time.time()-start
    elif n > 15:
        with Manager() as manager:
            L = manager.list()
            A = createGrid(n)
            start = time.time()
            counter = -1
            perm = [0]*10000001
            for i in itertools.permutations(A):
                #print(counter)
                counter += 1
                if counter >10000000-1:
                    break
                perm[counter] = i
            process1 = Process(target=verify2, args=(perm[0:1000000],L))
            process2 = Process(target=verify2, args=(perm[1000000:2000000],L))
            process3 = Process(target=verify2, args=(perm[2000000:3000000],L))
            process4 = Process(target=verify2, args=(perm[3000000:4000000],L))
            process5 = Process(target=verify2, args=(perm[4000000:5000000],L))
            process6 = Process(target=verify2, args=(perm[5000000:6000000],L))
            process7 = Process(target=verify2, args=(perm[6000000:7000000],L))
            process8 = Process(target=verify2, args=(perm[7000000:8000000],L))
            process9 = Process(target=verify2, args=(perm[8000000:9000000],L))
            process10 = Process(target=verify2, args=(perm[9000000:10000000],L))

            process1.start()
            process2.start()
            process3.start()
            process4.start()
            process5.start()
            process6.start()
            process7.start()
            process8.start()
            process9.start()
            process10.start()

            process1.join()
            process2.join()
            process3.join()
            process4.join()
            process5.join()
            process6.join()
            process7.join()
            process8.join()
            process9.join()
            process10.join()
            writeFile(L)
        #print("ellapsed",time.time()-start)
        return readFile(),time.time()-start
    elif n <= 10:
        if n<1 or num_processors<1 or str.isdigit(str(num_processors)) == False or str.isdigit(str(n)) == False:
            return False

        A = createGrid(n)
        start = time.time()

        pool = multiprocessing.Pool(processes=num_processors)
        pool_outputs = pool.map(verify, itertools.permutations(A))
        #print(len(pool_outputs))
        arr = []

        for i in pool_outputs:
            if i != None:
                arr.append(i)
        pool.close()
        pool.join()

        #print(arr)
        #print("ellapsed",time.time()-start)
        return arr,time.time()-start

#except:
#    return False,False

#print(begin(11,3))
