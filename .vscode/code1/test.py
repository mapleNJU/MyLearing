from game import Tile_map, Agent
from config import config
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy
from numpy import random
from math import inf

seeds = [5, 1, 8]


def work(config):
    effect_score = []
    for seed in seeds:
        random.seed(seed)
        # print(config.max_generation_time, config.max_life)
        world = Tile_map(config)
        agent = Agent(config, world)
        # print(world.map)
        for i in range(config.game_time):
            # for i in range(100):
            # print("i:",i)
            # print(agent.step, agent.k, agent.p)
            action = agent.action_work()
            hole = deepcopy(world.hole)
            # print(world.hole)
            score = world.map_update(action)
            # print(agent.env.hole)
            # if i>38 and i<55:
            #     for i in hole:
            #         print("hole position:",i.x,i.y, i.age, i.life)
            #     print("score=",score , world.agent_position_x, world.agent_position_y)
            # print(world.hole,world.agent_position_x,world.agent_position_y,action)
            # print(agent.env, world)
            agent.get_score(score)
        print("total score:", world.score_sum, ", effect_score:", agent.score)
        effect_score.append(agent.score / world.score_sum)
        # print(config.max_life)
    return sum(effect_score) / len(effect_score)


def test1():

    effect_score = []
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    for gamma in gammas:
        # print(gamma)
        # for gamma in [100]:
        temp_config = deepcopy(config)
        temp_config.min_life = int(temp_config.min_life // gamma) + 1
        # print(config.min_life)
        temp_config.max_life = int(temp_config.max_life // gamma) + 1
        temp_config.min_generation_time = int(
            temp_config.min_generation_time // gamma) + 1
        temp_config.max_generation_time = int(
            temp_config.max_generation_time // gamma) + 1
        effect_score.append(work(temp_config))
    plt.plot(gammas,
             effect_score,
             linestyle='-',
             marker='D',
             label='experiment')
    plt.grid(axis='both')
    plt.legend()
    plt.title("Effect of Rate of World Change ")
    plt.savefig('test1-1.png')
    plt.close()

    plt.plot(log10gammas,
             effect_score,
             linestyle='-',
             marker='D',
             label='experiment')
    plt.grid(axis='both')
    plt.legend()
    plt.title("Effect of Rate of World Change (log x-scale)")
    plt.savefig('test1-2.png')
    plt.close()


def test2():
    mark = ['D', 'H', 'P', 'X']
    color = ['b', 'c', 'g', 'r']
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    i = 0
    for p in [0.5, 1, 2, 4]:
        effect_score = []
        for gamma in gammas:
            # for gamma in [1]:
            temp_config = deepcopy(config)
            temp_config.p = p
            temp_config.min_life = int(temp_config.min_life // gamma)
            # print(config.min_life)
            temp_config.max_life = int(temp_config.max_life // gamma)
            temp_config.min_generation_time = int(
                temp_config.min_generation_time // gamma)
            temp_config.max_generation_time = int(
                temp_config.max_generation_time // gamma)
            effect_score.append(work(temp_config))
        label_temp = 'p=' + str(p)
        plt.plot(log10gammas,
                 effect_score,
                 marker=mark[i],
                 color=color[i],
                 label=label_temp)
        i += 1
    plt.grid()
    plt.legend()
    plt.title("Effect of Planning Time (bold agent)")
    plt.savefig('test2-1.png')
    plt.close()

    mark = ['D', 'H', 'P', 'X']
    color = ['b', 'c', 'g', 'r']
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    i = 0
    # for p in [4]:
    for p in [0.5, 1, 2, 4]:
        effect_score = []
        for gamma in gammas:
            # for gamma in [100]:
            temp_config = deepcopy(config)
            temp_config.k = 1
            temp_config.p = p
            temp_config.min_life = temp_config.min_life // gamma + 1
            # print(config.min_life)
            temp_config.max_life = temp_config.max_life // gamma + 1
            # print(temp_config.max_life)
            temp_config.min_generation_time = temp_config.min_generation_time // gamma + 1
            temp_config.max_generation_time = temp_config.max_generation_time // gamma + 1
            effect_score.append(work(temp_config))
        label_temp = 'p=' + str(p)
        plt.plot(log10gammas,
                 effect_score,
                 marker=mark[i],
                 color=color[i],
                 label=label_temp)
        i += 1
    plt.grid()
    plt.legend()
    plt.title("Effect of Planning Time (cautious agent)")
    plt.savefig('test2-2.png')
    plt.close()


def test3():
    mark = ['D', 'H', 'P']
    color = ['b', 'c', 'g']
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    i = 0
    for k in [inf, 4, 1]:
        effect_score = []
        for gamma in gammas:
            # for gamma in [1]:
            temp_config = deepcopy(config)
            temp_config.k = k
            temp_config.p = 4
            temp_config.min_life = int(temp_config.min_life // gamma)
            # print(config.min_life)
            temp_config.max_life = int(temp_config.max_life // gamma)
            temp_config.min_generation_time = int(
                temp_config.min_generation_time // gamma)
            temp_config.max_generation_time = int(
                temp_config.max_generation_time // gamma)
            effect_score.append(work(temp_config))
        label_temp = ['bold', 'normal', 'cautious']
        plt.plot(log10gammas,
                 effect_score,
                 marker=mark[i],
                 color=color[i],
                 label=label_temp[i])
        i += 1
    plt.grid()
    plt.legend()
    plt.title("Effect of Degree of Boldness (p = 4)")
    plt.savefig('test3-1.png')
    plt.close()

    mark = ['D', 'H', 'P']
    color = ['b', 'c', 'g']
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    i = 0
    for k in [inf, 4, 1]:
        effect_score = []
        for gamma in gammas:
            # for gamma in [1]:
            temp_config = deepcopy(config)
            temp_config.k = k
            temp_config.p = 2
            temp_config.min_life = int(temp_config.min_life // gamma)
            # print(config.min_life)
            temp_config.max_life = int(temp_config.max_life // gamma)
            temp_config.min_generation_time = int(
                temp_config.min_generation_time // gamma)
            temp_config.max_generation_time = int(
                temp_config.max_generation_time // gamma)
            effect_score.append(work(temp_config))
        label_temp = ['bold', 'normal', 'cautious']
        plt.plot(log10gammas,
                 effect_score,
                 marker=mark[i],
                 color=color[i],
                 label=label_temp[i])
        i += 1
    plt.grid()
    plt.legend()
    plt.title("Effect of Degree of Boldness (p = 2)")
    plt.savefig('test3-2.png')
    plt.close()

    mark = ['D', 'H', 'P']
    color = ['b', 'c', 'g']
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    i = 0
    for k in [inf, 4, 1]:
        effect_score = []
        for gamma in gammas:
            # for gamma in [1]:
            temp_config = deepcopy(config)
            temp_config.k = k
            temp_config.p = 1
            temp_config.min_life = int(temp_config.min_life // gamma)
            # print(config.min_life)
            temp_config.max_life = int(temp_config.max_life // gamma)
            temp_config.min_generation_time = int(
                temp_config.min_generation_time // gamma)
            temp_config.max_generation_time = int(
                temp_config.max_generation_time // gamma)
            effect_score.append(work(temp_config))
        label_temp = ['bold', 'normal', 'cautious']
        plt.plot(log10gammas,
                 effect_score,
                 marker=mark[i],
                 color=color[i],
                 label=label_temp[i])
        i += 1
    plt.grid()
    plt.legend()
    plt.title("Effect of Degree of Boldness (p = 1)")
    plt.savefig('test3-3.png')
    plt.close()


def test4():
    mark = ['D', 'H', 'P', 'X']
    color = ['b', 'c', 'g', 'r']
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    i = 0
    for reaction_strategy in [
            'blind_commitment', 'notice_disappearance', 'any_new_hole',
            'nearer_hole'
    ]:
        effect_score = []
        for gamma in gammas:
            # for gamma in [1]:
            temp_config = deepcopy(config)
            temp_config.p = 2
            temp_config.reaction_strategy = reaction_strategy
            temp_config.min_life = int(temp_config.min_life // gamma)
            # print(config.min_life)
            temp_config.max_life = int(temp_config.max_life // gamma)
            temp_config.min_generation_time = int(
                temp_config.min_generation_time // gamma)
            temp_config.max_generation_time = int(
                temp_config.max_generation_time // gamma)
            effect_score.append(work(temp_config))
        label_temp = [
            'blind commitment', 'notices target disappearance',
            'target dis. or any new hole', 'target dis. or nearer hole'
        ]
        plt.plot(log10gammas,
                 effect_score,
                 marker=mark[i],
                 color=color[i],
                 label=label_temp[i])
        i += 1
    plt.grid()
    plt.legend()
    plt.title("Effect of Reaction Strategy (p = 2) ")
    plt.savefig('test4-1.png')
    plt.close()

    mark = ['D', 'H', 'P', 'X']
    color = ['b', 'c', 'g', 'r']
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    i = 0
    for reaction_strategy in [
            'blind_commitment', 'notice_disappearance', 'any_new_hole',
            'nearer_hole'
    ]:
        effect_score = []
        for gamma in gammas:
            # for gamma in [1]:
            temp_config = deepcopy(config)
            temp_config.p = 1
            temp_config.reaction_strategy = reaction_strategy
            temp_config.min_life = int(temp_config.min_life // gamma)
            # print(config.min_life)
            temp_config.max_life = int(temp_config.max_life // gamma)
            temp_config.min_generation_time = int(
                temp_config.min_generation_time // gamma)
            temp_config.max_generation_time = int(
                temp_config.max_generation_time // gamma)
            effect_score.append(work(temp_config))
        label_temp = [
            'blind commitment', 'notices target disappearance',
            'target dis. or nearer hole', 'target dis. or any new hole'
        ]
        plt.plot(log10gammas,
                 effect_score,
                 marker=mark[i],
                 color=color[i],
                 label=label_temp[i])
        i += 1
    plt.grid()
    plt.legend()
    plt.title("Effect of Reaction Strategy (p = 1) ")
    plt.savefig('test4-2.png')
    plt.close()

    mark = ['D', 'H', 'P']
    color = ['b', 'c', 'g']
    log10gammas = np.linspace(0, 2, 15)
    gammas = 10**log10gammas
    i = 0
    for k in [inf, 4, 1]:
        effect_score = []
        for gamma in gammas:
            # for gamma in [1]:
            temp_config = deepcopy(config)
            temp_config.k = k
            temp_config.p = 1
            temp_config.reaction_strategy = 'notice_disappearance'
            temp_config.min_life = int(temp_config.min_life // gamma)
            # print(config.min_life)
            temp_config.max_life = int(temp_config.max_life // gamma)
            temp_config.min_generation_time = int(
                temp_config.min_generation_time // gamma)
            temp_config.max_generation_time = int(
                temp_config.max_generation_time // gamma)
            effect_score.append(work(temp_config))
        label_temp = ['bold', 'normal', 'cautious']
        plt.plot(log10gammas,
                 effect_score,
                 marker=mark[i],
                 color=color[i],
                 label=label_temp[i])
        i += 1
    plt.grid()
    plt.legend()
    plt.title("Effect of Degree of Boldness (reactive agent, p = 1) ")
    plt.savefig('test4-3.png')
    plt.close()