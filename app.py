import pygame



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move square")


square_size = 50 
square_color = (255, 0, 0)
player_x, player_y = 375, 275
speed = 0.5


enemy_size = 50 
enemy_color = (255, 255, 0)
enemy_x, enemy_y = 100, 100
enemy_speed = 0.2


font = pygame.font.Font(None, 85)
game_over = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            

    #player logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: 
        player_x -= speed
    if keys[pygame.K_d]:
        player_x += speed
    if keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_s]:
        player_y += speed


    # enemy logic ehh, tror något sånt
    if enemy_x < player_x:
        enemy_x += enemy_speed
    elif enemy_x > player_x:
        enemy_x -= enemy_speed

    if enemy_y < player_y:
        enemy_y += enemy_speed
    elif enemy_y > player_y:
        enemy_y -= enemy_speed


    #collision detection
    player_rect = pygame.Rect(player_x, player_y, square_size, square_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    if player_rect.colliderect(enemy_rect):
        game_over = True


    screen.fill((255, 255, 255))

    if not game_over:
        pygame.draw.rect(screen, square_color, (player_x, player_y, square_size, square_size ))
        pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, enemy_size, enemy_size))

    else:
        text = font.render("Game over", True, (255, 0, 0))
        screen.blit(text, (250, 250))

    pygame.display.flip()


pygame.quit()