from re import S
import pygame
import sys
import random
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
cyan = (0, 255, 255)
blink = [(224, 255, 255), (192, 240, 255), (128, 224, 255), (64, 192, 255), (128, 224, 255), (192, 240, 255)]

imgTitle = pygame.image.load("PYGAME/title.png")
imgWall = pygame.image.load("PYGAME/wall.png")
imgWall2 = pygame.image.load("PYGAME/wall2.png")
imgDark = pygame.image.load("PYGAME/dark.png")
imgPara = pygame.image.load("PYGAME/parameter.png")
imgbtlbg = pygame.image.load("PYGAME/btlbg.png")
imgEnemy = pygame.image.load("PYGAME/enemy0.png")
imgItem = [
    pygame.image.load("PYGAME/potion.png"),
    pygame.image.load("PYGAME/magbomb.png"),
    pygame.image.load("PYGAME/spoiled.png"),
    pygame.image.load("PYGAME/apple.png"),
    pygame.image.load("PYGAME/meat.png")
]
imgFloor = [
    pygame.image.load("PYGAME/floor.png"),
    pygame.image.load("PYGAME/tbox.png"),
    pygame.image.load("PYGAME/magcir.png"),
    pygame.image.load("PYGAME/stairs.png")
]
imgPlayer = [
    pygame.image.load("PYGAME/mychr0.png"),
    pygame.image.load("PYGAME/mychr1.png"),
    pygame.image.load("PYGAME/mychr2.png"),
    pygame.image.load("PYGAME/mychr3.png"),
    pygame.image.load("PYGAME/mychr4.png"),
    pygame.image.load("PYGAME/mychr5.png"),
    pygame.image.load("PYGAME/mychr6.png"),
    pygame.image.load("PYGAME/mychr7.png"),
    pygame.image.load("PYGAME/mychr8.png")
]
imgEffect = [
    pygame.image.load("PYGAME/effect_a.png"),
    pygame.image.load("PYGAME/effect_b.png")
]

speed = 1
volume = 3
idx = 0
tmr = 0
floor = 0
fl_max = 0
welcome = 0

pl_x = 0
pl_y = 0
pl_d = 0
pl_a = 0
pl_life = 0
pl_lifemax = 0
pl_str = 0
food = 0
potion = 0
magbomb = 0
treasure = 0

emy_name = ""
emy_lifemax = 0
emy_life = 0
emy_str = 0
emy_x = 0
emy_y = 0
emy_step = 0
emy_blink = 0

dmg_eff = 0
btl_cmd = 0

COMMAND = ["[A]ttack", "[P]otion", "[M]agic Bomb", "[R]un"]
TRE_NAME = ["Potion", "Magic Bomb", "Food Spoiled", "Food +20", "Food +100"]
EMY_NAME = ["Magic Eye", "Evil Flame", "Werewolf", "Naga", "Lizard Warrior", "Demon Centipede", "Elementals", "BLack ELemental", "Orc Forces", "Death Lord"]

maze_w = 11
maze_h = 9
maze = [] 

for y in range(maze_h):
    maze.append([0] * maze_w)

dungeon_w = maze_w * 3
dungeon_h = maze_h * 3
dungeon = []

for y in range(dungeon_h):
    dungeon.append([0] * dungeon_w)

def make_dungeon():
    xp = [0, 1, 0, -1]
    yp = [-1, 0, 1, 0]

    for x in range(maze_w):
        maze[0][x] = 1
        maze[maze_h - 1][x] = 1
    for y in range(1, maze_h-1):
        maze[y][0] = 1
        maze[y][maze_w - 1] = 1

    for y in range(1, maze_h - 1 ):
        for x in range(1, maze_w - 1):
            maze[y][x] = 0

    for y in range(2, maze_h - 2, 2):
        for x in range(2, maze_w - 2, 2):
            maze[y][x] = 1
    
    for y in range(2, maze_h -2, 2):
        for x in range(2, maze_w -2, 2):
            d = random.randint(0, 3)
            if x > 2:
                d = random.randint(0, 2)
            maze[y + yp[d]][x + xp[d]] = 1

    for y in range(dungeon_h):
        for x in range(dungeon_w):
            dungeon[y][x] = 9

    for y in range(1, maze_h -1):
        for x in range(1, maze_w -1):      
            dx = x * 3 + 1
            dy = y * 3 + 1
            if maze[y][x] == 0:
                if random.randint(0, 99) < 20:
                    for rx in range(-1, 2):
                        for ry in range(-1, 2):
                            dungeon[dy + ry][dx + rx] = 0

                else:
                    dungeon[dy][dx] = 0
                    if maze[y - 1][x] == 0:
                        dungeon[dy - 1][dx] = 0
                    if maze[y + 1][x] == 0:
                        dungeon[dy + 1][dx] = 0
                    if maze[y][x - 1] == 0:
                        dungeon[dy][dx - 1] = 0
                    if maze[y][x + 1] == 0:
                        dungeon[dy][dx + 1] = 0

def draw_dungeon(bg, fnt):
    bg.fill(black)
    for y in range(-4, 6):
        for x in range(-5, 6):
            X = (x + 5) * 80
            Y = (y + 4) * 80
            dx = pl_x + x
            dy = pl_y + y

            if 0 <= dx and dx <  dungeon_w and 0 <= dy and dy < dungeon_h:
                if dungeon[dy][dx] <= 3:
                    bg.blit(imgFloor[dungeon[dy][dx]], [X, Y])
                if dungeon [dy][dx] == 9:
                    bg.blit(imgWall, [X, Y-40])
                    if dy >= 2 and dungeon[dy - 1][dx] == 9:
                        bg.blit(imgWall2, [X, Y-80])

            if x == 0 and y == 0:
                bg.blit(imgPlayer[pl_a], [X, Y - 40])
    
    bg.blit(imgDark, [0, 0])
    draw_para(bg, fnt)

def put_event():
    global pl_x, pl_y, pl_d, pl_a

    while True:
        x = random.randint(3, dungeon_w - 4)
        y = random.randint(3, dungeon_h - 4)

        if (dungeon[y][x] == 0):
            for ry in range(-1, 2):
                for rx in range(-1, 2):
                    dungeon[y + ry][x + rx ] = 0
            dungeon[y][x] = 3
            break
    for i in range(60):
        x = random.randint(3, dungeon_w - 4)
        y = random.randint(3, dungeon_h - 4)

        if (dungeon[y][x] == 0):
            dungeon[y][x] = random.choice([1, 2, 2, 2, 2])

    while True:
        pl_x = random.randint(3, dungeon_w - 4)
        pl_y = random.randint(3, dungeon_h - 4)

        if (dungeon[pl_y][pl_x] == 0):
            break

    pl_d = 1
    pl_a = 2
    
def move_player(key):
    global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life, food, potion, magbomb, treasure

    if dungeon[pl_y][pl_x] == 1:
        dungeon[pl_y][pl_x] = 0
        treasure = random.choice([0, 0, 0, 1, 1, 1, 1, 1, 1, 2]) 

        if treasure == 0:
            potion = potion + 1
        if treasure == 1:
            magbomb = magbomb + 1
        if treasure == 2:
            food = int(food / 2)

        idx = 3
        tmr = 0
    
    if dungeon[pl_y][pl_x] == 2:
        dungeon[pl_y][pl_x] = 0
        r = random.randint(0, 99)

        if r < 40:
            treasure = random.choice([3, 3, 3, 4])
                
            if treasure == 3:
                food = food + 20
            if treasure == 4:
                food = food + 100

            idx = 3
            tmr = 0

        else:
            idx = 10
            tmr = 0
        return

    if dungeon[pl_y][pl_x] == 3:
        idx = 2
        tmr = 0
        return
    
    x = pl_x 
    y = pl_y

    if key[K_UP] == 1:
        pl_d = 0
        if dungeon[pl_y - 1][pl_x] != 9:
            pl_y = pl_y - 1
    if key[K_DOWN] == 1:
        pl_d = 1
        if dungeon[pl_y + 1][pl_x] != 9:
            pl_y = pl_y + 1
    if key[K_LEFT] == 1:
        pl_d = 2
        if dungeon[pl_y][pl_x - 1]  != 9:
            pl_x = pl_x - 1
    if key[K_RIGHT] == 1:
        pl_d = 3
        if dungeon[pl_y][pl_x + 1] != 9:
            pl_x = pl_x + 1

    pl_a = pl_d * 2
    if pl_x != x or pl_y != y:
        pl_a = pl_a + tmr % 2
        if food > 0:
            food = food - 1
            if pl_life < pl_lifemax:
                pl_life = pl_life + 1

        else:
            pl_life = pl_life - 5
            if pl_life <= 0:
                pl_life = 0
                pygame.mixer.music.stop()
                idx = 9
                tmr = 0

def draw_text(bg, txt, x, y, fnt, col):
    sur = fnt.render(txt, True, black)
    bg.blit(sur, [x + 1, y + 2])

    sur = fnt.render(txt, True, col )
    bg.blit(sur, [x, y])

def draw_para(bg, fnt):
    x = 30
    y = 600
    bg.blit(imgPara, [x, y])
    col = white 

    if pl_life < 10 and tmr % 2 == 0:
        col = red
        
    draw_text(bg, "{}/{}".format(pl_life, pl_lifemax), x + 128, y + 6, fnt, col)
    draw_text(bg, str(pl_str), x + 128, y + 33, fnt, white)

    col = white
    
    if food == 0 and tmr % 2 == 0:
        col = red

    draw_text(bg, str(food), x + 128, y + 60, fnt, col)
    draw_text(bg, str(potion), x + 266, y + 6, fnt, col)
    draw_text(bg, str(magbomb), x + 266, y + 33, fnt, col)

def init_battle():
    global imgEnemy, emy_name, emy_lifemax, emy_life, emy_str, emy_x, emy_y

    typ = random.randint(0, floor)
    if floor >= 10:
        typ = random.randint(0, 9)

    lev = random.randint(1, floor)

    imgEnemy = pygame.image.load("PYGAME/enemy" + str(typ) + ".png")
    emy_name = EMY_NAME[typ] + "LV" + str(lev)

    emy_lifemax = 60 * (typ + 1) + (lev - 1) * 10
    emy_life = emy_lifemax
    emy_str = int(emy_lifemax / 8)
    emy_x = 440 - imgEnemy.get_width() / 2
    emy_y = 560 - imgEnemy.get_height()

def draw_bar(bg, x, y, w, h, val, ma):

    pygame.draw.rect(bg, white, [x -2, y -2, w + 4, h + 4])
    pygame.draw.rect(bg, black, [x, y, w, h])

    if val > 0:
        pygame.draw.rect(bg, (0, 128, 255), [x, y, w * val / ma, h])

def draw_battle(bg, font):
    global emy_blink, dmg_eff
    bx = 0
    by = 0

    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)

    bg.blit(imgbtlbg, [bx, by])

    
    if emy_life > 0 and emy_blink % 2 == 0:
        bg.blit(imgEnemy, [emy_x, emy_y + emy_step])

    draw_bar(bg, 340, 680, 200, 10, emy_life, emy_lifemax)

    if emy_blink > 0:
        emy_blink = emy_blink - 1

    for i in range(10):
        draw_text(bg, message[i], 600, 100 + i * 50, font, white)

    draw_para(bg, font)

def battle_command(bg, font, key):
    global btl_cmd

    ent = False

    if key[K_a]:
        btl_cmd = 0
        ent = True
    if key[K_1]:
        btl_cmd = 1
        ent = True
    if key[K_m]:
        btl_cmd = 2
        ent = True
    if key[K_r]:
        btl_cmd = 3
        ent = True

    if key[K_UP] and btl_cmd > 0:
        btl_cmd -= 1
    if key[K_DOWN] and btl_cmd < 3:
        btl_cmd += 1
    if key[K_SPACE] or key[K_RETURN]:
        ent = True
    
    for i in range(4):
        c = white
        
        if btl_cmd == i:
            c = blink[tmr % 6]

        draw_text(bg, COMMAND[i], 20 , 360 + i * 60, font, c)

    return ent

message = [""] * 10

def init_message():
    for i in range(10):
        message[i] == ""

def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    
    for i in range(9):
        message[i] = message[i + 1]
    message[9] = msg

def PAIN():
    global speed, volume, idx, tmr, floor, fl_max, welcome
    global pl_a,  pl_lifemax, pl_life, pl_str, food, potion, magbomb
    global emy_life, emy_step, emy_blink, dmg_eff

    dmg = 0
    lif_p = 0
    str_p = 0

    pygame.init()
    pygame.display.set_caption("Dungeon Explorer")
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font("C:\\Windows\Fonts\Arial.ttf", 30)
    fontS = pygame.font.Font("C:\\WIndows\Fonts\Arial.ttf", 20)

    se = [
        pygame.mixer.Sound("PYGAME/de_se_attack.ogg"),
        pygame.mixer.Sound('PYGAME/de_se_blaze.ogg'),
        pygame.mixer.Sound('PYGAME/de_se_potion.ogg'),
        pygame.mixer.Sound('PYGAME/de_jin_gameover.ogg'),
        pygame.mixer.Sound('PYGAME/de_jin_levup.ogg'),
        pygame.mixer.Sound('PYGAME/de_jin_win.ogg')
    ]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_s:
                    speed = speed + 1
                    if speed == 4:
                        speed = 1
                if event.key == K_p:
                    volume = volume + 1
                    if volume > 7:
                        volume = 7
                if event.key == K_o:
                    volume = volume - 1
                    if volume <= 0:
                        volume = 0
        
        tmr = tmr + 1
        key= pygame.key.get_pressed()

        if idx == 0:
            if tmr == 1:
                pygame.mixer.music.load("PYGAME/de_bgm_title.ogg")
                pygame.mixer.music.set_volume(volume / 10)
                pygame.mixer.music.play(-1)
            screen.fill(black)
            screen.blit(imgTitle, [40, 60])
            if fl_max >= 2:
                draw_text(screen, "You reached floor {}".format(fl_max), 200, 400, font, cyan)
            draw_text(screen, "Press Space Key", 320, 560, font, blink[tmr % 6])  

            if key[K_SPACE] == 1:
                make_dungeon()
                put_event()

                floor = 1
                welcome = 15
                pl_lifemax = 300
                pl_life = pl_lifemax
                pl_str = 100
                food = 300
                potion = 0
                magbomb = 0
                idx = 1
                pygame.mixer.music.load("PYGAME/de_bgm_field.ogg")
                pygame.mixer.music.set_volume(volume / 10)
                pygame.mixer.music.play(-10)
        
        elif idx == 1:
            move_player(key)
            draw_dungeon(screen, fontS)
            draw_text(screen, "floor {} ({}, {}).".format(floor, pl_x, pl_y), 60, 40, fontS, white)

            if welcome > 0:
                welcome = welcome - 1
                draw_text(screen, "Welcome to floor {}".format(floor), 300, 180, font, cyan)

        elif idx == 2:
            draw_dungeon(screen, fontS)
            if 1 <= tmr and tmr<= 5:
                h = 80 * tmr
                pygame.draw.rect(screen, black, [0, 0, 880, h])
                pygame.draw.rect(screen, black, [0, 720 - h, 880, h])
            if tmr == 5:
                floor = floor + 1
                if floor > fl_max:
                    fl_max = floor
                welcome = 15
                make_dungeon()
                put_event()
            if 6 <= tmr and tmr <= 9:
                h = 80 * (10 - tmr)
                pygame.draw.rect(screen, black, [0, 0, 880, h])
                pygame.draw.rect(screen, black, [0, 720 - h, 880, h])               
            if tmr == 10:
                idx = 1

        elif idx == 3:
            draw_dungeon(screen, fontS)
            screen.blit(imgItem[treasure], [320, 220])
            draw_text(screen, TRE_NAME[treasure], 380, 240, font, white)
            if tmr == 10:
                idx = 1

        elif idx == 9:
            if tmr <= 30:
                pl_turn = [2, 4, 6, 8]
                pl_a = pl_turn[tmr % 4]
                if tmr == 30:
                    pl_a = 8
                draw_dungeon(screen, fontS)
            elif tmr  == 31:
                se[3].play()
                draw_text(screen, "You died", 360, 240, font, red)
                draw_text(screen, "GAME OVER", 360, 380, font, red)
            elif tmr == 100:
                idx = 0
                tmr = 0

        elif idx == 10:
            if tmr == 1:
                pygame.mixer.music.load("PYGAME/de_bgm_battle.ogg")
                pygame.mixer.music.set_volume(volume / 10)
                pygame.mixer.music.play(-1)
                init_battle()
                init_message()
            elif tmr <= 4:
                bx = (4 - tmr) * 220
                by = 0
                screen.blit(imgbtlbg, [bx, by])
                draw_text(screen, "ENCOUNTER!", 350, 200, font, white)
            elif tmr <= 16:
                draw_battle(screen, fontS)
                draw_text(screen, emy_name + " appeared!", 300, 200, font, white)
            else:
                idx = 11
                tmr = 0
        
        elif idx == 11:
            draw_battle(screen, fontS)
            if tmr == 11:
                set_message("Your turn.")
            if battle_command(screen, font, key) == True:
                if btl_cmd == 0:
                    idx = 12
                    tmr = 0
                if btl_cmd == 1 and potion > 0:
                    idx = 20
                    tmr = 0
                if btl_cmd == 2 and magbomb > 0:
                    idx = 21
                    tmr = 0
                if btl_cmd == 3:
                    idx = 14
                    tmr = 0
        
        elif idx == 12:
            draw_battle(screen, fontS)

            if tmr == 1:
                set_message("Your attack")
                se[0].play()
                dmg = pl_str + random.randint(0, 9)

            if 2 <= tmr and tmr <= 4:
                screen.blit(imgEffect[0], [700 - tmr * 120, -100 + tmr * 120])
            if tmr == 5:
                emy_blink = 5
                set_message(str(dmg) + "pts of damage!")

            if tmr == 11:
                emy_life = emy_life - dmg
                if emy_life <= 0:
                    emy_life = 0
                    idx = 16
                    tmr = 0
            if tmr == 16:
                idx = 13
                tmr = 0
        
        elif idx == 13:
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Enemy turn.")
            if tmr == 5:
                set_message(emy_name + " attacks!")
                se[0].play()
                emy_step = 30
            if tmr == 9:
                dmg = emy_str + random.randint(0, 9)
                dmg_eff = 5
                emy_step = 0
            if tmr == 15:
                pl_life = pl_life - dmg
                if pl_life < 0:
                    pl_life - 0
                    idx = 15
                    tmr = 0
            if tmr == 20:
                idx = 11
                tmr = 0
        
        elif idx == 14:
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("...")
            if tmr == 2:
                set_message(".....")
            if tmr == 3:
                set_message(".......")
            if tmr == 4:
                set_message(".........")
            if tmr == 5:
                if random.randint(0, 99) < 60:
                    idx == 22
                else:
                    set_message("Bruh, u failed to flee bro...")

            if tmr == 10:
                idx = 13
                tmr = 0
        
        elif idx == 15:
            draw_battle(screen, fontS)
            if tmr == 1:
                pygame.mixer.music.stop()
                set_message("LOL skill issue XD")

            if tmr == 11:
                idx = 9
                tmr = 29
        
        elif idx == 16:
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("LOL EZ GG")
                pygame.mixer.music.stop()
                se[5].play()
            if tmr == 28:
                idx = 22
                if random.randint(0, emy_lifemax) > random.randint(0, pl_lifemax):
                    idx = 17
                    tmr = 0

        elif idx == 17:
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Keed you have leveled up!!!")
                se[4].play()
                lif_p = random.randint(10, 20)
                str_p = random.randint(5, 10)
            if tmr == 21:
                set_message("Max life + " + str(lif_p))
                pl_lifemax = pl_lifemax + lif_p
            if tmr == 26:
                set_message("str + " + str(str_p))
                pl_str = pl_str + str_p
            if tmr == 35:
                idx == 22

        elif idx == 20:
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Potion!")
                se[2].play()
            if tmr == 6:
                pl_life = pl_lifemax
                potion = potion - 1
            if tmr == 11:
                idx = 13
                tmr = 0

        elif idx == 21:
            draw_battle(screen, fontS)
            img_rz = pygame.transform.rotozoom(imgEffect[1], 30 * tmr, (12 - tmr) / 8)
            X = 440 - img_rz.get_width() / 2
            Y = 360 - img_rz.get_height() / 2
            screen.blit(img_rz, [X, Y])
            if tmr == 1:
                set_message("Magic Bomb!")
                se[1].play()
            if tmr == 6:
                magbomb = magbomb - 1
            if tmr == 11:
                dmg = 1000
                idx = 12
                tmr = 4
        
        elif idx == 22:
            pygame.mixer.music.load("PYGAME/de_bgm_field.ogg")
            pygame.mixer.music.set_volume(volume / 10)
            pygame.mixer.music.play(-1)
            idx = 1

        draw_text(screen, "[s]peed " + str(speed), 740, 40, fontS, white)
        draw_text(screen, "Volyme U[p] D[o]wn " + str(volume), 630, 10, fontS, white)

        pygame.display.update()
        clock.tick(4 + 2 * speed)

if __name__ == "__main__":
    PAIN()






