import numpy as np
from pyamaze import maze,agent

class MazeMDP:
    def __init__(self, m, maze, goal_state,a):
        self.m = m
        self.maze = maze
        self.states = list(self.maze.keys())
        self.actions = ['N', 'S', 'E', 'W']
        self.gamma = 0.9  # Discount factor
        self.epsilon = 1e-6  # Convergence criterion
        self.values = {state: 0 for state in self.states}
        self.goal_state = goal_state
        self.agent =a
        
    def get_transition_prob(self, state, action):
        next_state = self._get_next_state(state, action)
        return 1 if next_state else 0
    
    def get_reward(self, state, action):
        next_state = self._get_next_state(state, action)
        if next_state == self.goal_state:
            return 10  # Higher reward for reaching the goal state
        elif next_state:
            return self.maze[next_state][action]
        else:
            return -1  # Default reward for hitting a wall or going out of bounds
    
    def _get_next_state(self, state, action):
        x, y = state
        next_state = None
        if action == 'N':
            if self.maze[(x,y)]['N'] == 1:
                next_state = (x, y + 1)
        elif action == 'S':
            if self.maze[(x,y)]['S'] == 1:
                next_state = (x, y - 1)
        elif action == 'E':
            if self.maze[(x,y)]['E'] == 1:
                next_state = (x + 1, y)
        elif action == 'W':
            if self.maze[(x,y)]['W'] == 1:
                next_state = (x - 1, y)
        else:
            next_state = self.move(state)
        return next_state if next_state in self.states else None
    
    def value_iteration(self):
        path = {}
        while True:
            delta = 0
            for state in self.states:
                if state not in self.values:
                    continue
                v = self.values[state]
                max_value = float('-inf')
                for action in self.actions:
                    transition_prob = self.get_transition_prob(state, action)
                    reward = self.get_reward(state, action)
                    next_state = self._get_next_state(state, action)
                    path[state] = next_state
                    if next_state:
                        max_value = max(max_value, transition_prob * (reward + self.gamma * self.values[next_state]))
                self.values[state] = max_value
                delta = max(delta, abs(v - self.values[state]))
            if delta < self.epsilon:
                break
        print(path)
        self.m.tracePath({self.agent:path})
        self.m.run()
        print("here2")
    
    def possible_moves(self, state):
        x, y = state
        if self.maze[(x,y)]['W'] == 1:
            return 'W'
        elif self.maze[(x,y)]['N'] == 1:
            return 'N'
        elif self.maze[(x,y)]['S'] == 1:
            return 'S'
        elif self.maze[(x,y)]['E'] == 1:
            return 'E'
        
    def move (self, state):
        x, y = state
        if self.maze[(x,y)]['W'] == 1:
            next_state = (x - 1, y)
        elif self.maze[(x,y)]['N'] == 1:
            next_state = (x , y-1)
        elif self.maze[(x,y)]['S'] == 1:
            next_state = (x , y + 1)
        elif self.maze[(x,y)]['E'] == 1:
            next_state = (x +1, y)
        return next_state

    def value_iteration2(self):
            path = {}
            while True:
                delta =  0
                for state in self.states:
                    if state not in self.values:
                        continue
                    v = self.values[state]
                    max_value = float('-inf')
                    best_action = None
                    for action in self.actions:
                        transition_prob = self.get_transition_prob(state, action)
                        reward = self.get_reward(state, action)
                        next_state = self._get_next_state(state, action)
                        if next_state:
                            value = transition_prob * (reward + self.gamma * self.values[next_state])
                            if value > max_value:
                                max_value = value
                                best_action = self.possible_moves(state)
                                print("best action ", best_action)
                    self.values[state] = max_value
                    delta = max(delta, abs(v - self.values[state]))
                    # Force a move if the current state is not the goal state
                    if state != self.goal_state:
                        path[state] = self._get_next_state(state, best_action)
                print(path)
                self.m.tracePath({self.agent:path})
                self.m.run()
                print("here2")
                if delta < self.epsilon:
                    break

    
    def get_optimal_policy(self):
        optimal_policy = {}
        for state in self.states:
            if state not in self.values:
                continue
            max_value = float('-inf')
            best_action = None
            for action in self.actions:
                transition_prob = self.get_transition_prob(state, action)
                reward = self.get_reward(state, action)
                next_state = self._get_next_state(state, action)
                if next_state:
                    value = transition_prob * (reward + self.gamma * self.values[next_state])
                    if value > max_value:
                        max_value = value
                        best_action = action
            optimal_policy[state] = best_action
        return optimal_policy


def main():
    m = maze(5,5)
    m.CreateMaze(loopPercent=50)
    a = agent(m, footprints=True, shape='arrow')
    goal_state = (1, 1)

    maze_mdp = MazeMDP(m, m.maze_map, goal_state, a)
    maze_mdp.value_iteration2()
    optimal_policy = maze_mdp.get_optimal_policy()
    for state, action in optimal_policy.items():
        print(f'State: {state}, Action: {action}')

main()
