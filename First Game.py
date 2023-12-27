import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

running = True

image = pygame.image.load("ball.png").convert()

while running:

     for event in pygame.event.get():
          if event.type ==  pygame.QUIT:
               running = False
     pressed = pygame.key.get_pressed()
     if pressed[pygame.K_LEFT]:
          print("Left")
     if pressed[pygame.K_RIGHT]:
          print("Right")
     if pressed[pygame.K_UP]:
          print("UO")
     if pressed[pygame.K_DOWN]:
          print("Down")
     screen.blit(image,(0,0))
     pygame.display.flip() 


pygame.quit()

