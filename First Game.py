import pygame

#Init Pygame module
pygame.init()

#Get screen
screen = pygame.display.set_mode((400,400))

#endless loop variable set to true
running = True

image = pygame.image.load("ball.png").convert()

# Init the location of our Ball
x = 0
y = 0

#Init clock
clock = pygame.time.Clock()

while running:

     for event in pygame.event.get():
          if event.type ==  pygame.QUIT:
               running = False
     pressed = pygame.key.get_pressed()
     if pressed[pygame.K_LEFT]:
          print("Left")
          x -= 1
     if pressed[pygame.K_RIGHT]:
          print("Right")
          x += 1
     if pressed[pygame.K_UP]:
          print("Up")
          y-=1
     if pressed[pygame.K_DOWN]:
          print("Down")
          y+=1
     screen.fill((0,0,0))
     screen.blit(image,(x,y))
     pygame.display.flip() 
     clock.tick(60)


pygame.quit()

