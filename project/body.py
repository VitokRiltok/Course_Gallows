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