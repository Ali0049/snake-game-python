import pygame
from random import randint
pygame.init()

#colors
white = (255, 255, 255)
red =   (255, 0, 0)
black = (0,0,0)
screen_width = 800
screen_height = 500
#creating window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("SnankeWithAli")


#Game Specific Variables
exit_game = False
game_over = False
snake_x = randint(1,screen_width)
snake_y = randint(1,screen_height)
velocity_x = 1
velocity_y = 1  
init_velocity = 2
food_x = randint(0,screen_width/2)
food_y = randint(0,screen_height/2)
food_size = 20
score = 0
snake_size = 20
fps = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)
def text_screen(text, color, x, y):
    '''for score printing on screen of game '''
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color, [x , y , snake_size , snake_size])
snake_list = []
snake_length = 1
#Game Loop
def gameloop ():
    exit_game = False
    game_over = False
    snake_x = randint(1,screen_width)
    snake_y = randint(1,screen_height)
    velocity_x = 1
    velocity_y = 1  
    init_velocity = 2
    food_x = randint(0,screen_width/2)
    food_y = randint(0,screen_height/2)
    food_size = 20
    score = 0
    snake_size = 20
    fps = 60
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None,55)
    snake_list = []
    snake_length = 1    
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game over! Press Enter To continue",red,50,300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()    
        else:
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y =  init_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
            if abs(snake_x-food_x)<8 and abs(snake_y-food_y )<8:
                score += 1
                food_x = randint(0,screen_width/2)
                food_y = randint(0,screen_height/2)
                snake_length += 5
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y> screen_height:
                game_over = True
                print("Game over")

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y 
            gameWindow.fill(white)
            
            plot_snake(gameWindow, black ,snake_list, snake_size)
            
            
            pygame.draw.rect(gameWindow, red, [food_x, food_y,food_size ,food_size])
            text_screen("Score: "+ str (score*10), red, 5, 5)
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]                
            if head in snake_list[:-1]:
                game_over = True            
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop ()