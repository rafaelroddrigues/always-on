import pyautogui
import time
import random

def move_mouse():
    while True:
        # Move the mouse cursor 1 pixel in a random direction
        x, y = pyautogui.position()
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            pyautogui.moveTo(x, y - 1)
        elif direction == 'down':
            pyautogui.moveTo(x, y + 1)
        elif direction == 'left':
            pyautogui.moveTo(x - 1, y)
        elif direction == 'right':
            pyautogui.moveTo(x + 1, y)
        # Wait for 60 seconds
        time.sleep(60)

if __name__ == "__main__":
    move_mouse()