from pyamaze import maze,agent
m=maze(4,4)
m.CreateMaze(loopPercent=50)
a=agent(m,shape='arrow',filled=True,footprints=True)
print(m.maze_map)
m.tracePath({a:m.path})
m.run()