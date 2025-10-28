import pygame
from utils import load_sprite

class SpaceRocks:
    def __init__(self):
        self._init_pygame()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Space Rocks")

        # Load and scale background image to fit the entire screen
        self.background = load_sprite("bg", False)
        self.background = pygame.transform.smoothscale(self.background, (self.screen_width, self.screen_height))

        self.clock = pygame.time.Clock()
        self.running = True

    def main_loop(self):
        while self.running:
            self._handle_input()
            self._process_game_logic()
            self._draw()
            self.clock.tick(60)  # Limit to 60 FPS

    def _init_pygame(self):
        pygame.init()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def _process_game_logic(self):
        # Placeholder for your asteroid / ship logic
        pass

    def _draw(self):
        # Draw scaled background
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    game = SpaceRocks()
    game.main_loop()