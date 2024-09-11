import os
import time

import pygame # Windows + R > pip3 install pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    user_input = input("Hit Enter to Exit: ")

    if user_input == "": 
      pygame.mixer.pause()
      break
    else: 
      continue 

def menu(): 
  print("Welcome to the music player!\n")
  time.sleep(.5)
  print("Press 1 to Play")
  time.sleep(.5)
  print("Press 2 to Exit")
  time.sleep(.5)
  print()
  print("Press anything else to see the menu again")
  print()
  time.sleep(.5)

while True:
  # clear the screen 
  os.system("cls") # "cls" for windows "clear" for Unix/Max/Linux

  # Show the menu
  menu()

  # take user's input
  user_input = input("Enter your choice: ")
  print()

  # check whether you should call the play() subroutine depending on user's input
  if user_input == "1":
    print("Playing some proper tunes!\n")
    play()
  elif user_input == "2":
    print("Exiting the music player!\n")
    exit()
  else: 
    continue 