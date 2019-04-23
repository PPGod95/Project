#!/usr/bin/python
# -*- coding: utf-8 -*-

from setting import *
import random


# 开始菜单
def start():
    global status
    menu_music.play()
    while status != START:
        if status == MENU:
            while status == MENU:
                screen.fill(BLACK)

                title_surf = t_FONT.render('split', True, WHITE)
                title_rect = title_surf.get_rect(center=(400, 200))
                screen.blit(title_surf, title_rect)

                start_surf = o_FONT.render('START', True, WHITE)
                start_rect = start_surf.get_rect(center=(400, 500))
                screen.blit(start_surf, start_rect)

                exit_surf = o_FONT.render('EXIT', True, WHITE)
                exit_rect = exit_surf.get_rect(center=(400, 600))
                screen.blit(exit_surf, exit_rect)

                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if (start_rect.left < x < start_rect.right) and (start_rect.top < y < start_rect.bottom):
                            status = START
                        if (exit_rect.left < x < exit_rect.right) and (exit_rect.top < y < exit_rect.bottom):
                            status = EXIT
        elif status == EXIT:
            pygame.quit()
            exit()


# 方块产生频率
def check():
    global enemy_frequency
    enemy_frequency += 1
    if enemy_frequency >= 80:
        enemy_frequency = 0


# 产生方块
def produce_l1():
    global enemy
    if enemy_frequency % 18 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = v[j], k
            if j == 0:
                enemy = Enemy(enemy_img[0], pos, RIGHT, 2, TYPE[0])
            else:
                enemy = Enemy(enemy_img[0], pos, LEFT, 2, TYPE[0])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, h[j]
            if j == 0:
                enemy = Enemy(enemy_img[0], pos, DOWN, 2, TYPE[0])
            else:
                enemy = Enemy(enemy_img[0], pos, UP, 2, TYPE[0])
        add(enemy)
    check()


def produce_l2():
    global enemy
    if enemy_frequency % 18 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = v[j], k
            if j == 0:
                enemy = Enemy(enemy_img[1], pos, RIGHT, 1, TYPE[1])
            else:
                enemy = Enemy(enemy_img[1], pos, LEFT, 1, TYPE[1])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, h[j]
            if j == 0:
                enemy = Enemy(enemy_img[1], pos, DOWN, 1, TYPE[1])
            else:
                enemy = Enemy(enemy_img[1], pos, UP, 1, TYPE[1])
        add(enemy)
    check()


def produce_l3():
    global enemy
    if enemy_frequency % 30 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = v[j], k
            if j == 0:
                enemy = Enemy(enemy_img[2], pos, RIGHT, 2, TYPE[1])
            else:
                enemy = Enemy(enemy_img[2], pos, LEFT, 2, TYPE[1])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, h[j]
            if j == 0:
                enemy = Enemy(enemy_img[2], pos, DOWN, 2, TYPE[1])
            else:
                enemy = Enemy(enemy_img[2], pos, UP, 2, TYPE[1])
        add(enemy)
    check()


def produce_l4():
    global enemy
    if enemy_frequency % 20 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = v[j], k
            if j == 0:
                enemy = Enemy(enemy_img[3], pos, RIGHT, 1, TYPE[2])
            else:
                enemy = Enemy(enemy_img[3], pos, LEFT, 1, TYPE[2])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, h[j]
            if j == 0:
                enemy = Enemy(enemy_img[3], pos, DOWN, 1, TYPE[2])
            else:
                enemy = Enemy(enemy_img[3], pos, UP, 1, TYPE[2])
        add(enemy)
    check()


def produce_l5():
    global enemy
    if enemy_frequency % 20 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = v[j], k
            if j == 0:
                enemy = Enemy(enemy_img[4], pos, RIGHT, 2, TYPE[2])
            else:
                enemy = Enemy(enemy_img[4], pos, LEFT, 2, TYPE[2])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, h[j]
            if j == 0:
                enemy = Enemy(enemy_img[4], pos, DOWN, 2, TYPE[2])
            else:
                enemy = Enemy(enemy_img[4], pos, UP, 2, TYPE[2])
        add(enemy)
    check()


def produce_l6():
    i = random.randint(1, 5)
    if i == 1:
        # produce_l1()
        pass
    elif i == 2:
        # produce_l2()
        pass
    elif i == 3:
        # produce_l3()
        pass
    elif i == 4:
        produce_l4()
    elif i == 5:
        produce_l5()


def generate():
    if level == 1:
        produce_l1()
    elif level == 2:
        produce_l2()
    elif level == 3:
        produce_l3()
    elif level == 4:
        produce_l4()
    elif level == 5:
        produce_l5()
    else:
        produce_l6()


# 增加方块
def add(n):
    global enemies, enemy_num
    enemies.add(n)
    enemy_num += 1


# 分裂
def split():
    global enemies
    for i in enemies:
        if i.type == EXBIG:
            enemy1 = Enemy(i.image, i.rect.topleft, UP, i.speed, BIG)
            enemy2 = Enemy(i.image, i.rect.topleft, DOWN, i.speed, BIG)
            enemy3 = Enemy(i.image, i.rect.topleft, LEFT, i.speed, BIG)
            enemy4 = Enemy(i.image, i.rect.topleft, RIGHT, i.speed, BIG)
            if i.distance > SCREEN_WIDTH / 4 + enemy_num % 150:
                if i.direction == LEFT:
                    enemies.add(enemy1, enemy2, enemy4)
                elif i.direction == RIGHT:
                    enemies.add(enemy1, enemy2, enemy3)
                elif i.direction == UP:
                    enemies.add(enemy2, enemy3, enemy4)
                elif i.direction == DOWN:
                    enemies.add(enemy1, enemy3, enemy4)
                i.change()
        elif i.type == BIG:
            enemy1 = Enemy(i.image, i.rect.topleft, UP, i.speed)
            enemy2 = Enemy(i.image, i.rect.topleft, DOWN, i.speed)
            enemy3 = Enemy(i.image, i.rect.topleft, LEFT, i.speed)
            enemy4 = Enemy(i.image, i.rect.topleft, RIGHT, i.speed)
            if i.distance > SCREEN_WIDTH / 4 + enemy_num % 150:
                if i.direction == LEFT:
                    enemies.add(enemy1, enemy2, enemy4)
                elif i.direction == RIGHT:
                    enemies.add(enemy1, enemy2, enemy3)
                elif i.direction == UP:
                    enemies.add(enemy2, enemy3, enemy4)
                elif i.direction == DOWN:
                    enemies.add(enemy1, enemy3, enemy4)
                i.change()


# 移动方块
def move():
    global running, player, enemies
    for i in enemies:
        i.move()
        if pygame.sprite.collide_rect_ratio(0.98)(player, i):
            player.is_hit = True
            running = False
        if i.rect.left < -24 or i.rect.left > SCREEN_WIDTH or i.rect.top > SCREEN_HEIGHT or i.rect.top < -24:
            enemies.remove(i)


# 初始化
def init():
    global level, player, enemies, enemy_num
    # level = 1
    player.is_hit = False
    enemies.empty()
    enemy_num = 0


# 游戏循环
def run():
    global running, level, enemy_num, Pass
    menu_music.stop()
    pygame.mixer.music.play(-1)
    init()
    i = 0
    while running:
        # 控制游戏最大帧率为60
        clock.tick(FPS)

        # level up
        if level < 6:
            if enemy_num > NUMBER[level - 1]:
                enemy_num = 0
                level += 1
                i = 0

        # produce enemy
        if level == 6 and enemy_num > NUMBER[level - 1]:
            if len(enemies) == 0:
                running = False
                Pass = True
        else:
            generate()

        # move enemy
        move()
        split()

        # draw
        screen.fill(0)
        # level
        if i < 180:
            screen.blit(LEVEL[level - 1], (260, 340))
            i += 1
        # player
        screen.blit(player.image, player.rect)
        # enemies
        enemies.draw(screen)

        # update
        pygame.display.update()

        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()
        # 若玩家被击中，则无效
        if not player.is_hit:
            if key_pressed[K_w] or key_pressed[K_UP]:
                player.up()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                player.down()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                player.left()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                player.right()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


# 是否再来
def again():
    global running

    level_surf = o_FONT.render('Level ' + str(level), True, WHITE)
    level_rect = level_surf.get_rect(center=(400, 240))
    screen.blit(level_surf, level_rect)

    con_surf = o_FONT.render('Continue?', True, WHITE)
    con_rect = con_surf.get_rect(center=(200, 500))
    screen.blit(con_surf, con_rect)

    yes_surf = o_FONT.render('YES', True, WHITE)
    yes_rect = yes_surf.get_rect(center=(500, 500))
    screen.blit(yes_surf, yes_rect)

    no_surf = o_FONT.render('NO', True, WHITE)
    no_rect = no_surf.get_rect(center=(700, 500))
    screen.blit(no_surf, no_rect)

    # 更新屏幕
    pygame.display.update()

    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (no_rect.left < x < no_rect.right) and (no_rect.top < y < no_rect.bottom):
                    pygame.quit()
                    exit()
                if (yes_rect.left < x < yes_rect.right) and (yes_rect.top < y < yes_rect.bottom):
                    running = True


# 通关
def pass_game():
    global running

    c_surf = o_FONT.render('Congrtulations!', True, WHITE)
    c_rect = c_surf.get_rect(center=(400, 240))
    screen.blit(c_surf, c_rect)

    a_surf = o_FONT.render('Play again?', True, WHITE)
    a_rect = a_surf.get_rect(center=(200, 500))
    screen.blit(a_surf, a_rect)

    yes_surf = o_FONT.render('YES', True, WHITE)
    yes_rect = yes_surf.get_rect(center=(500, 500))
    screen.blit(yes_surf, yes_rect)

    no_surf = o_FONT.render('NO', True, WHITE)
    no_rect = no_surf.get_rect(center=(700, 500))
    screen.blit(no_surf, no_rect)

    # 更新屏幕
    pygame.display.update()

    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (no_rect.left < x < no_rect.right) and (no_rect.top < y < no_rect.bottom):
                    pygame.quit()
                    exit()
                if (yes_rect.left < x < yes_rect.right) and (y > yes_rect.top < yes_rect.bottom):
                    running = True


# 游戏结束否
def over():
    pygame.mixer.music.stop()
    clock.tick(FPS)
    if Pass:
        pass_game()
    else:
        again()


# 主函数
def main():
    start()
    while running:
        run()
        over()


if __name__ == '__main__':
    main()
