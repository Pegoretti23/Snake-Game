import pygame_menu
import pygame
import time
import random

#game over function
def game_over(score):
    #creating font
    my_font = pygame.font.SysFont('comic sans ms', 50)

    #end score
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()

    #position of text
    game_over_rect.midtop = (window_x/2, window_y/4)

    #drw text on scrren
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    #after 3 seconds close de game
    time.sleep(2)

    #quit
    quit()

#set difficulty
def set_difficulty(value):

    if value== 2:
        speed = 15
        add = 10
        return snake_speed, add
    elif value == 1:
        speed = 10
        add = 5
        return snake_speed, add
    pass
def start_game():
    # snake default position
    snake_position = [240, 50]

    #body snake
    snake_body = [
                    [240, 50],
                    [230, 50],
                    [220, 50],
                    [210, 50]
    ]

    #position of fruit
    fruit_position = [random.randrange(1, (window_x//10))*10,
                      random.randrange(1, (window_y//10))*10]
    fruit_spawn = True

    #default snake direction
    direction = 'DOWN'
    change_to = direction

    #Main Funcition

    score = 0
    while True:
        #event Keys
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
        #no move snake in two directions
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        #Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10
        # Growing snake's body
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 1
            fruit_spawn = False
        else:
            snake_body.pop()
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10))*10,
                              random.randrange(1, (window_y//10))*10]
            #progression of dificulty
            if score % 2 == 0 and score != 0:
                snake_speed += add
        fruit_spawn = True
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(
                pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        #GAME OVER CONDITIONS
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over(score)
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over(score)
        #Touching snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(score)
        #display score
        score_font = pygame.font.SysFont('verdana', 20)
        score_surface = score_font.render('Score : ' + str(score), True, red)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)
        #refresh game screen
        pygame.display.update()
        #FPS
        fps.tick(snake_speed)

#WINDOW SIZE
window_x = 720
window_y = 480

#Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#Initiate pygame
pygame.init()

#Initialise game window
pygame.display.set_caption("Snake")
game_window = pygame.display.set_mode((window_x, window_y))

#Frames Controller
fps = pygame.time.Clock()
#Initialize menu
menu = pygame_menu.Menu('Snake', window_x, window_y, theme=pygame_menu.themes.THEME_DARK)
#elements menus
menu.add.button('Play', start_game)
menu.add.selector('Difficulty : ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Quit', pygame_menu.events.EXIT)

#run menu
menu.mainloop(game_window)
snake_speed, add = set_difficulty()