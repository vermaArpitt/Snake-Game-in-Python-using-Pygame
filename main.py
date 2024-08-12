import pygame as p
import random

p.init()
WIDTH = 1000
HEIGHT = 700

def display_text(screen, text, x, y, color, size):
     font = p.font.SysFont(None, size)
     img = font.render(text, True, color)
     screen.blit(img, [x,y])

def main():

    #Setting game screen
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Hungry Hungry Snake!")

    #Game variables
    exit_game = False
    game_over = False
    snakeX = 500
    snakeY = 350
    snakeSize = 25
    fps = 30
    init_Velocity = 6
    velocityX = init_Velocity
    velocityY = 0
    fruitX = 700
    fruitY = 350
    fruitSize = 25
    score = 0

    clock = p.time.Clock()
    #Game loop
    while not exit_game:           
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
        display_text(screen, "Score: " + str(score), 11, 11, "black", 55)
        display_text(screen, "Score: " + str(score), 10, 10, "yellow", 55)
        p.draw.rect(screen, "red", [fruitX, fruitY, fruitSize, fruitSize])
        p.draw.rect(screen, "black", [snakeX, snakeY, snakeSize, snakeSize])
        p.display.update()
        clock.tick(fps)

        #snake movement
        snakeX += velocityX
        snakeY += velocityY

        #spawning fruit after eating
        if(abs(snakeX - fruitX) <= 5 and abs(fruitY - snakeY) <= 5):
            fruitX = random.randint(0, WIDTH-fruitSize)
            fruitY = random.randint(70, HEIGHT-fruitSize)
            score += 1

    p.quit()

if __name__ == "__main__":
    main()