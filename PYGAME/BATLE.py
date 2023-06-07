import pygame
import sys

white =  [255, 255, 255]

imgBattle = pygame.image.load("PYGAME/btlbg.png")
imgEnemy = None

emy_num = 0
emy_x = 0
emy_y = 0

def init_battle():
    global imgEnemy, emy_num, emy_x, emy_y

    emy_num = emy_num + 1
    if emy_num == 5:
        emy_num = 0
    imgEnemy = pygame.image.load("PYGAME/enemy" + str(emy_num) + ".png")

    emy_x = 440 - imgEnemy.get_width() / 2
    emy_y = 560 - imgEnemy.get_height()

def draw_battle(bg, fnt):
    bg.blit(imgBattle, [0, 0])
    bg.blit(imgEnemy, [emy_x, emy_y] )

    sur = fnt.render("enemy" + str(emy_num) + ".png", True, white)
    bg.blit(sur, [360, 580])

def main():
    pygame.init()
    pygame.display.set_caption("Battle Start")
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    init_battle()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    init_battle()

        draw_battle(screen, font)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()