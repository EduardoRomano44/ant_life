import pygame
from entities.Home import Home
from entities.Resourse import Food, Water


WIDTH, HEIGHT = 40, 20
SCALE = 10

clock = pygame.time.Clock()

home = Home()
f1 = Food((0, 5, 3))
w1 = Water((10, 15, 2))

def await_close():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    return

def main():
    while home.has_ants():
        artist.draw_map()
        artist.update()
        clock.tick(60)
    
    artist.game_over()
    await_close()
    pygame.quit()
        
if __name__ == "__main__":
    main()