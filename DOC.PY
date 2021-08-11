""" Google doc filler/spammer by Jake CEO of annoyance#1904"""
from pyautogui import *

PATH = "whattosay.txt"  # str(input("Please enter the name of your file"))
FILE = open(PATH, mode="r+", encoding="UTF-8")
GOOGLE_DOC_INPUTS = 14
KEY = 'tab'


def Generator(File):
    for line in File.read().split("\n"):
        yield line


def main(file):
    time.sleep(5)
    g = Generator(file)
    k = KEY
    press(k, presses=2)
    write(next(g))
    time.sleep(.5)
    # tab tab (text)
    press(k)
    write(next(g))
    time.sleep(.5)
    # tab (text)
    press(k, presses=7, interval=0.25)
    time.sleep(.5)
    # tab tab tab tab tab tab tab
    press('space')
    write(next(g))
    time.sleep(.5)
    # spacebar (text)
    press(k)
    write(next(g))
    time.sleep(.5)
    # tab (text)
    press(k)
    press('space')
    time.sleep(.5)
    # tab spacebar
    press('down')
    press('enter')
    press('tab')
    time.sleep(.5)
    # downarrorw enter tab
    write(next(g))
    press(k)
    # (text) tab
    press(['space', 'tab'], presses=3)
    # spacebar tab spacebar tab spacebar tab
    write(next(g))
    press(k)
    time.sleep(.5)
    write(next(g))
    press(k)
    write(next(g))
    time.sleep(.5)
    press(k)
    write(next(g))
    time.sleep(.5)
    press(k)
    write(next(g))
    press(k)
    write(next(g))
    time.sleep(.5)
    press(k)
    write(next(g))
    press('enter')
    time.sleep(2)
    # (text) tab (text) tab (text) tab (text) tab (text) tab enter


def runmanytimes(times):
    for x in range(times):
        main(FILE)
        press('browserrefresh')
        press('enter')


""" to run again) tab enter tab"""
if __name__ == __name__:
    runmanytimes(40)
