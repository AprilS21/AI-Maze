#Uses pyamaze library https://github.com/MAN1986/pyamaze 
from pyamaze import maze,agent
from DFS import DFS
from BFS import BFS
from Astar import Astar
from mdp import value_iteration, convert_policy_to_path, policy_iteration
import time
import matplotlib.pyplot as plt

def main():
    m=maze(20,20)
    m.CreateMaze(loopPercent=50, theme='light')
    a=agent(m,shape='arrow',filled=True,footprints=True)
    start = time.time()
    path, cells_visited_DFS = DFS(m)
    end = time.time()
    print("DFS runtime: ", (end - start))
    DFSruntime = end - start
    print("DFS Length of path: ", len(path))
    DFSPathLength = len(path)
    m.tracePath({a:path})

    b=agent(m,shape='arrow',filled=True,footprints=True, color='red')
    start = time.time()
    path, cells_visited_BFS = BFS(m)
    end = time.time()
    print("BFS runtime: ", (end - start))
    BFSruntime = end - start
    print("BFS Length of path: ", len(path))
    BFSPathLength = len(path)
    m.tracePath({b:path})

    c=agent(m,shape='arrow',filled=True,footprints=True, color='green')
    start = time.time()
    path, cells_visited_Astar = Astar(m)
    end = time.time()
    print("Astar runtime: ", (end - start))
    Astarruntime = end - start
    print("Astar Length of path: ", len(path))
    AstarPathLength = len(path)
    m.tracePath({c:path})

    d=agent(m,shape='arrow',filled=True,footprints=True, color='yellow')
    start = time.time()
    policy1 = value_iteration(m, a)
    #print("converitng")
    policy1path = convert_policy_to_path(policy1, (m.rows, m.cols))
    end = time.time()
    print("MDP value iteration runtime: ", (end - start))
    valueruntime = end - start
    print("MDP value iteration Length of path: ", len(policy1path))
    ValuePathLength = len(policy1path)
    m.tracePath({d:policy1path})

    e=agent(m,shape='arrow',filled=True,footprints=True, color='black')
    start = time.time()
    policy2 = policy_iteration(m)
    print("converting")
    policy2path = convert_policy_to_path(policy2, (m.rows, m.cols))
    end = time.time()
    print("MDP policy iteration runtime: ", (end - start))
    policyruntime = end - start
    print("MDP policy iteration Length of path: ", len(policy2path))
    PolicyPathLength = len(policy2path)
    m.tracePath({e:policy2path})

    algorithms =["DFS", "BFS", "Astar", "value", "policy"]
    times =[DFSruntime, BFSruntime, Astarruntime, valueruntime, policyruntime]
    path_lengths =[DFSPathLength, BFSPathLength, AstarPathLength, ValuePathLength, PolicyPathLength]

    plt.plot(algorithms, times)
    plt.xlabel('algorithms')
    plt.ylabel('seconds')
    plt.title('runtime per algorithm')
    plt.show()

    plt.clf()
    plt.plot(algorithms, path_lengths)
    plt.xlabel('algorithms')
    plt.ylabel('length')
    plt.title('length of path found')
    plt.show()

    plt.clf()
    plt.plot([algorithms[0], algorithms[1], algorithms[2]], [cells_visited_DFS, cells_visited_BFS, cells_visited_Astar])
    plt.xlabel('algorithms')
    plt.ylabel('number')
    plt.title('numbers of cells visited (Search)')
    plt.show()

    plt.clf()
    plt.plot([algorithms[0], algorithms[1], algorithms[2]], [path_lengths[0], path_lengths[1], path_lengths[2]])
    plt.xlabel('algorithms')
    plt.ylabel('length')
    plt.title('Length of path found (Search)')
    plt.show()


    m.run()

main()