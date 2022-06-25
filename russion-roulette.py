from random import randint
from sys import platform
import time
import os

bullet_slots = 6
bullet_position = randint(1, bullet_slots)
current_slot = randint(1, bullet_slots)

def shootdown():
  time.sleep(2)
  if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
    os.system('shutdown now -h')
  elif platform == 'win32':
    os.system('shutdown /s /t 1')

print('\nWelcome to Russian Roulette, let\'s play the game.\n')

while True :
  input("Enter to shoot...")
  if current_slot == bullet_position:
    print('DORR!! You die.\n')
    shootdown()
    break
  else:
    print('Click.\n')
    current_slot += 1
    if current_slot > bullet_slots:
      current_slot = 1
