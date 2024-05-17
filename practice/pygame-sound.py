import pygame

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/done.wav")
    pygame.mixer.music.play()


play_sound()