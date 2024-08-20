import pygame
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField


def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = [asteroids, drawable, updatable]
    AsteroidField.containers = updatable
    asteriodfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ingame_clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.collision_check(player):
                print("GAME OVER !!!")
                exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = ingame_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
