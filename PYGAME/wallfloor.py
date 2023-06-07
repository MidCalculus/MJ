
import pygame
import sys
import random

floor = (153, 255, 203)
wall = (100, 100, 100)
blank = (0, 0, 0)

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

def main():
    pygame.init()
    pygame.display.set_caption("Dungeon Maker")
    screen = pygame.display.set_mode((1056, 432))
    clock = pygame.time.Clock()

    make_dungeon()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_dungeon()

        for y in range(maze_h):
            for x in range(maze_w):
                X = x * 48
                Y = y * 48
                if maze[y][x] == 0:
                    pygame.draw.rect(screen, floor, [X, Y, 48, 48])
                if maze[y][x] == 1:
                    pygame.draw.rect(screen, wall, [X, Y, 48, 48])
                
        for y in range(dungeon_h):
            for x in range(dungeon_w):
                X = x * 16 + 528
                Y = y * 16
                if dungeon[y][x] == 0:
                    screen.blit(imgFloor, [X, Y])
                if dungeon[y][x] == 9:
                    screen.blit(imgwall, [X, Y])

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()