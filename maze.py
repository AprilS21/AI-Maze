from pyamaze import maze,agent
from DFS import DFS
from BFS import BFS
from Astar import Astar
from mdp import value_iteration, convert_policy_to_path, policy_iteration
def main():
    m=maze(40,40)
    m.CreateMaze(loopPercent=50, theme='light')
    a=agent(m,shape='arrow',filled=True,footprints=True)
    path = DFS(m)
    m.tracePath({a:path})

    b=agent(m,shape='arrow',filled=True,footprints=True, color='red')
    path = BFS(m)
    m.tracePath({b:path})

    c=agent(m,shape='arrow',filled=True,footprints=True, color='green')
    path = Astar(m)
    m.tracePath({c:path})

    d=agent(m,shape='arrow',filled=True,footprints=True, color='yellow')
    policy1 = value_iteration(m, a)
    policy1path = convert_policy_to_path(policy1, (m.rows, m.cols))
    m.tracePath({d:policy1path})

    e=agent(m,shape='arrow',filled=True,footprints=True, color='black')
    policy2 = policy_iteration(m)
    policy2path = convert_policy_to_path(policy2, (m.rows, m.cols))
    m.tracePath({e:policy2path})



    m.run()

main()