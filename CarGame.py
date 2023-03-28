###########################################################
#
#
#
#
#
#
#
###########################################################




import pygame, sys
from pygame.locals import QUIT

pygame.init()

# create window
win_size = width, height = (1000, 1000)
win = pygame.display.set_mode(win_size)
pygame.display.set_caption('My Car Game!')

# road dimenssions
road_w = int(width / 1.6)
road_cord = ((width / 2 - road_w / 2), 0, road_w, height)
rd_mark_w = (width / 100)
center_mark_cord = ((width / 2 - road_w / 2), 0, road_w, height)
left_mark_cord = ((width / 2 - road_w / 2 + rd_mark_w*2), 0, road_w, height)
right_mark_cord = ((width / 2 + road_w / 2 - rd_mark_w*2), 0, road_w, height)

# colors



# game loop
runing = True
while runing:
  for event in pygame.event.get():
    if event.type == QUIT:
        runing = False

  # draw the grass
  win.fill("green")

  # draw the road
  pygame.draw.rect(win, "gray", road_cord)

  # draw the road
  pygame.draw.rect(win, "gray", left_mark_cord)
  pygame.draw.rect(win, "gray", right_mark_cord)
  
  pygame.display.update()
pygame.quit()

