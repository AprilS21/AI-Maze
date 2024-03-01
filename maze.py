from pyamaze import maze,agent
from DFS import DFS
from BFS import BFS
from Astar import Astar
from mdp import value_iteration, convert_policy_to_path, policy_iteration
import time

def main():
    m=maze(40,40)
    m.CreateMaze(loopPercent=50, theme='light')
    a=agent(m,shape='arrow',filled=True,footprints=True)
    start = time.time()
    path = DFS(m)
    end = time.time()
    print("DFS runtime: ", (end - start))
    m.tracePath({a:path})

    b=agent(m,shape='arrow',filled=True,footprints=True, color='red')
    start = time.time()
    path = BFS(m)
    end = time.time()
    print("BFS runtime: ", (end - start))
    m.tracePath({b:path})

    c=agent(m,shape='arrow',filled=True,footprints=True, color='green')
    start = time.time()
    path = Astar(m)
    end = time.time()
    print("Astar runtime: ", (end - start))
    m.tracePath({c:path})

    d=agent(m,shape='arrow',filled=True,footprints=True, color='yellow')
    start = time.time()
    policy1 = value_iteration(m, a)
    policy1path = convert_policy_to_path(policy1, (m.rows, m.cols))
    end = time.time()
    print("MDP value iteration runtime: ", (end - start))
    m.tracePath({d:policy1path})

    e=agent(m,shape='arrow',filled=True,footprints=True, color='black')
    start = time.time()
    policy2 = policy_iteration(m)
    policy2path = convert_policy_to_path(policy2, (m.rows, m.cols))
    end = time.time()
    print("MDP policy iteration runtime: ", (end - start))
    m.tracePath({e:policy2path})



    m.run()

main()