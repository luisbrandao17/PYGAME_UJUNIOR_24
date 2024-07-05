#Example file showing a circle moving on screen
import pygame
import random 
from time import sleep

#escolher nome de equipa
name_left = input("Escreve o nome do jogador da esquerda:\n")
name_right = input("Escreve o nome do jogador da direita:\n")

#pygame setup (variáveis)
pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True
dt = 0
vball_x = 0
vball_y = 0
increase = 0

#PONTUAÇÕES
score_left = 0
score_right = 0

#posições inicais dos jogadores e da bola
player_right_pos = pygame.Vector2(1080 - screen.get_width() / 8, screen.get_height() / 2 - 30)
player_left_pos = pygame.Vector2(screen.get_width() / 8, screen.get_height() / 2 - 30)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#variáveis das balizas
goal_width = 10
goal_height = 200
goal_left = pygame.Rect(0, screen.get_height() / 2 - goal_height / 2, goal_width, goal_height)
goal_right = pygame.Rect(screen.get_width() - goal_width, screen.get_height() / 2 - goal_height / 2, goal_width, goal_height)

#fonte para o texto de golo
font = pygame.font.Font(None, 74)
goal_message = ""
goal_time = 0
marcou = False
#cor = ""

#golos
def check_goal(ball_pos, goal_left, goal_right):
    global player_left_pos, player_right_pos
    if goal_left.collidepoint(ball_pos.x - 20, ball_pos.y) or goal_left.collidepoint(ball_pos.x + 20, ball_pos.y):
        return "GOLO DO "  + name_right +" !"
    if goal_right.collidepoint(ball_pos.x - 20, ball_pos.y) or goal_right.collidepoint(ball_pos.x + 20, ball_pos.y):
        return "GOLO DO "  + name_left +" !"
    return ""

#velocidades padrão dos jogadores
player_speed = 300
player_left_pos_speed = player_speed
player_right_pos_speed = player_speed


while running:
    if marcou:
        dt = 0
    marcou = False
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # verifica se a tecla Enter foi pressionada
                # reiniciar o jogo
                score_left = 0
                score_right = 0
                goal_time = 0
                ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                player_right_pos = pygame.Vector2(1080 - screen.get_width() / 8, screen.get_height() / 2 - 30)
                player_left_pos = pygame.Vector2(screen.get_width() / 8, screen.get_height() / 2 - 30)
                vball_x = 0
                vball_y = 0
                increase = 0
            if event.key == pygame.K_SPACE:  #aumentar velocidade do jogador esquerdo
                player_left_pos_speed = player_speed * 1.5
            if event.key == pygame.K_DELETE:  #aumentar velocidade do jogador direito
                player_right_pos_speed = player_speed * 1.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:  #restaurar velocidade do jogador esquerdo
                player_left_pos_speed = player_speed
            if event.key == pygame.K_DELETE:  #restaurar velocidade do jogador direito
                player_right_pos_speed = player_speed

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")

    #desenhar balizas
    pygame.draw.rect(screen, "white", goal_left)
    pygame.draw.rect(screen, "white", goal_right)

    pygame.draw.rect(screen, "red", pygame.Rect(player_left_pos.x, player_left_pos.y, 60, 60))
    keys = pygame.key.get_pressed()

    player_left_pos_old = pygame.Vector2(player_left_pos.x, player_left_pos.y)
    player_right_pos_old = pygame.Vector2(player_right_pos.x, player_right_pos.y)
    if keys[pygame.K_w]:
        player_left_pos.y -= player_left_pos_speed * dt
    if keys[pygame.K_s]:
        player_left_pos.y += player_left_pos_speed * dt
    if keys[pygame.K_a]:
        player_left_pos.x -= player_left_pos_speed * dt
    if keys[pygame.K_d]:
        player_left_pos.x += player_left_pos_speed * dt

    pygame.draw.rect(screen, "purple", pygame.Rect(player_right_pos.x, player_right_pos.y, 60, 60))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_right_pos.y -= player_right_pos_speed * dt
    if keys[pygame.K_DOWN]:
        player_right_pos.y += player_right_pos_speed * dt
    if keys[pygame.K_LEFT]:
        player_right_pos.x -= player_right_pos_speed * dt
    if keys[pygame.K_RIGHT]:
        player_right_pos.x += player_right_pos_speed * dt
    #player1 = pygame.draw.rect
    #player2 = pygame.draw.rect 
    pygame.draw.circle(screen, "white", ball_pos, 20, 4)
    #bola andar pra frente  e pra trás (cubo esquerdo)
    if (player_left_pos.y - 20 <  ball_pos.y and player_left_pos.y + 80 > ball_pos.y):
        if (player_left_pos.x + 80 > ball_pos.x and player_left_pos.x -20 < ball_pos.x):
            if increase < 10:
                increase += 0.8
            if (ball_pos.x > player_left_pos.x + 60):
                vball_x = random.randint(2,5) + increase
            if (ball_pos.x < player_left_pos.x):
                vball_x = -random.randint(2,5) - increase
            if (ball_pos.y < player_left_pos.y):
                vball_y = -random.randint(2,5) - increase
            if (ball_pos.y > player_left_pos.y + 60):
                vball_y = random.randint(2,5) + increase
    #bola andar pra frente  e pra trás (cubo direito)
    if (player_right_pos.y - 20 <  ball_pos.y and player_right_pos.y + 80 > ball_pos.y):
        if (player_right_pos.x + 80 > ball_pos.x and player_right_pos.x -20 < ball_pos.x):
            if increase < 7:
                increase += 0.5
            if (ball_pos.x > player_right_pos.x + 60):
                vball_x = random.randint(2,5) + increase
            if (ball_pos.x < player_right_pos.x):
                vball_x = -random.randint(2,5) - increase
            if (ball_pos.y < player_right_pos.y):
                vball_y = -random.randint(2,5) - increase
            if (ball_pos.y > player_right_pos.y + 60):
                vball_y = random.randint(2,5) + increase
    #quadrados não se tocam
    pl = pygame.Rect(player_left_pos.x, player_left_pos.y, 60, 60)
    pr = pygame.Rect(player_right_pos.x, player_right_pos.y, 60, 60)
    if pygame.Rect.colliderect(pl, pr):
        player_right_pos = player_right_pos_old
        player_left_pos = player_left_pos_old




    #colisão com as bordas da tela
    if ball_pos.x - 20 <= 0 or ball_pos.x + 20 >= 1080:
        vball_x = -vball_x
    if ball_pos.y - 20 <= 0 or ball_pos.y + 20 >= 720:
        vball_y = -vball_y
    #colisão com as bordas da tela (cubos)
    #ESQUERDO (parede)
    if player_left_pos.x <= 0:
        player_left_pos.x = 0 
    if player_left_pos.x + 60 >= 1080:
        player_left_pos.x = 1020
    #DIREITO (parede)
    if player_right_pos.x <= 0:
        player_right_pos.x = 0 
    if player_right_pos.x + 60 >= 1080:
        player_right_pos.x = 1020
    #ESQUERDO (teto e chão)
    if player_left_pos.y <= 0:
        player_left_pos.y = 0 
    if player_left_pos.y + 60 >= 720:
        player_left_pos.y = 660
    #DIREITO (teto e chãos)
    if player_right_pos.y <= 0:
        player_right_pos.y = 0 
    if player_right_pos.y + 60 >= 720:
        player_right_pos.y = 660


    ball_pos.x += vball_x
    ball_pos.y += vball_y

    #VERIFICAR SE A BOLA ENTROU
    goal_message = check_goal(ball_pos, goal_left, goal_right)
    if check_goal(ball_pos, goal_left, goal_right):
        marcou = True
        goal_time = pygame.time.get_ticks()
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        player_right_pos = pygame.Vector2(1080 - screen.get_width() / 8, screen.get_height() / 2 - 30)
        player_left_pos = pygame.Vector2(screen.get_width() / 8, screen.get_height() / 2 - 30)
        vball_x = 0
        vball_y = 0
        increase = 0
        if name_right in goal_message:
            score_right += 1
        else:
            score_left += 1
        if score_left >= 5 or score_right >= 5:
            running = False
        text = font.render(goal_message, True, (255, 255, 255))
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))

    #mostrar pontuação
    score_text = font.render(f"{name_left} {score_left} - {score_right} {name_right}", True, (255, 255, 255))
    screen.blit(score_text, (screen.get_width() / 2 - score_text.get_width() / 2, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()
    if marcou:
        sleep(2)
        pygame.event.clear()
        for a in pygame.key.get_pressed():
            a = False


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

    #Descomentar isto!!


    dt = clock.tick(60) / 1000

pygame.quit()