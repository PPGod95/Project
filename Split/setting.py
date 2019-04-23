#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


# 游戏属性
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

# RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 游戏状态
MENU = 0
START = 1
EXIT = 2
status = MENU

# 方向
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


# 类型
SMALL = 0
BIG = 1
EXBIG = 2
TYPE = [SMALL, BIG, EXBIG]


class Player(pygame.sprite.Sprite):
    def __init__(self, init_img):
        self.image = init_img
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)
        self.speed = 10
        self.is_hit = False

    def up(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def down(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def left(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def right(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, init_pos, init_dir, init_speed=1, init_type=SMALL):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = init_pos
        self.speed = init_speed
        self.direction = init_dir
        self.type = init_type
        self.distance = 0

    def move(self):
        # 移动
        self.distance += self.speed * 3
        if self.direction == UP:
            self.rect.top -= self.speed * 3
        elif self.direction == DOWN:
            self.rect.top += self.speed * 3
        elif self.direction == LEFT:
            self.rect.left -= self.speed * 3
        elif self.direction == RIGHT:
            self.rect.left += self.speed * 3

    def change(self):
        # 类型转换
        if self.type == EXBIG:
            self.type = BIG
            self.distance = 0
        elif self.type == BIG:
            self.type = SMALL


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN, 32)
pygame.display.set_caption("split")
clock = pygame.time.Clock()
level = 1
running = True
Pass = False

# 字体
t_FONT = pygame.font.Font('Fonts/CHILLER.ttf', 200)
o_FONT = pygame.font.Font('Fonts/comic.ttf', 80)

# 音乐
menu_music = pygame.mixer.Sound('Music/per.wav')
menu_music.set_volume(0.4)
pygame.mixer.music.load('Music/circles.mp3')
pygame.mixer.music.set_volume(0.5)

# 等级
level1_img = pygame.image.load('Images/Level/level1.png')
level2_img = pygame.image.load('Images/Level/level2.png')
level3_img = pygame.image.load('Images/Level/level3.png')
level4_img = pygame.image.load('Images/Level/level4.png')
level5_img = pygame.image.load('Images/Level/level5.png')
level6_img = pygame.image.load('Images/Level/level6.png')
LEVEL = [level1_img, level2_img, level3_img, level4_img, level5_img, level6_img]

# 玩家初始化
player_img = pygame.image.load('Images/0.png')
player = Player(player_img)

# 方块初始化
enemy_img1 = pygame.image.load('Images/1.png')
enemy_img2 = pygame.image.load('Images/1.png')
enemy_img3 = pygame.image.load('Images/1.png')
enemy_img4 = pygame.image.load('Images/1.png')
enemy_img5 = pygame.image.load('Images/1.png')
enemy_img = [enemy_img1, enemy_img2, enemy_img3, enemy_img4, enemy_img5]
v = [-24, SCREEN_WIDTH]
h = [-24, SCREEN_HEIGHT]
enemies = pygame.sprite.Group()
enemy_frequency = 0
enemy_num = 0
NUMBER = [20, 20, 20, 20, 20, 50]
