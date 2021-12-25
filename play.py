# -*- coding: utf-8 -*-

import pygame, time

pygame
pygame.init()
pygame.mixer.init()
f = open('./data/Beep.mp3')
f2 = open('./data/Beep.mp3')

def play(filename):
    global pygame
    global f, f2
    f = open('./data/'+str(filename)+'.wav')
    f2 = open('./data/Beep.mp3')
    pygame.mixer.music.load(f2)
    pygame.mixer.music.play()
    time.sleep(4)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f)
    pygame.mixer.music.play()

def stop():
    global pygame
    global f, f2
    pygame.mixer.music.stop()
    f.close()
    f2.close()
