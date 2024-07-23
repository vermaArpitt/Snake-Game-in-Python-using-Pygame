import pygame as p

p.init()

def main():
    exit_game = False
    game_over = False
    screen = p.display.set_mode((500, 750))
    p.display.set_caption("Flappy Bird")

    while not exit_game:
        for event in p.event.get():
            if event.type == p.QUIT:
                exit_game = True

p.quit()

if __name__ == "__main__":
    main()