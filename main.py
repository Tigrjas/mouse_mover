import pyautogui
import random
import time

RUNTIME = time.time() + 10

while time.time() < RUNTIME:
    random_x = random.randint(0, 3440)
    random_y = random.randint(0, 1440)
    pyautogui.moveTo(random_x, random_y, 2)
