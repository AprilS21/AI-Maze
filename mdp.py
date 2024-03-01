from pyamaze import maze,agent

def value_iteration(maze, agent):
   goal_state = (1, 1)
   map = maze.maze_map
   states = list(maze.maze_map.keys())
   states.reverse()
   actions = ['N', 'S', 'E', 'W']
   gamma = 0.9  # Discount 
   epsilon = 0.01  # Convergence criterion
   values = {state: 0 for state in states}

   iterations =0

   path = {}

   value_changed = True
   while True:
       value_changed = False
       delta =0
       for state in states:
           v = values[state]
           max_val = float('-inf')
           #print("STATE ", state)
           for action in actions:
               next_state, transition_prob = get_next_state(map, state, action)
               reward = get_reward(state, next_state, goal_state)
               max_val = max(max_val, transition_prob * (reward + gamma * values[next_state]))
               #print("max val ", max_val)
           values[state] = max_val
           delta = max(delta, abs(v - values[state]))
       if delta < epsilon:
            break
       iterations = iterations + 1

   #print(values)
   print("iterations ", iterations)

   optimal_policy = {}
   for state in states:
            if state not in values:
                continue
            max_value = float('-inf')
            best_action = None
            for action in actions:
                next_state, transition_prob = get_next_state(map, state, action)
                reward = get_reward(state, action, goal_state)
                if next_state:
                    value = transition_prob * (reward + gamma * values[next_state])
                    if value > max_value:
                        max_value = value
                        best_action = action
            optimal_policy[state] = best_action
   #print(optimal_policy)
   return optimal_policy
           

def get_reward(state, next_state, goal):
    if next_state == goal:
        return 10  # Higher reward for reaching the goal state
    elif next_state != state:
        return 1
    else:
        return -1  # Default reward for hitting a wall or going out of bounds
       
def get_next_state(maze, state, action):
    x, y = state
    next_state = None
    #print(state)
    #print(action)
    if action == 'N':
        #print("here")
        if maze[(x,y)]['N'] == 1:
            next_state = (x-1, y)
            #print("return ", next_state)
            return next_state, 1
    elif action == 'S':
        if maze[(x,y)]['S'] == 1:
                next_state = (x+1, y )
                #print("return ", next_state)
                return next_state, 1
    elif action == 'E':
        if maze[(x,y)]['E'] == 1:
                next_state = (x, y+1)
                #print("return ", next_state)
                return next_state, 1
    elif action == 'W':
        if maze[(x,y)]['W'] == 1:
                next_state = (x, y-1)
                #print("return ", next_state)
                return next_state, 1
    next_state = state
    #print("return ", next_state)
    return next_state, 0

def policy_evaluation(policy, vals, states, maze):
        goal = (1,1)
        gamma = 0.9  # Discount 
        epsilon = 0.01  # Convergence criterion
        values = {state: 0 for state in states}
        while True:
            delta = 0
            for state in states:
                if state not in values:
                    continue
                v = values[state]
                action = policy[state]
                next_state, transition_prob = get_next_state(maze, state, action)
                reward = get_reward(state, next_state, goal)
                if next_state:
                    values[state] = transition_prob * (reward + gamma * values[next_state])
                delta = max(delta, abs(v - values[state]))
            if delta < epsilon:
                break
        return values
    
def get_best_policy_policy(values, states, actions, maze):
        policy = {}
        goal =(1,1)
        gamma = 0.9  # Discount 
        epsilon = 0.01  # Convergence criterion
        for state in states:
            if state not in values:
                continue
            max_value = float('-inf')
            best_action = None
            for action in actions:
                next_state, transition_prob = get_next_state(maze, state, action)
                reward = get_reward(state, action, goal)
                if next_state:
                    value = transition_prob * (reward + gamma * values[next_state])
                    if value > max_value:
                        max_value = value
                        best_action = action
            policy[state] = best_action
        return policy

    
def policy_iteration(maze):
        goal_state = (1, 1)
        map = maze.maze_map
        states = list(maze.maze_map.keys())
        states.reverse()
        actions = ['N', 'S', 'E', 'W']
        gamma = 0.9  # Discount 
        epsilon = 0.01  # Convergence criterion
        values = {state: 0 for state in states}

        iterations =0
        policy = {state: 'N' for state in states}  # Initialize with arbitrary policy
        while True:
            values = policy_evaluation(policy, values, states, map)
            new_policy = get_best_policy_policy(values, states, actions, map)
            if new_policy == policy:
                break
            policy = new_policy
            iterations+= 1
        #print(values)
        #print(policy)
        print("iteration ", iterations)
        return policy
        
def convert_policy_to_path(policy, start_state):
     path = {}
     goal = (1,1)
     state = start_state
     while True:
          if state == goal:
               break
          action = policy[state]
          x,y = state
          if action == 'N':
               path[state] = (x-1, y)
               state = (x-1, y)
          if action == 'S':
               path[state] = (x+1, y)
               state = (x+1, y)
          if action == 'W':
               path[state] = (x, y-1)
               state = (x, y-1)
          if action == 'E':
               path[state] = (x, y+1)
               state = (x, y+1)
     return path
               

def main():
    m = maze(40,40)
    m.CreateMaze(loopPercent=100)
    a = agent(m, footprints=True, shape='arrow')
    b = agent(m, footprints=True, shape='arrow', color='red')
    goal_state = (1, 1)
    #print(m.maze_map)
    #print(list(m.maze_map.keys()))
    policy1 = value_iteration(m, a)
    policy1path = convert_policy_to_path(policy1, (m.rows, m.cols))
    policy2 = policy_iteration(m)
    policy2path = convert_policy_to_path(policy2, (m.rows, m.cols))
    m.tracePath({a:policy1path})
    m.tracePath({b:policy2path})
    m.run()

#main()