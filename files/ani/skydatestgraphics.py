#skydatestgraphics.py
import pygame, player, sys, link

pygame.init()
screen = pygame.display.set_mode([768,768])
clock = pygame.time.Clock()
link = link.Player()
rate = 6
dx = dy = 0
posx = posy = 0

def animate():
  screen.fill([255,255,255])
  screen.blit(link.image, link.rect)
  pygame.display.update()

while True:
  clock.tick(30)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    #dx = dy = 0
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: dx = -rate
    elif event.type == pygame.KEYUP   and event.key == pygame.K_LEFT: dx = 0
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: dx = rate
    elif event.type == pygame.KEYUP   and event.key == pygame.K_RIGHT: dx = 0
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: dy = -rate
    elif event.type == pygame.KEYUP   and event.key == pygame.K_DOWN: dy = 0
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP: dy = rate
    elif event.type == pygame.KEYUP   and event.key == pygame.K_UP: dy = 0
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      pygame.quit()
      sys.exit()
    print('link pos: ' + str(posx) + ' ' + str(posy))
  posx += dx
  posy += dy
  link.move(dx, dy)
  animate()
