import pygame

pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLATFORM_COLOR = (255, 255, 255)
PLAYER_COLOR = (255, 0, 0)
PLATFORM_WIDTH2 = 150


current_level = 1

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the platform
platform1 = pygame.Rect(350, 500, PLATFORM_WIDTH, PLATFORM_HEIGHT)

platform2 = pygame.Rect(200, 500, PLATFORM_WIDTH2, PLATFORM_HEIGHT)

# Create the player
player = pygame.Rect(375, 460, PLAYER_WIDTH, PLAYER_HEIGHT)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_ip(-10, 0)
            elif event.key == pygame.K_RIGHT:
                player.move_ip(10, 0)

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw the platform and the player based on the current level
    if current_level == 1:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform1)
        pygame.draw.rect(screen, PLAYER_COLOR, player)
        # Check if the player has reached the end of the level
        if player.colliderect(platform1) == False:
            current_level = 2
    elif current_level == 2:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform2)
        pygame.draw.rect(screen, PLAYER_COLOR, player)
        # Check if the player has reached the end of the level
        if player.colliderect(platform2) == True:
            running = False

    # Update the screen
    pygame.display.flip()

pygame.quit()
