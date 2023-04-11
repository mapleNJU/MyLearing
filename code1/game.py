
import numpy as np
from  config import config
from math import inf,floor
from queue import Queue
from copy import deepcopy
class Hole():
    def __init__(self, config, x, y):
        self.life = np.random.randint(config.min_life, config.max_life+1)
        self.score = np.random.randint(config.min_score, config.max_score+1)
        self.age = 0
        self.x = x
        self.y = y

#hole 1, obstacle -1, road 0
class Tile_map():
    def __init__(self, config):
        self.config = config
        self.length = config.map_length
        self.obstacle = config.obstacle
        self.hole_generation_time_min = config.min_generation_time
        self.hole_generation_time_max = config.max_generation_time
        self.hole_generation_time_next = 0
        self.hole = []
        self.agent_position_x = 6
        self.agent_position_y = 6
        self.score_sum = 0
        self.map = self.generate_map()
    def is_map_connected(self, world_map):
        row, col = np.where(world_map == 0)
        if len(row) == 0:
            return True
        start = (row[0], col[0])
        visited = set()
        queue = [start]
        while queue:
            row, col = queue.pop(0)
            if (row, col) not in visited:
                visited.add((row, col))
                if row > 0 and world_map[row-1, col] == 0:
                    queue.append((row-1, col))
                if row < world_map.shape[0]-1 and world_map[row+1, col] == 0:
                    queue.append((row+1, col))
                if col > 0 and world_map[row, col-1] == 0:
                    queue.append((row, col-1))
                if col < world_map.shape[1]-1 and world_map[row, col+1] == 0:
                    queue.append((row, col+1))
        row, col = np.where(world_map == 0)
        return len(row) == len(visited)
    def generate_map(self):
        world_map = np.zeros((config.map_length, config.map_length), dtype=int)
        for i in range(self.obstacle):
            while True:
                row = np.random.randint(config.map_length)
                col = np.random.randint(config.map_length)
                if world_map[row, col] == 0 and row!=6 and col!=6:
                    world_map[row, col] = -1
                    break
        while not self.is_map_connected(world_map):
            world_map = self.generate_map()
        return world_map
    def hole_same(self, x, y):
        for i in self.hole:
            if i.x == x and i.y == y:
                return True
        return False

    def hole_generate(self):
        x = np.random.randint(0, self.length)
        y = np.random.randint(0, self.length)
        while self.map[x][y]==-1 or self.hole_same(x,y):
            x = np.random.randint(0, self.length)
            y = np.random.randint(0, self.length)
        self.map[x][y] = 1
        self.hole.append(Hole(self.config, x, y))
        self.score_sum += self.hole[-1].score
        # print(self.score_sum)
        self.hole_generation_time_next = np.random.randint(self.hole_generation_time_min, self.hole_generation_time_max+1)
    
    def map_update(self, action):
        if action == 'up':
            self.agent_position_y += 1
        elif action == 'down':
            self.agent_position_y -= 1
        elif action == 'left':
            self.agent_position_x -= 1
        elif action == 'right':
            self.agent_position_x += 1
        t=len(self.hole)
        q=0
        while q<len(self.hole):
            item = self.hole[q]
            # print(q,item.age, item.life)
            if item.age >= item.life:
                self.map[item.x][item.y] = 0
                # print("yes")
                self.hole.remove(item)
            else:
                q+=1
        # for it in range(t):
        #     print(q,it.age, it.life)

        #     q+=1
        #     # print(item.age, item.life)
        #     if it.age == it.life:
        #         self.map[it.x][it.y] = 0
        #         # print("yes")
        #         self.hole.remove(it)
        temp_score = 0
        for item in self.hole:
            if item.x == self.agent_position_x and item.y == self.agent_position_y:
                # print("remov")
                self.map[item.x][item.y] = 0
                temp_score = deepcopy(item.score)
                self.hole.remove(item)
        if self.hole_generation_time_next == 0:
            # print("yes")
            self.hole_generate()
        else:
            self.hole_generation_time_next -= 1
        for item in self.hole:
            item.age += 1
        for item in self.hole:
            self.map[item.x][item.y] = 1
        
        return temp_score


class Node():
    def __init__(self, x, y, parent, last_action, distance):
        self.x = x
        self.y = y
        self.parent = parent
        self.last_action = last_action
        self.distance = distance
class Agent():
    def __init__(self, config, world):
        self.config = config
        self.k = config.k
        self.p = floor(config.p)+1
        self.score = 0
        self.target_hole = None
        self.actions = []
        self.step = 0
        self.env = world
        self.reaction_strategy = config.reaction_strategy
        self.holes_found = None
    def plan_action_need(self):
        if len(self.actions) == 0:
            # print("yes")
            return True
        if self.step >= self.k + self.p:
            # print("yes")
            return True
        if self.reaction_strategy != 'blind_commitment' and self.env.map[self.target_hole[0]][self.target_hole[1]]!=1:
            # print("yes")
            return True
        elif self.reaction_strategy == 'any_new_hole' and self.judge_new_hole():
            # print("yes1")
            return True
        elif self.reaction_strategy == 'nearer_hole' and self.judge_new_hole_and_distance():
            # print("yes2")
            return True
        return False
    def judge_new_hole(self):
        # print("yes1")
        for hole in self.env.hole:
            judge = False
            for found_hole in self.holes_found:
                if found_hole.x == hole.x and found_hole.y == hole.y:
                    judge = True
            if not judge:
                return True
        return False
    def judge_new_hole_and_distance(self):
        for hole in self.env.hole:
            judge = False
            for found_hole in self.holes_found:
                if found_hole.x == hole.x and found_hole.y == hole.y:
                    judge = True
            if not judge and abs(hole.x-self.env.agent_position_x)+abs(hole.y-self.env.agent_position_y)<abs(self.env.agent_position_x-self.target_hole[0])+abs(self.env.agent_position_y-self.target_hole[1]):
                return True
        return False
    def action_work(self):
        # print(self.actions)
        if self.plan_action_need():
            self.plan()
        if len(self.actions) == 0:
            return 'stop'
        if self.step<self.p:
            self.step+=1
            return 'stop'
        else:
            self.step+=1
            action=self.actions.pop(0)
            return action
    def plan(self):
        if(len(self.env.hole)==0):
            return
        self.step = 0
        self.holes_found = deepcopy(self.env.hole)
        self.target_hole, self.actions = self.target_select()
    def get_score(self, temp_score):
        self.score += temp_score

    def target_select(self):
        world_map = deepcopy(self.env.map) #-2 already searched
        world_map[self.env.agent_position_x][self.env.agent_position_y] = -2
        start = Node(self.env.agent_position_x, self.env.agent_position_y, None, None, 0)
        node_list = Queue()
        node_list.put(start)
        hole_list = []
        action_list = ['right','left','up','down']
        while not node_list.empty():
            temp_node = node_list.get()
            i = 0
            for x_move, y_move in [(1,0),(-1,0),(0,1),(0,-1)]:
                now_x = temp_node.x + x_move
                now_y = temp_node.y + y_move
                if now_x>=0 and now_y>=0 and now_x<self.env.length and now_y<self.env.length and world_map[now_x][now_y]!=-2 and world_map[now_x][now_y]!=-1:
                    node_list.put(Node(now_x, now_y, temp_node, action_list[i], temp_node.distance+1))
                    if world_map[now_x][now_y] == 1:
                        hole_list.append(Node(now_x, now_y, temp_node, action_list[i], temp_node.distance+1))
                    world_map[now_x][now_y] = -2
                i += 1
        action = []
        max_score = -inf
        target_hole = None
        for i in hole_list:
            temp_action = []
            distance = i.distance
            temp_action.append(i.last_action)
            t=i
            while t.last_action!=None:
                t = t.parent
                if t.last_action!=None:
                    temp_action.append(t.last_action)
            temp_score = self.calculate_score(distance, i.x, i.y)
            if temp_score>max_score:
                max_score = temp_score
                target_hole = (i.x, i.y)
                temp_action.reverse()
                action = temp_action
        return target_hole, action
    def calculate_score_type(self, distance, x, y):
        for i in self.env.hole:
            if i.x == x and i.y == y:
                score = self.config.age_influence * i.age + self.config.distance_influence * distance + self.config.score_influence * i.score
                return score
    def calculate_score(self, distance, x, y):
        for i in self.env.hole:
            if i.x == x and i.y == y:
                score = i.score/distance
                return score
            


    

