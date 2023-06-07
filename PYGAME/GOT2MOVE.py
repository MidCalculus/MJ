import pygame
import sys
import random

black = (0, 0, 0)

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

imgwall = pygame.image.load("PYGAME/e_wall.png")
imgFloor = pygame.image.load("PYGAME/e_floor.png")
imgPlayer = pygame.image.load("PYGAME/e_player.png")

pl_x = 4
pl_y = 4

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

def draw_dungeon(bg):

    bg.fill(black)
    for y in range(-5, 6):
        for x in range(-5, 6):
            X = (x + 5) * 16
            Y = (y + 5) * 16
            dx = pl_x + x
            dy = pl_y + y

            if 0 <= dx and dx < dungeon_w and 0 <= dy and dy < dungeon_h:
                if dungeon[dy][dx] == 0:
                    bg.blit(imgFloor, [X, Y])
                if dungeon[dy][dx] == 9:
                    bg.blit(imgwall, [X, Y])

            if x == 0 and y == 0:
                bg.blit(imgPlayer, [X, Y - 8])


def move_player():
    global pl_x, pl_y

    key = pygame.key.get_pressed()

    if key[pygame.K_UP] == 1:
        if dungeon[pl_y - 1][pl_x] != 9:
            pl_y = pl_y - 1
    if key[pygame.K_DOWN] == 1:
        if dungeon[pl_y + 1][pl_x] != 9:
            pl_y = pl_y + 1
    if key[pygame.K_LEFT] == 1:
        if dungeon[pl_y][pl_x - 1] != 9:
            pl_x = pl_x - 1
    if key[pygame.K_RIGHT] == 1:
        if dungeon[pl_y][pl_x + 1] != 9:
            pl_x = pl_x + 1

def main():
    pygame.init()
    pygame.display.set_caption("Dungeon Maker")
    screen = pygame.display.set_mode((176, 176))
    clock = pygame.time.Clock()

    make_dungeon()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_player()
        draw_dungeon(screen)

        pygame.display.update()
        clock.tick(20)

if __name__ == "__main__":
    main()
