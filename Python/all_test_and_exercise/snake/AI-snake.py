import pygame, sys, random, time
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((300, 300))
pygame.display.set_caption('贪吃蛇')#设置游戏窗口的标题
FPSCLOCK = pygame.time.Clock()#游戏速度
BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)#字体
font = pygame.font.SysFont('simsunnsimsun', 80)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (150, 150, 150)
GREEN = (0, 255, 255)
YELLOW = (255, 255, 0)
FORESTGREEN = (34, 139, 34)
Purple3 = (125, 38, 205)

snake_Head = [100, 100]#贪吃蛇的的初始位置
snake_Body = [[80, 100], [60, 100], [40, 100]]#初始化贪吃蛇的长度
direction = "RIGHT"#指定蛇初始前进的方向，向右


def randomfood(snake_Body):
    # 随机生成x, y
    x = random.randrange(1, 15)
    y = random.randrange(1, 15)
    Position = [int(x * 20), int(y * 20)]
    while Position in snake_Body:
        x = random.randrange(1, 15)
        y = random.randrange(1, 15)
        Position = [int(x * 20), int(y * 20)]
    return Position


#随机出现第一个食物
food_Position = randomfood(snake_Body)
food_flag = 1


def GameOver():
    # 设置GameOver的显示颜色
    # 设置GameOver的位置

    pygame.display.flip()
    # 等待3秒
    time.sleep(3)
    # 退出游戏
    pygame.quit()
    # 退出程序
    sys.exit()


def walkable(location0, snake_body0):
    l = []
    if location0[0] + 20 < 300 and [location0[0] + 20, location0[1]] not in snake_body0:#+20表示下一个位置
        l.append([location0[0] + 20, location0[1]])

    if location0[0] - 20 >= 0 and [location0[0] - 20, location0[1]] not in snake_body0:
        l.append([location0[0] - 20, location0[1]])

    if location0[1] + 20 < 300 and [location0[0], location0[1] + 20] not in snake_body0:
        l.append([location0[0], location0[1] + 20])

    if location0[1] - 20 >= 0 and [location0[0], location0[1] - 20] not in snake_body0:
        l.append([location0[0], location0[1] - 20])

    return l


def changexy(position0):
    position = position0
    return position[1] * 15 + position[0]


def BFS(food_position0, snake_body0):
    food_position = food_position0.copy()
    snake_body = snake_body0.copy()
    flag = 0
    path = []
    search = []
    dict = {}
    search.append([snake_body[0][0], snake_body[0][1]])
    dict[changexy([snake_body[0][0], snake_body[0][1]])] = -1
    while len(search) > 0:
        currentlocation = search.pop(0)
        if currentlocation != food_position:
            l1 = walkable(currentlocation, snake_body)
            for i in l1:
                if dict.get(changexy(i)) == None:
                    search.append(i)
                    dict[changexy(i)] = currentlocation
        else:
            flag = 1
            break

    path.append(currentlocation)
    while dict[changexy(currentlocation)] != -1:
        currentlocation = dict[changexy(currentlocation)]
        path.append(currentlocation)
    path.reverse()

    return path, flag


def tailBFS(tail_position0, snake_body0):
    tail_position = tail_position0.copy()
    snake_body = snake_body0.copy()
    flag = 0
    path = []
    search = []
    dict = {}
    search.append([snake_body[0][0], snake_body[0][1]])
    dict[changexy([snake_body[0][0], snake_body[0][1]])] = -1
    while len(search) > 0:
        currentlocation = search.pop(0)
        if currentlocation != tail_position:
            tail = snake_body.pop()
            l1 = walkable(currentlocation, snake_body)
            snake_body.append(tail)
            for i1 in l1:
                if dict.get(changexy(i1)) == None:
                    search.append(i1)
                    dict[changexy(i1)] = currentlocation
        else:
            flag = 1
            break

    return flag


def exploretheway(food_position0, snake_body0):
    snake_body = snake_body0.copy()
    food_position = food_position0.copy()
    while True:
        path, flag1 = BFS(food_position, snake_body)
        snake_body.insert(0, path[1])
        if snake_body[0][0] == food_position[0] and snake_body[0][1] == food_position[1]:
            flag2 = tailBFS(snake_body[-1], snake_body)

            break
        else:
            snake_body.pop()
    return flag2


def longest_tail_path(snake_body0):
    snake_body = snake_body0.copy()
    tail = snake_body.pop()
    l0 = walkable(snake_body[0], snake_body)
    snake_body.append(tail)
    longest = -1

    for i0 in l0:
        flag = 0
        path = []
        search = []
        dict = {}
        search.append(i0)
        dict[changexy(i0)] = -1
        while len(search) > 0:
            currentlocation = search.pop(0)
            if currentlocation != snake_body[-1]:
                tail = snake_body.pop()
                l1 = walkable(currentlocation, snake_body)
                snake_body.append(tail)
                for j in l1:
                    if dict.get(changexy(j)) == None:
                        search.append(j)
                        dict[changexy(j)] = currentlocation
            else:
                flag = 1
                break
        path.append(currentlocation)
        while dict[changexy(currentlocation)] != -1:
            currentlocation = dict[changexy(currentlocation)]
            path.append(currentlocation)
        path.reverse()

        if flag == 1:

            if len(path) > longest:
                longest = len(path)
                longest_path = path
    return longest_path


#漫步函数，随机选择蛇头周围四个方向中可走的方向走一步
def wander(snake_body0):
    l = walkable(snake_body0[0], snake_body0)
    if len(l) > 1:
        x = random.randrange(0, len(l))
    elif len(l) == 1:
        x = 0
    else:
        return l
    return l[x]

def hit_wall(head):
    if head[0] >= 300 or head[0]<0 or head[1] >= 300 or head[1] < 0:   #如果蛇头坐标超出四周的界线
        return 1   #撞墙发生
    else:
        return 0
#咬蛇自尽
def hit_snake():
    if snake_Head in snake_Body:   #如果蛇头坐标与身体中坐标重合
        return 1   #咬蛇自尽发生
    else:
        return 0

while True:
    food_path, food_flag = BFS(food_Position, snake_Body)
    tail_flag = tailBFS(snake_Body[-1], snake_Body)
    if food_flag == 1: #当前布局能找到吃food_path
        virtual_tail_flag = exploretheway(food_Position, snake_Body) #虚拟蛇探路，吃到食物后如果能找到tail_path则返回1
        if virtual_tail_flag == 1:#虚拟蛇吃完食物后找得到tail_path
            print("安全路径吃食物")
            #真实的蛇沿最短路径向食物走一步#
            snake_Body.insert(0, food_path[1])
            if snake_Body[0][0] == food_Position[0] and snake_Body[0][1] == food_Position[1]:
                food_Position = randomfood(snake_Body)
            else:
                snake_Body.pop()#删除最后一个

        else:  #虚拟蛇吃完食物后找不到tail_path
            print("直接吃不安全，找蛇尾")
            #真实的蛇沿最长路径向蛇尾走一步#
            longest_path = longest_tail_path(snake_Body)
            snake_Body.insert(0, longest_path[0])
            if snake_Body[0][0] == food_Position[0] and snake_Body[0][1] == food_Position[1]:
                food_Position = randomfood(snake_Body)
            else:
                snake_Body.pop()

    elif tail_flag == 1:##当前布局能找到tail_path（找不到food_path）
        print("找到蛇尾")
        #真实的蛇沿最长路径向蛇尾走一步#
        longest_path = longest_tail_path(snake_Body)
        snake_Body.insert(0, longest_path[0])
        snake_Body.pop()

    elif food_flag != 1 and tail_flag != 1: #找不到food_path也找不到tail_path时
        print("找不到食物也找不到蛇尾")
        if len(wander(snake_Body)) == 0:
            print("走投无路")
            GameOver()
        else:
            snake_Body.insert(0, wander(snake_Body))
            snake_Body.pop()

    def drawSnake(snake_body0):
        pygame.draw.rect(DISPLAY, Purple3, Rect(snake_body0[0][0], snake_body0[0][1], 20, 20))
        for j in range(1, len(snake_body0)-1):
            pygame.draw.rect(DISPLAY, FORESTGREEN, Rect(snake_body0[j][0], snake_body0[j][1], 20, 20))
        pygame.draw.rect(DISPLAY, GREEN, Rect(snake_body0[-1][0], snake_body0[-1][1], 20, 20))


    def drawFood(food_position0):
        pygame.draw.rect(DISPLAY, RED, Rect(food_position0[0], food_position0[1], 20, 20))


    def drawScore(score):
        # 设置分数的显示颜色
        score_Surf = BASICFONT.render('%s' % (score), True, GREY)
        # 设置分数的位置
        score_Rect = score_Surf.get_rect()
        score_Rect.midtop = (50, 20)
        DISPLAY.blit(score_Surf, score_Rect)


    DISPLAY.fill(WHITE)
    drawSnake(snake_Body)# 画出贪吃蛇
    drawFood(food_Position)# 画出食物的位置
    drawScore(len(snake_Body) - 3)# 打印出玩家的分数
    pygame.display.flip()# 刷新Pygame的显示层
    FPSCLOCK.tick(50)# 控制游戏速度

    if hit_wall(snake_Head) or hit_snake():
        GameOver()