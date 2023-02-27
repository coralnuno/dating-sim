#BASIC SET UP FOR GAME 

#Importing and initiallizing pygame 
import pygame, sys 

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


            dt = self.clock.tick() / 1000
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run
    
