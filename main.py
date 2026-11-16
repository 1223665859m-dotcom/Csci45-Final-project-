
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Survival")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player1 = pygame.Rect(30, 250, 15, 100)
player2 = pygame.Rect(755, 250, 15, 100)
ball = pygame.Rect(390, 290, 20, 20)

paddle_speed = 6
ball_speed_x = 5
ball_speed_y = 5

score1 = 0
score2 = 0

font = pygame.font.Font(None, 60)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed

    if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
        player1.y += paddle_speed

    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed

    if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
        player2.y += paddle_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player1) and ball_speed_x < 0:
        ball.left = player1.right
        ball_speed_x *= -1

    if ball.colliderect(player2) and ball_speed_x > 0:
        ball.right = player2.left
        ball_speed_x *= -1

    if ball.left <= 0:
        score2 += 1
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ball_speed_x = 5
        ball_speed_y = 5

    if ball.right >= SCREEN_WIDTH:
        score1 += 1
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ball_speed_x = -5
        ball_speed_y = -5

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    score_text = font.render(f"{score1}     {score2}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 75, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
