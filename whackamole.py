import pygame
import random

def main():
    global mole_pos

    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    mouse_x = mouse_pos[0] // 32
                    mouse_y = mouse_pos[1] // 32
                    if (mouse_x,mouse_y) == mole_pos:
                        mole_x = random.randrange(0,20) * 32
                        mole_y = random.randrange(0,16) * 32
                        pygame.display.flip()
                        clock.tick(60)

            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            mole_pos = (mole_x//32, mole_y//32)
            for i in range(640):
                if i % 32 == 0 and i != 0:
                    pygame.draw.line(screen, "black", (i, 0), (i, 512))
            for j in range(512):
                if j % 32 == 0 and j != 0:
                    pygame.draw.line(screen, "black", (0, j), (640, j))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
