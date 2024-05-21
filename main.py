import pyautogui
import random
import time

# Constants
RUNTIME = time.time() + 10


def move_mouse():
    random_x = random.randint(0, 3440)
    random_y = random.randint(0, 1440)
    pyautogui.moveTo(random_x, random_y, 2)


def pause_mouse():
    time.sleep(random.randint(1, 3))


def main():
    # Dictionary of possible actions
    mydict = {
        "move": move_mouse,
        "pause": pause_mouse,
    }

    # Choosing a random action and running for a specific time
    while time.time() < RUNTIME:
        random.choice(list(mydict.values()))()


if __name__ == "__main__":
    main()
