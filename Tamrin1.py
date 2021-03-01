# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:28:54 2020

@author: farimah
"""

from __future__ import division
import math
import sys
import pygame


class MyGame(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.bg_img = pygame.image.load('ufo.png')

        self.FPS = 30
        self.REFRESH = pygame.USEREVENT+1
        pygame.time.set_timer(self.REFRESH, 1000//self.FPS)


    def run(self):
        running = True
        while running:
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                running = False

            elif event.type == self.REFRESH:
                self.draw()

            else:
                pass         

    def draw(self):
        self.screen.fill(self.bg_img)

        pygame.display.flip()


MyGame().run()
pygame.quit()
sys.exit()