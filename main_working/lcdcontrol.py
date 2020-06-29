#sudo pkill fbcp #bug in pitft
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
specblue = (161,223,237)

surfaceSize = (480,320)
swissSize = (200,200)

pygame.init()
pygame.font.init()
#pygame.mouse.set_visible(False)

lcd = pygame.Surface(surfaceSize)
myfont = pygame.font.SysFont('Arial',25)



picture = pygame.image.load("1200x1189.png")
picture = pygame.transform.scale(picture,swissSize)


def refresh():
    f = open("/dev/fb1","wb")
    f.write(lcd.convert(16,0).get_buffer())
    f.close()

def toblack():
    lcd.fill(red)
    refresh()
def blank():
    lcd.fill(white)
    pygame.draw.rect(lcd, specblue, (0,270,480,50))
    pygame.draw.rect(lcd, specblue, (0,0,480,40))
    
    pygame.draw.line(lcd, white, (130,310),(130,320), 3)
    pygame.draw.line(lcd, white, (240,310),(240,320), 3)
    pygame.draw.line(lcd, white, (350,310),(350,320), 3)
    
    t = time.localtime()
    texttime = myfont.render(time.strftime("%H:%M",t),False, (255,255,255))
    lcd.blit(texttime,(200,5))
    
    calltext = myfont.render("Call",False, (255,255,255))
    lcd.blit(calltext,(110,275))
    deltext = myfont.render("Delete",False, (255,255,255))
    lcd.blit(deltext,(210,275))
    cleartext = myfont.render("Clear",False, (255,255,255))
    lcd.blit(cleartext,(320,275))
    refresh()
def waitscreen():
    blank()
    lcd.blit(picture, ((surfaceSize[0]/2)-(swissSize[0]/2),50))
    refresh()

def phone(phoneNum):
    blank()
    textphone = myfont.render(phoneNum, False, (0,0,0))
    lcd.blit(textphone, (0,150))
    refresh()

#toblack()

if __name__ == "__main__":
    waitscreen()
    
    #waitscreen()
#     Clock = pygame.time.Clock()
#     prevNum = "0"
#     for i in range(10):
#         prevNum = prevNum+str(i)
#         phone(prevNum)
#         #print(Clock.tick())#only 2-3 extra ms to update phone number
#         sleep(0.2)
#     sleep(1)
#     waitscreen()
    
