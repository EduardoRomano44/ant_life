import pygame
from entities.Resourse import Food, Water
from entities.map import Map
from engine.artist import Artist


WIDTH, HEIGHT = 80, 40
SCALE = 10

def await_close(clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    return
        clock.tick(60)

def main():
    pygame.init()
    try:
        clock = pygame.time.Clock()
        world = Map((WIDTH, HEIGHT), {
            "food": [Food(((0, 20), 5, 7))],
            "water": [Water(((60, 20), 20, 3))],
        }, starting_location=(39, 19))
        artist = Artist(WIDTH, HEIGHT, SCALE)

        while world.home.has_ants():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            world.tick()
            artist.draw_map()
            for food in world.food:
                artist.draw_food(food)
            for water in world.water:
                artist.draw_water(water)
            for ant in world.home.ants:
                artist.draw_ant(ant)
            artist.draw_home(world.home)
            artist.update()
            clock.tick(10)

        artist.game_over()
        await_close(clock)
    finally:
        pygame.quit()
        
if __name__ == "__main__":
    main()
