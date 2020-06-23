import pygame
import os
from time import sleep
from pygame import *
import time

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

surfaceSize = (480,320)
swissSize = (200,200)

os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV','/dev/fb1')
#os.environ["SDL_FBDEV"] = "/dev/fb1"

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)

#lcd = pygame.Surface(surfaceSize)
lcd = pygame.display.set_mode(surfaceSize, 0 , 16)
myfont = pygame.font.SysFont('Arial',20)



picture = pygame.image.load("1200x1189.png")
picture = pygame.transform.scale(picture,swissSize)


def refresh():
    f = open("/dev/fb1","wb")
    f.write(lcd.convert(16,0).get_buffer())
    f.close()

t = time.localtime()
def toblack():
    lcd.fill(black)
    refresh()
def blank():
    lcd.fill(white)
    rectangle = pygame.draw.rect(lcd, (161,223,237), (0,280,480,40))
    texttime = myfont.render(time.strftime("%H:%M",t),False, (255,255,255))
    lcd.blit(texttime,(420,290))
    refresh()
def waitscreen():
    blank()
    lcd.blit(picture, ((surfaceSize[0]/2)-(swissSize[0]/2),20))
    refresh()

def phone():
    pass

if __name__ == "__main__":
    waitscreen()
    