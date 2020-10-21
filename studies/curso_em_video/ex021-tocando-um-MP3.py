print()
from emoji import emojize

print(emojize(':notes: Tocador de MP3 :notes:', use_aliases=True))
import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# Para a música continuar tocando, foi necessário colocar a linha abaixo, senão ela para ao mover o mouse.
input()