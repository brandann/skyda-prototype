import pygame, sys

class Player(pygame.sprite.Sprite):
  def __init__(self, u, d, l, r):
    pygame.sprite.Sprite.__init__(self)
    self.ani_up = u
    self.ani_down = d
    self.ani_left = l
    self.ani_right = r
    self.images = self.ani_down
    self.image = pygame.image.load(self.images[0])
    self.rect = self.image.get_rect()
    self.rect.center = [100,100]
    self.ani_pos = 0

  def move(self, dx, dy):
    if dx > 0: self.images = self.ani_right
    elif dx < 0: self.images = self.ani_left
    elif dy > 0: self.images = self.ani_up
    elif dy < 0: self.images = self.ani_down
    #else: self.ani_pos = 0
    if dx or dy != 0:
      self.ani_pos += 1
      print('move: ' + str(dx) + " " + str(dy) + " " + str(self.ani_pos))
      if self.ani_pos >= len(self.images): self.ani_pos = 0
      self.rect.centerx += dx
      self.rect.centery += -dy
    else:
      self.ani_pos = 0
    self.image = pygame.image.load(self.images[self.ani_pos])
    self.image = pygame.transform.smoothscale(self.image, (16*3,16*3))

down1 = ('link_down1.png')
down2 = ('link_down2.png')
up1   = ('link_up1.png')
up2   = ('link_up2.png')
left1 = ('link_left1.png')
left2 = ('link_left2.png')
right1 = ('link_right1.png')
right2 = ('link_right2.png')

link_U = []
link_D = []
link_L = []
link_R = []

link_U.append(up1)
link_U.append(up2)
link_D.append(down1)
link_D.append(down2)
link_L.append(left1)
link_L.append(left2)
link_R.append(right1)
link_R.append(right2)
