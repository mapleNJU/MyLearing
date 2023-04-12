from matplotlib import pyplot as plt
import numpy as np
from enum import Enum
import math


class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    STOP = 4


class Config:
    def __init__(self):
        self.size = 15
        self.l_min = 240  #最小洞寿命
        self.l_max = 960  #最大洞寿命
        self.g_min = 60  #最小孕育周期
        self.g_max = 240  #最大孕育周期
        self.game_length = 3000
        self.score_min = 1  #最小分数
        self.score_max = 10  #最大分数
        self.u_dis = 10
        self.u_score = 10
        self.u_age = -1


class Hole:
    def __init__(self, gamma, config: Config, env):
        while True:
            x = np.random.randint(0, env.size - 1)
            y = np.random.randint(0, env.size - 1)
            if (x, y) not in env.holes:
                self.position = (x, y)
                break

        self.config = Config()
        self.life_expectancy = 0
        self.score = 0
        self.age = 0
        self.life_expectancy = np.random.uniform(self.config.l_min / gamma,
                                                 self.config.l_max / gamma)
        self.score = np.random.uniform(self.config.score_min,
                                       self.config.score_max)

    def get_position(self):
        return self.position


config = Config()


class Agent:
    def __init__(self, k, p, config: Config, reaction_strategy='blind'):
        self.k = math.floor(k)  #返回其下舍整数
        self.p = math.floor(p)

        self.config = Config()
        self.score = 0
        self.steps_after_plan = 0
        self.position = [0, 0]
        self.action_to_do = []
        self.target = None
        self.last_holes = None
        self.reaction_strategy = reaction_strategy

    def get_action(self, env):
        if self.steps_after_plan % (self.k + self.p) == 0 or len(
                self.action_to_do) == 0:
            self.plan(env)

        if self.reaction_strategy != 'blind' and self.target and self.target not in env.holes:
            if self.reaction_strategy == 'disappear':
                self.plan(env)
            elif self.reaction_strategy == 'any_appear':
                for hole in env.holes:
                    if hole not in self.last_holes:
                        self.plan(env)
                        break
            elif self.reaction_strategy == 'near_appear':
                for hole in env.holes:
                    if hole not in self.last_holes and \
                            abs(hole[0] - self.position[0]) + abs(hole[1] - self.position[1]) < \
                            abs(self.target[0] - self.position[0]) + abs(self.target[1] - self.position[1]):
                        self.plan(env)
                        break
        else:
            if self.steps_after_plan < self.p:
                self.steps_after_plan += 1
                return Action.STOP
            elif self.steps_after_plan < self.p + self.k:
                if len(self.action_to_do) > 0:
                    self.steps_after_plan += 1
                    return self.action_to_do.pop(0)
                else:
                    return Action.STOP
            else:
                return Action.STOP
        return Action.STOP

    def plan(self, env):
        self.steps_after_plan = 0
        self.action_to_do = []
        self.last_holes = env.holes.copy()

        target_hole = self.plan_selection(env)
        if target_hole:
            self.target = target_hole.position
            target_x, target_y = target_hole.position
            agent_x, agent_y = self.position
            if agent_x >= target_x:
                self.action_to_do.extend([Action.LEFT] * (agent_x - target_x))
            else:
                self.action_to_do.extend([Action.RIGHT] * (target_x - agent_x))

            if agent_y >= target_y:
                self.action_to_do.extend([Action.UP] * (agent_y - target_y))
            else:
                self.action_to_do.extend([Action.DOWN] * (target_y - agent_y))

    def plan_selection(self, env):
        max_score = 0
        max_hole = None
        for key in env.holes:
            hole = env.holes[key]
            hole_score = self.utility(hole)
            if hole_score > max_score:
                max_score = hole_score
                max_hole = hole
        return max_hole

    def utility(self, hole):
        distance = abs(self.position[0] - hole.position[0]) + abs(
            self.position[1] - hole.position[1])  #计算曼哈顿距离
        score = hole.score
        age = hole.age
        return self.config.u_dis * distance + self.config.u_score * score + self.config.u_age * age

    def get_effectiveness(self, env):
        if env.history_total_score == 0:
            return 0
        return self.score / env.history_total_score


class Tileworld:
    def __init__(self, gamma, config: Config):
        self.gamma = gamma
        self.size = config.size
        self.config = config
        self.holes = dict()
        self.obstacles = None
        self.time_after_gen_hole = 0
        self.gestation_period = 0
        self.history_total_score = 0
        self.gen_hole()

    def update(self, action, agent: Agent):
        self.interact(action, agent)
        new_position = tuple(agent.position)
        if new_position in self.holes.copy():
            hole_to_fill = self.holes[new_position]
            agent.score += hole_to_fill.score
            self.holes.pop(new_position)
            self.gen_hole()
        self.time_check()

    def interact(self, action, agent: Agent):
        if action == Action.UP:
            agent.position[1] = max(agent.position[1] - 1, 0)
        if action == Action.DOWN:
            agent.position[1] = min(agent.position[1] + 1, self.size - 1)
        if action == Action.LEFT:
            agent.position[0] = max(agent.position[0] - 1, 0)
        if action == Action.RIGHT:
            agent.position[0] = min(agent.position[0] + 1, self.size - 1)

    def time_check(self):
        for key in self.holes.copy():
            hole = self.holes[key]
            hole.age += 1
            if hole.age >= hole.life_expectancy:
                self.holes.pop(key)

        self.time_after_gen_hole += 1
        if self.time_after_gen_hole >= self.gestation_period:
            self.gen_hole()

    def gen_hole(self):
        new_hole = Hole(self.gamma, self.config, self)
        new_position = new_hole.get_position()
        self.holes[new_position] = new_hole
        self.gestation_period = np.random.uniform(
            self.config.g_min / self.gamma, self.config.g_max / self.gamma)
        self.time_after_gen_hole = 0
        self.history_total_score += new_hole.score

    def get_holes(self):
        return self.holes


def test(gamma, k, p, reaction):
    result = []
    for game in range(5):
        # seed = random.random()
        env = Tileworld(gamma, config)
        agent = Agent(k, p, config, reaction)
        for time_step in range(config.game_length):
            action = agent.get_action(env)
            env.update(action, agent)
        result.append(agent.get_effectiveness(env))
    return result


def ComputeScoreList(k, p, reaction='blind'):
    eff_list = []
    gamma_list = []
    lg10gamma_list = []
    for lg10gamma in np.linspace(0, 2, 15, endpoint=True):
        gamma = 10**lg10gamma

        lg10gamma_list.append(lg10gamma)
        gamma_list.append(gamma)

        eff = test(gamma, k, p, reaction)
        eff_list.append(np.mean(eff))

    return gamma_list, lg10gamma_list, eff_list


def test1():  #默认情况，k=4,p=1,正常策略
    gamma_list, lg10gamma_list, eff_list = ComputeScoreList(4, 1)

    plt.plot(gamma_list, eff_list, linestyle='-', marker='D')
    plt.grid()
    plt.xlabel(r'$\gamma$')
    plt.ylabel(r'$\epsilon$')
    plt.title('Effect of Rate of World Change')
    plt.savefig('figure1.png')
    plt.close()

    plt.plot(lg10gamma_list, eff_list, linestyle='-', marker='D')
    plt.grid()
    plt.xlabel(r'$\log_{10}\gamma$')
    plt.ylabel(r'$\epsilon$')
    plt.title(r'Effect of Rate of World Change ($\log$ x-scale)')
    plt.savefig('figure2.png')
    plt.close()


def test2():  #对p进行轮换
    for p in [0.5, 1, 2, 4]:
        _, lg10gamma_list, eff_list = ComputeScoreList(2 * config.size,
                                                       p)  #这里k是2*config.size
        plt.plot(lg10gamma_list,
                 eff_list,
                 linestyle='-',
                 marker='D',
                 label='p=' + str(p))
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\log_{10}\gamma$')
    plt.ylabel(r'$\epsilon$')
    plt.title(r'Effect of Planning Time (bold agent)')
    plt.savefig('figure3.png')
    plt.close()

    for p in [0.5, 1, 2, 4]:
        _, lg10gamma_list, eff_list = ComputeScoreList(1, p)  #k=1,也即选择的是保守策略
        plt.plot(lg10gamma_list,
                 eff_list,
                 linestyle='-',
                 marker='D',
                 label='p=' + str(p))
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\log_{10}\gamma$')
    plt.ylabel(r'$\epsilon$')
    plt.title(r'Effect of Planning Time (cautious agent)')
    plt.savefig('figure4.png')
    plt.close()


def test3():
    i = 5
    p = 4
    k_list = [1, 4, 2 * config.size]  #对比不同的策略和不同的p
    labels = ['cautious', 'normal', 'bold']
    for p in [4, 2, 1]:
        for k, label in zip(k_list, labels):
            _, lg10gamma_list, eff_list = ComputeScoreList(k, p)
            plt.plot(lg10gamma_list,
                     eff_list,
                     linestyle='-',
                     marker='D',
                     label=label)

        plt.grid()
        plt.legend()
        plt.xlabel(r'$\log_{10}\gamma$')
        plt.ylabel(r'$\epsilon$')
        plt.title('Effect of Degree of Boldness (p=%d)' % (p))
        plt.savefig('figure%d.png' % i)
        plt.close()
        i += 1


def test4():
    i = 8
    bold_k = 2 * config.size
    for p in [2, 1]:
        _, lg10gamma_list, eff_list = ComputeScoreList(bold_k, p)
        plt.plot(lg10gamma_list,
                 eff_list,
                 linestyle='-',
                 marker='D',
                 label='blind commitment')

        _, lg10gamma_list, eff_list = ComputeScoreList(bold_k, p, 'disappear')
        plt.plot(lg10gamma_list,
                 eff_list,
                 linestyle='-',
                 marker='D',
                 label='target disappearance')

        _, lg10gamma_list, eff_list = ComputeScoreList(bold_k, p, 'any_appear')
        plt.plot(lg10gamma_list,
                 eff_list,
                 linestyle='-',
                 marker='D',
                 label='target dis. or near')

        _, lg10gamma_list, eff_list = ComputeScoreList(bold_k, p,
                                                       'near_appear')
        plt.plot(lg10gamma_list,
                 eff_list,
                 linestyle='-',
                 marker='D',
                 label='target dis. or any')

        plt.grid()
        plt.legend()
        plt.xlabel(r'$\log_{10}\gamma$')
        plt.ylabel(r'$\epsilon$')
        plt.title('Effect of Reaction Strategy (p=%d)' % (p))
        plt.savefig('figure%d.png' % i)
        plt.close()
        i += 1

    k_list = [1, 4, 2 * config.size]
    labels = ['cautious', 'normal', 'bold']
    for k, label in zip(k_list, labels):
        _, lg10gamma_list, eff_list = ComputeScoreList(k, 1, 'disappear')
        plt.plot(lg10gamma_list,
                 eff_list,
                 linestyle='-',
                 marker='D',
                 label=label)
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\log_{10}\gamma$')
    plt.ylabel(r'$\epsilon$')
    plt.title('Effect of Degree of Boldness (reactive agent, p=1)')
    plt.savefig('figure10.png')
    plt.close()


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()