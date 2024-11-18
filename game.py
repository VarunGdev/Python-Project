import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 2 * player_size
player_speed = 7

# Falling block settings
block_size = 50
block_speed = 5
blocks = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop flag
running = True

# Function to display score
def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Main game loop
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Create new blocks
    if random.randint(1, 20) == 1:  # 5% chance per frame to spawn a new block
        new_block = [random.randint(0, WIDTH - block_size), 0]
        blocks.append(new_block)

    # Move blocks
    for block in blocks:
        block[1] += block_speed

    # Remove blocks that are off-screen
    blocks = [block for block in blocks if block[1] < HEIGHT]

    # Collision detection
    for block in blocks:
        if (player_x < block[0] + block_size and
            player_x + player_size > block[0] and
            player_y < block[1] + block_size and
            player_y + player_size > block[1]):
            running = False

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, RED, (block[0], block[1], block_size, block_size))

    # Update score
    score += 1

    # Display score
    display_score()

    # Refresh screen
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
