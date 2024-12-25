import time
import random
import keyboard
import pyautogui

DESIRED_WPM = 105  # Words per minute

TARGET_CPS =(DESIRED_WPM/10 * (DESIRED_WPM * 6.1) / 60) # 6 includes avg length of 5.1 characters per word and 1 space


def human_type(text):
	for char in text:
		if keyboard.is_pressed('f10'):  # Check for F10 press
			break
		time.sleep(1 / TARGET_CPS * random.uniform(0.8, 1.2))
		
		if random.random() < 0.05:  # 5% chance of error
			typo_char = random.choice(list("abcdefghijklmno!0#(%*Cpqrstuvwxyz"))
			pyautogui.typewrite(typo_char)
			time.sleep(random.uniform(0.1, 0.3))
			pyautogui.press("backspace")  # Correct the typo
		
		pyautogui.typewrite(char)


TEXT = """Enter random text here"""
if __name__ == "__main__":
	time.sleep(2)
	human_type(TEXT)
