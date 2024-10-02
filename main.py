import pygame
import constants
import player


def main():
    pygame.init()
    screen = pygame.display.set_mode((
        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player_character = player.Player(x, y, constants.PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_character.draw(screen)
        player_character.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
