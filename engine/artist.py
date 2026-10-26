from pathlib import Path
import pygame
from engine.sprite_library import SpriteLibrary



class Artist:
    def __init__(self, width, height, scale, font_name="PressStart2P", font_size=20, sprites=None, score_font_size=11):
        self.width = width
        self.height = height
        self.scale = scale
        self.display = pygame.display.set_mode((scale * width, scale * height))
        pygame.font.init()
        self.sprites = sprites or SpriteLibrary(scale)
        self.font_name = font_name
        self.font = self.get_font(font_size)

    def get_font(self, size: int) -> pygame.font.Font:
        font_file = Path(__file__).parent.parent / "assets" / "fonts" / "PressStart2P.ttf"
        if font_file.exists():
            try:
                return pygame.font.Font(str(font_file), size)
            except Exception:
                pass
        return pygame.font.SysFont("Arial", size)

    def copy_display(self):
        return self.display.copy()

    def blit_display(self, image, position=(0,0), update=False):
        self.display.blit(image, position)
        if update:
            pygame.display.flip()

    def draw_map(self, variant="default"):
        if variant is None:
            self.display.fill("green")
            return

        if variant == "end":
            self.display.fill("black")
            return

        background_image = self.sprites.get("background", variant, size=self.display.get_size())
        self.display.blit(background_image, (0, 0))

    def draw_square(self, position, color):
        x, y = position
        pygame.draw.rect(self.display, color, (x * self.scale, y * self.scale, self.scale, self.scale))

    def draw_home(self, home):
        self.draw_square(home.location, "yellow")

    def draw_ant(self, ant, variant="default"):
        self.draw_square(ant.location, "brown")

    def draw_water(self, water, variant="default"):
        for position in water.positions:
            self.draw_square(position, "blue")

    def draw_food(self, food, variant="default"):
        for position in food.positions:
            self.draw_square(position, "white")
    
    def update(self):
        pygame.display.flip()

    def game_over(self):
        self.draw_map("end")
        messages = ["Game Over", "All ants have died", "Press Enter to exit"]
        color = ["red", "white", "white"]
        text_sizes = [40, 22, 14]
        for i in range(len(messages)):
            font = self.get_font(text_sizes[i])
            text_render = font.render(messages[i], True, color[i])
            text_rect = text_render.get_rect(center=(self.width * self.scale / 2, self.height * self.scale / 2 + (i - 1) * 50))
            self.display.blit(text_render, text_rect)

        pygame.display.flip()
