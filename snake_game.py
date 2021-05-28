import pygame
import random
from enum import Enum
from collections import namedtuple
pygame.init()

font  = pygame.font.Font('arial.ttf',25)

BLOCK_SIZE = 20
SPEED = 40

#rgb colors
WHITE = (255,255,255)
RED = (200,0,0)
BLUE1 = (0,0,255)
BLUE2 = (0,100,255)
BLACK = (0,0,0 )

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point','x, y')
class snakeGame:

    def __init__(self,w=640,h=480):
        self.w = w
        self.h = h
        #init display
        self.display = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()


        #init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2,self.h/2)

        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE,self.head.y),
                      Point(self.head.x - (2*BLOCK_SIZE),self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()
    

    def _place_food(self):
        x = random.randint(0,(self.w - BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0,(self.w - BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()
        

    def playStep(self):
    #1. collect user input

    #2. move

    #3. check if game over

    #4. place new food or jsut move

    #5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

    #6. return game over and score
        game_over = False
        return game_over, self.score
    
    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " , str(self.score), True, WHITE)
        self.display.blit(text,[0,0])
        pygame.display.flip()






if __name__ == '__main__':
    game = snakeGame()

    while True:
        game_over, score = game.playStep()

        if game_over:
            break

    print('Final Score: ',score)

    pygame.quit()