import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((300, 300))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 30)
txt = "wait..."
txt2 = "Key Down!"

while True:
     SCREEN.fill((255, 255, 255))

     for event in pygame.event.get():
          if event.type == QUIT :
               pygame.quit()
               sys.exit()

     key_event = pygame.key.get_pressed()
     if key_event[pygame.K_LEFT]:
          txt = "Left" + txt2
     if key_event[pygame.K_RIGHT]:
          txt = "Right" + txt2
     if key_event[pygame.K_UP]:
          txt = "Up" + txt2
     if key_event[pygame.K_DOWN]:
          txt = "Down" + txt2
     if key_event[pygame.K_ESCAPE]:
          txt = "Escape" + txt2
          pygame.quit()
          sys.exit()
     

     msg = sysfont.render(txt, True, (255, 0, 255))
     SCREEN.blit(msg, (50, 100))
     pygame.display.update()
     CLOCK.tick(60)
