import pygame
from pygame.locals import *

import os
import random
from string import ascii_letters

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()
pygame.display.set_caption("Hangman")


class Hangman():
    def __init__(self):
        with open("./words.txt", "r") as file:
            # выбирает секретное слово
            words = file.read().split("\n")
            self.secret_word = random.choice(words)
            # передача длины секретного слова для создания пробелов в буквах
            self.guessed_word = "*" * len(self.secret_word)
        self.wrong_guesses = []
        self.wrong_guess_count = 0
        self.taking_guess = True
        self.running = True

        self.background_color = (155, 120, 70)
        self.gallow_color = (0,0,0)
        self.body_color = (255,253,175)

        self.font = pygame.font.SysFont("Courier New", 20)
        self.FPS = pygame.time.Clock()


    # рисует виселицу
    def _gallow(self):
        stand = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(75, 280, 120, 10))
        body = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(128, 40, 10, 240))
        hanger = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(128, 40, 80, 10))
        rope = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(205, 40,10, 30))


    # рисует части тела человека в случае каждой неверной догадки
    def _man_pieces(self):
        if self.wrong_guess_count == 1:
            head = pygame.draw.circle(screen, self.body_color, [210, 85], 20, 0)
        elif self.wrong_guess_count == 2:
            body = pygame.draw.rect(screen, self.body_color, pygame.Rect(206, 105, 8, 45))
        elif self.wrong_guess_count == 3:
            r_arm = pygame.draw.line(screen, self.body_color, [183, 149], [200, 107], 6)
        elif self.wrong_guess_count == 4:
            l_arm = pygame.draw.line(screen, self.body_color, [231, 149], [218, 107], 6),
        elif self.wrong_guess_count == 5:
            r_leg = pygame.draw.line(screen, self.body_color, [189, 198], [208, 148], 6),
        elif self.wrong_guess_count == 6:
            l_leg = pygame.draw.line(screen, self.body_color, [224, 198], [210, 148], 6)