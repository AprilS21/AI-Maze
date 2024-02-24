# Code based on https://www.youtube.com/watch?v=sTRK9mQgYuc 

from pyamaze import maze,agent

def DFS(maze):
    startCell = (maze.rows, maze.cols) # set starting cell to bottom right of the maze
    visited = [startCell]
    frontier = [startCell]
    goal = (1,1)
    mapMaze = maze.maze_map
    path = {}

    
    while len(frontier) >0: #while frontier is not empty
        currentCell = frontier.pop()
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
                if childCell not in visited:
                    visited.append(childCell)
                    frontier.append(childCell)
                    path[childCell] = currentCell #stores reverse path
    finalPath = {}
    cell = goal
    while cell != startCell:
        finalPath[path[cell]] = cell
        cell = path[cell]

    return finalPath
# dfs does not necessarily give the shortest path
def main():
    m = maze(10,10)
    m.CreateMaze(loopPercent=100)
    path = DFS(m)
    a = agent(m, footprints=True, shape='arrow')
    m.tracePath({a:path})
    m.run()

main()