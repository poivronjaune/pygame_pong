import sys
import random
import pygame

pygame.init()
screen_width = 1280
screen_height = 800

class Speed:
    def __init__(self, x=0, y=0):
        self.x_velocity = x
        self.y_velocity = y
        self.min = 0
        self.max = 5

class Ball:
    def __init__(self, width=30, height=30):
        self.width = width
        self.height = height
        self.ball = pygame.Rect(0,0,self.width,self.height)
        self.speed = Speed()
        
        self.reset()

    def reset(self):
        self.ball.x = screen_width / 2 - 10
        self.ball.y = random.randint(10, screen_height - 10)
        self.speed.x_velocity *= random.choice([self.speed.min * -1, self.speed.max])
        self.speed.y_velocity *= random.choice([self.speed.min * -1, self.speed.max])        
    
    def animate(self):
        self.ball.x += self.speed.x_velocity
        self.ball.y += self.speed.y_velocity

    def draw(self, screen):
        pygame.draw.ellipse(screen, 'white', self.ball)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game OOP")
clock = pygame.time.Clock()

ball = Ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    ball.draw(screen)

    pygame.display.update()
    clock.tick(60)
    