# Code based on https://www.youtube.com/watch?v=W9zSr9jnoqY 

# heuristic is the manhattan distance which is horizontal + vertical distance. 
# Shortest path other than eucilidean distance but cannot move diagonal so not relevant

from pyamaze import maze,agent
from queue import PriorityQueue
def heuristic(cell1, cell2):
    x1,y1 = cell1
    x2,y2 = cell2
    
    z = abs(x1-x2) + abs(y1-y2)
    return z

def Astar(maze):
    goal = (1,1)
    mapMaze = maze.maze_map
    startCell = (maze.rows, maze.cols) # set starting cell to bottom right of the maze
    g_score = {cell:float('inf') for cell in maze.grid}
    g_score[startCell] = 0
    f_score = {cell:float('inf') for cell in maze.grid}
    f_score[startCell] = heuristic(startCell, goal) + 0
    
    queue = PriorityQueue()
    queue.put((f_score[startCell], heuristic(startCell, goal), startCell))
    path = {}
    cells_visited =0

    while not queue.empty():
        currentCell = queue.get()[2]
        cells_visited +=1
        if currentCell == goal:
            break
        for direction in 'ESNW':
            if mapMaze[currentCell][direction] == 1:
                if direction == 'E':
                    childCell = (currentCell[0], currentCell[1] +1) #move cell to the right
                elif direction == 'S':
                    childCell = (currentCell[0] +1, currentCell[1]) #move cell down
                elif direction == 'N':
                    childCell = (currentCell[0] -1, currentCell[1]) #move cell up
                elif direction == 'W':
                    childCell = (currentCell[0], currentCell[1] -1) #move cell to the left
                current_g_score = g_score[currentCell] +1
                current_f_score = current_g_score + heuristic(childCell, goal)

                if current_f_score < f_score[childCell]:
                    g_score[childCell] =  current_g_score
                    f_score[childCell] = current_f_score
                    queue.put((f_score[childCell], heuristic(childCell, goal), childCell))
                    path[childCell] = currentCell #stores reverse path
    finalPath = {}
    cell = goal
    while cell != startCell:
        finalPath[path[cell]] = cell
        cell = path[cell]
    
    print("Astar Cells visited: ", cells_visited)
    return finalPath, cells_visited

# Astar does give the shortest path
def main():
    m = maze(10,10)
    m.CreateMaze(loopPercent=100)
    path = Astar(m)
    a = agent(m, footprints=True, shape='arrow')
    m.tracePath({a:path})
    m.run()

#main()