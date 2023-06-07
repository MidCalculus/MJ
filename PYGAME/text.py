from tkinter import W
import pygame
import sys
import random

floor = (153, 255, 203)
wall = (100, 100, 100)

maze_w = 11
maze_h = 9
maze = []

for y in range(maze_h):
    maze.append([0] * maze_w)

def make_maze():
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

def main():
    pygame.init()
    pygame.display.set_caption("Maze Maker")
    screen = pygame.display.set_mode((528, 432))
    clock = pygame.time.Clock()

    make_maze()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_maze()

        for y in range(maze_h):
            for x in range(maze_w):
                h = 48
                w = 48
                X = x * w
                Y = y * h

                if maze[y][x] == 0:
                    pygame.draw.rect(screen, floor, [X, Y, w, h])
                if maze[y][x] == 1:
                    pygame.draw.rect(screen, wall, [X, Y, w, h])

        pygame.display.update()
        clock.tick(60)                                                



if __name__ == "__main__":
    main()

                            
                                
