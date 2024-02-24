from pyamaze import maze,agent
from DFS import DFS
from BFS import BFS
from Astar import Astar
def main():
    m=maze(10,10)
    m.CreateMaze(loopPercent=50)
    a=agent(m,shape='arrow',filled=True,footprints=True)
    path = DFS(m)
    m.tracePath({a:path})

    b=agent(m,shape='arrow',filled=True,footprints=True, color='red')
    path = BFS(m)
    m.tracePath({b:path})

    c=agent(m,shape='arrow',filled=True,footprints=True, color='green')
    path = Astar(m)
    m.tracePath({c:path})


    m.run()

main()