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
from pygame.locals import *
from pgu import gui
import random

'''
from bs4 import * 
import requests

text= "web scraping"
url = 'https://google.com/search?q=' + text
request_result=requests.get( url )

soup = bs4.BeautifulSoup(request_result.text, "html.parser")
'''
import googlesearch

pygame.init()

# create window
win_size = width, height = (500, 500)
win = pygame.display.set_mode(win_size)
pygame.display.set_caption('My Car Game!')

# button class
class Button:
  def __init__(self, text, x_cord, y_cord):
    self.color = ""
    self.textcolor = ""
    self.text = text
    self.x_cord = x_cord
    self.y_cord = y_cord
"""
start = Button("start", x_cord, y_cord)
instruction = Button("Instruction", x_cord, y_cord)
quit = Button("Quit", x_cord, y_cord)
try_again = Button("Try_again!", x_cord, y_cord)
next = Button("Next!", x_cord, y_cord)
"""
class Popup:
  def __init__(self, text):
    self.text = text
    self.title = gui.Label("Game Status")




# road dimenssions
road_w = int(width / 1.6)
road_cord = ((width / 2 - road_w / 2), 0, road_w, height)
rd_mark_w = (width / 100)
center_mark_cord = ((width / 2 - road_w / 2), 0, road_w, height)
left_mark_cord = ((width / 2 - road_w / 2 + rd_mark_w * 2), 0, rd_mark_w, height)
right_mark_cord = ((width / 2 + road_w / 2 - rd_mark_w * 2), 0, rd_mark_w, height)
num1_mark_cord = ((width / 2 + road_w / 6), 0, rd_mark_w, height)
num2_mark_cord = ((width / 2 - road_w / 6), 0, rd_mark_w, float(height))

# cars
# player car
car = "To be scraped" # how to scrape it
car_loc = (width / 2 + road_w / 4, height * .7)
car_move_cord = [int(road_w) / 2, 0]

car1 = pygame.image.load("enemy_car.png")
img_size = (road_w*2, height)
car1 = pygame.transform.scale(car1, img_size)
car1 = pygame.transform.flip(car1, False, True)
car_loc1 = (a, d) = (road_w/3, height * .3)

# enemy car
# https://img1.pnghut.com/24/21/23/m4KqBmb8JW/google-simulation-video-game-car-3-pandas-in-brazil-unblocked-games.jpg
car2 = pygame.image.load("enemy_car.png")
img_size = (road_w*2, height)
car2 = pygame.transform.scale(car2, img_size)
car_loc2 = (x, y) = (-road_w/3, -height * .3)

# game loop
runing = True
while runing:
  for event in pygame.event.get():
    if event.type == QUIT:
      runing = False

    # move player car
    if event.type == KEYDOWN:  # it doesn't turn properly # aslo add restrictions
      if event.key in [K_a, K_LEFT] and a > -int((width / 2 - road_w / 2)):
        a -= (int((width / 2 - road_w / 2)))
        print(-int((width / 2 - road_w / 2)))
        car_loc1 = (a-int(road_w/3), d)
      if event.key in [K_d, K_RIGHT] and d > int((width / 2 - road_w / 2)):
        car_loc1 = a+int(road_w/3), d

  # draw the first opening page

  # draw the grass
  win.fill("green")

  # draw the road
  pygame.draw.rect(win, "black", road_cord)

  # draw the road
  pygame.draw.rect(win, "yellow", left_mark_cord)
  pygame.draw.rect(win, "yellow", right_mark_cord)
  pygame.draw.rect(win, "white", num1_mark_cord) # I want it to e dashed
  pygame.draw.rect(win, "white", num2_mark_cord)
  """
  # make dashed lines
  for i in range(5):
      pygame.draw.rect(win, "white", num2_mark_cord)
      pygame.draw.rect(win, "red", num2_mark_cord)
  """

  # crash
  if a == x and y > d: # how do I align it perfectly
    break


  # animation
  list  = [(-road_w/3), (0), (road_w/3)]
  y  += 1
  if y > height:
    y = -height * .3
    x = random.choice(list)
    car_loc2 = (x, height)

  # car
  #win.blit(car, car_loc)
  win.blit(car1, car_loc1)
  win.blit(car2, (x, y))

  pygame.display.update()
pygame.quit()
