import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 10
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50
PLAYER_SPEED = 5
BLOCK_SPEED = 5
FONT_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Font
font = pygame.font.Font(None, FONT_SIZE)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Keep the player within the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH

# Block class
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - BLOCK_WIDTH)
        self.rect.y = -BLOCK_HEIGHT
    
    def update(self):
        self.rect.y += BLOCK_SPEED
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -BLOCK_HEIGHT
            self.rect.x = random.randint(0, SCREEN_WIDTH - BLOCK_WIDTH)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def show_menu():
    screen.fill(BLACK)
    draw_text("Dodge the Blocks", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
    draw_text("Press SPACE to Start", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text("Press Q to Quit", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
    pygame.display.flip()

def game_loop(player_name):
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group()

    # Create player
    player = Player()
    all_sprites.add(player)

    # Create blocks
    for _ in range(5):
        block = Block()
        all_sprites.add(block)
        blocks.add(block)

    # Initialize game variables
    score = 0
    start_time = pygame.time.get_ticks()
    
    # Game loop
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        # Update sprites
        all_sprites.update()

        # Check for collisions
        if pygame.sprite.spritecollideany(player, blocks):
            running = False
            print(f"Game Over! Your score: {score}")

        # Update score and timer
        score = (pygame.time.get_ticks() - start_time) // 1000  # Score increases every second

        # Draw everything
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        # Display score and timer
        draw_text(f"Score: {score}", font, WHITE, screen, 100, 20)
        draw_text(f"Player: {player_name}", font, WHITE, screen, SCREEN_WIDTH - 100, 20)
        draw_text(f"Time: {(pygame.time.get_ticks() - start_time) // 1000} seconds", font, WHITE, screen, SCREEN_WIDTH // 2, 20)

        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

def main():
    show_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_name = input("Enter your name: ")
                    game_loop(player_name)
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
