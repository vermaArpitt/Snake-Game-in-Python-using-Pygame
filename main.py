import pygame as p
import random

p.init()
WIDTH = 1000
HEIGHT = 700
fps = 30
clock = p.time.Clock()

def display_text(screen, text, x, y, color, size):
     font = p.font.SysFont(None, size)
     img = font.render(text, True, color)
     screen.blit(img, [x,y])

def draw_snake(screen, snakeList, color, snakeSize):
     for snakeX, snakeY in snakeList:
          p.draw.rect(screen, color, [snakeX, snakeY, snakeSize, snakeSize])

def gameLoop(screen):
    #Game variables
    exit_game = False
    game_over = False
    snakeX = 500
    snakeY = 350
    snakeSize = 25
    head = []
    snakeLength = 25
    snakeList = []
    init_Velocity = 6
    velocityX = init_Velocity
    velocityY = 0
    fruitX = 700
    fruitY = 350
    fruitSize = 25
    score = 0

    #Game loop
    while not exit_game:
        if game_over:
            display_text(screen, "Game Over!", 383, 253, "white", 65)
            display_text(screen, "Game Over!", 380, 250, "black", 65)
            display_text(screen, "Press Space to Retry", 400, 400, "black", 30)
            display_text(screen, "Press Enter to Return", 400, 450, "black", 30)

            for event in p.event.get():
                if event.type == p.QUIT:
                    exit_game = True

                elif event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        gameMenu(screen)
                    
                    elif event.key == p.K_SPACE:
                        gameLoop(screen)

        else:
            for event in p.event.get():
                if event.type == p.QUIT:
                    exit_game = True
                        
                elif event.type == p.KEYDOWN:
                    if event.key == p.K_RIGHT:
                        velocityX = init_Velocity
                        velocityY = 0

                    elif event.key == p.K_LEFT:
                        velocityX = -init_Velocity
                        velocityY = 0

                    elif event.key == p.K_UP:
                        velocityX = 0
                        velocityY = -init_Velocity

                    elif event.key == p.K_DOWN:
                        velocityX = 0
                        velocityY = init_Velocity

            screen.fill("green")

            #Displaying the score
            display_text(screen, "Score: " + str(score), 11, 11, "black", 55)
            display_text(screen, "Score: " + str(score), 10, 10, "yellow", 55)

            #Drawing the Fruit
            p.draw.rect(screen, "red", [fruitX, fruitY, fruitSize, fruitSize])

            #Handling game over
            if([snakeX, snakeY] in snakeList or snakeX < 0 or snakeX + snakeSize > WIDTH or snakeY < 0 or snakeY + snakeSize > HEIGHT):
                game_over = True

            #Drawing the snake
            head = [snakeX, snakeY]
            snakeList.append(head)

            if(len(snakeList) > snakeLength):
                del(snakeList[0])

            draw_snake(screen, snakeList, "black", snakeSize)

            #Snake movement
            snakeX += velocityX
            snakeY += velocityY

            #Spawning fruit after eating
            if(abs(snakeX - fruitX) <= 5 and abs(fruitY - snakeY) <= 5):
                fruitX = random.randint(0, WIDTH-fruitSize)
                fruitY = random.randint(70, HEIGHT-fruitSize)
                score += 1
                snakeLength += 1
                if(score % 10 == 0):
                    init_Velocity += 1
        
        p.display.update()
        clock.tick(fps)

    p.quit()

def gameMenu(screen):
    screen.fill("blue")
    display_text(screen, "Hungry Hungry Snake!", 255, 205, "black", 70)
    display_text(screen, "Hungry Hungry Snake!", 250, 200, "green", 70)

    display_text(screen, "__Press Space to Play__", 290, 350, "black", 50)

    exit_game = False
    while not exit_game:
        for event in p.event.get():
            if event.type == p.QUIT:
                    exit_game = True

            elif event.type == p.KEYDOWN:
                    if event.key == p.K_SPACE:
                        gameLoop(screen)

        p.display.update()
        clock.tick(fps)

    p.quit()   

def main():
    #Setting game screen
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Hungry Hungry Snake!")

    gameMenu(screen)

if __name__ == "__main__":
    main()