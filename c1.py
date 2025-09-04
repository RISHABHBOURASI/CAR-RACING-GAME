import pygame, random, sys

pygame.init()
screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()

car = pygame.Rect(180, 500, 40, 80)
enemy = pygame.Rect(random.randint(50, 310), -100, 40, 80)

speed = 5
score = 0
font = pygame.font.SysFont(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.left > 50: car.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and car.right < 350: car.move_ip(5, 0)

    enemy.move_ip(0, speed)
    if enemy.top > 600:
        enemy.topleft = (random.randint(50, 310), -100)
        score += 1
        speed += 0.2

    if car.colliderect(enemy):
        print("Game Over! Score:", score)
        pygame.quit(); sys.exit()

    screen.fill((50,150,50))
    pygame.draw.rect(screen, (0,0,255), car)
    pygame.draw.rect(screen, (255,0,0), enemy)
    text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(text, (10,10))

    pygame.display.flip()
    clock.tick(60)
