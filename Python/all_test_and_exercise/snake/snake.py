import pygame
import random
pygame.init()

import matplotlib.pyplot as plt
 
font = pygame.font.SysFont("", 40)

#设置窗口
length = 600   #窗口长度
width = 600   #窗口宽度
score = 0   #初始成绩
window = pygame.display.set_mode((length,width))   #设置窗口的长度与宽度
pygame.display.set_caption('贪吃蛇')   #设置窗口标题

blue=(0,0,255)   #蓝色RGB
black=(0,0,0)   #黑色RGB
white=(255,255,255)
NJUpurple=(106,0,95)   #南大紫的RGB
Red=(255,0,0)   #红色RGB
green=(0,255,255)

#给出蛇的坐标
head=[300,300]#蛇头的坐标
snake=[[300,300], [290,300], [280,300]]#蛇身体的三个矩形的坐标

#随机给出食物的坐标
food=[random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]

#游戏开始与游戏结束界面
#设置游戏开始界面
def start(window):
    window.fill(white)
    prompt = font.render('Press Enter to start', 1 , black)   #设置文本内容和字体颜色
    window.blit(prompt, (175, 285))   #绘制出字体
    pygame.display.update()   #刷新
    while True:  #进行按键监听  
        for event in pygame.event.get():  #获取所有事件信息
            if event.type == pygame.QUIT:   #如果用户鼠标点击了窗口的X
                pygame.quit()   #终止程序
                exit()   #终止程序
            elif event.type == pygame.KEYDOWN:#获取键盘按键信息
                if event.key == pygame.K_ESCAPE:   #终止程序
                    pygame.quit()   #终止程序
                else:
                    return 0   #结束初始界面，开始玩蛇
#设置游戏结束界面        
def over(window):
    window.fill(white)
    prompt = font.render('Your Score is %s .Thanks to play.'%score, 1 , Red)
    window.blit(prompt, (100,285))
    pygame.display.update()
    while True:  
	    for event in pygame.event.get():  
		    if event.type == pygame.QUIT:
			    pygame.quit()
			    exit()   
		    elif event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_ESCAPE:
				    pygame.quit() 
				    exit()
def hit_wall(head):
    if head[0] >= length or head[0]<0 or head[1] >= width or head[1] < 0:   #如果蛇头坐标超出四周的界线
        return 1   #撞墙发生
    else:
        return 0
#咬蛇自尽
def hit_snake():
    if snake[0] in snake[1:]:   #如果蛇头坐标与身体中坐标重合
        return 1   #咬蛇自尽发生
    else:
        return 0

#控制蛇的移动
def movesnake (direction):
    global food   #声明全局变量（在函数中有赋值时使用）
    global score
    if direction == 1:   #如果移动方向为上
        head[1] = head[1] - 10   #Y轴坐标-10
        snake.insert(0, list(head))   #插入新的头部坐标
        if head != food:   #如果没有吃到食物
            snake.pop(-1)   #删去最后一个元素
        else:   #头部坐标等于食物坐标时即吃到食物，不删除末尾元素即完成增长
            score = score + 1#分数
            food = [random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]   #食物被吃后随机产生新食物
            while food in snake:
                food = [random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]   #食物被吃后随机产生新食物
    elif direction == 2:
        head[1] = head[1] + 10
        snake.insert(0, list(head))
        if head != food:
            snake.pop(-1)
        else:
            score = score + 1
            food = [random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]
            while food in snake:
                food = [random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]   #食物被吃后随机产生新食物
    elif direction == 3:
        head[0] = head[0] - 10
        snake.insert(0, list(head))
        if head != food:
            snake.pop(-1)
        else:
            score = score + 1
            food = [random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]
            while food in snake:
                food = [random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]   #食物被吃后随机产生新食物
    elif direction == 4:       
        head[0] = head[0] + 10
        snake.insert(0, list(head))
        if head != food:
            snake.pop(-1)
        else:
            score = score + 1
            food = [random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]
            while food in snake:
                food = [random.randrange(1, 60) * 10, random.randrange(1, 60) * 10]   #食物被吃后随机产生新食物
            
    #贪吃蛇死了
    if hit_snake() or hit_wall(head):   #蛇撞到自身或者撞到墙
        over(window)  
 
speed = pygame.time.Clock()
direction = 4   #初始化移动方向为右 
start(window) 
while True:
    for event in pygame.event.get():#获取所有事件信息
        if event.type == pygame.QUIT: #如果用户鼠标点击了窗口的X
            pygame.quit()             #终止pygame程序   
            exit()                    #终止所有程序   
            
        if event.type == pygame.KEYDOWN:   #获取键盘按键信息
            if event.key == pygame.K_ESCAPE:   #如果按键ESC
                pygame.quit()
                exit()
            if direction != 2 and event.key == pygame.K_UP:   #如果原始方向不是下，并且现在按键为上
                direction = 1   #方向改变为上   
            elif direction != 1 and event.key == pygame.K_DOWN:
                direction = 2
            elif direction != 4 and event.key == pygame.K_LEFT:
                direction = 3             
            elif direction != 3 and event.key == pygame.K_RIGHT:
                direction = 4
    
    movesnake(direction)   #根据按键方向移动蛇
    window.fill(white)   #给窗口绘制白色的画布
    pygame.draw.rect(window,black,pygame.Rect(food[0],food[1],10,10))   #画出食物
    #画出小蓝蛇
    for i in snake:   
        pygame.draw.rect(window, NJUpurple, pygame.Rect(i[0], i[1], 10, 10))

    score_show = font.render('Score: %s' % score, 1 , Red)   #格式化输出得分信息
    window.blit(score_show, (450, 20))
    pygame.display.update()   #刷新界面
    speed.tick(5)