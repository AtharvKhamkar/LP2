g=0
def printboard(arr):
    for i in range(len(arr)):
        
        if(i %3 ==0):
            print()
        if(arr[i] == -1):
            print("_",end=" ")
        else :
            print(arr[i],end=" ")
def heuristic(start,goal):
    global g
    h=0
    for i in range(len(start)):
        for j in range(len(start)):
            if(start[i] == goal[j] and start[i] !=1):
                h += (abs(j-i)//3)+(abs(j-i)%3)
    return h+g

def moveleft(start,i):
    start[i-1],start[i]=start[i],start[i-1]
def moveright(start,i):
    start[i+1],start[i]=start[i],start[i+1]
def moveup(start,i):
    start[i-3],start[i] = start[i],start[i-3]
def movedown(start,i):
    start[i+3],start[i] = start[i],start[i+3]


def movetile(start,goal):
    emptyat = start.index(-1)
    row = emptyat//3
    col = emptyat%3
    t1,t2,t3,t4 = start[:],start[:],start[:],start[:]
    f1,f2,f3,f4 = 100,100,100,100
    
    if(col-1 > 0):
        moveleft(t1,emptyat)
        f1=heuristic(t1,emptyat)
    elif(col+1 < 3):
        moveright(t2,emptyat)
        f2 = heuristic(t2,emptyat)
    elif(row-1 > 0):
        moveup(t3,emptyat)
        f3 = heuristic(t3,emptyat)
    elif(row+1 < 3 ):
        movedown(t4,emptyat)
        f4 = heuristic(t4,emptyat)
    minf = min(f1,f2,f3,f4)
   
    if(f1 == minf):
        moveleft(start,emptyat)
    elif(f2 == minf):
        moveright(start,emptyat)
    elif(f3 == minf):
        moveup(start,emptyat)
    elif(f4 == minf):
        movedown(start,emptyat)
    
def solveright(start,goal):
    global g
    g +=1
    movetile(start,goal)
    printboard(start)
    f = heuristic(start,goal)
    if(f==g):
        print("solve in {} steps :".format(f))
        return
    solveright(start,goal)
def main():
    start =list()
    goal = list()
    n  = int(input("Enter number of elemets in start and goal state : "))
    for i in range(n):
        k = int(input("Enter element : "))
        start.append(k)
    print("Enter goal state :")
    for i in range(n):
        m = int(input("Enter element :"))
    printboard(start)
    printboard(goal)
    solveright(start,goal)
    
if __name__ == '__main__':
     main()