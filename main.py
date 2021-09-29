"""
Use
import pyautogui, sys
while True:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)
    sleep(1)
for your mouse cords
"""
__author__ = 'Jake CEO of annoyance#1904'

from random import randrange

from pyscreeze import locateCenterOnScreen
from pyautogui import onScreen, click, sleep, size, moveTo

groups_left = 0



class Leave:
    def __init__(self, x, y, log=False):
        self.groups_left = 0
        self._x = x
        self._y = y
        self.log = log
        self._errorcount = 0

    def click_x(self, x, y, delay: int):
        if onScreen(x, y):
            click(x, y, duration=delay)

    def click_leave(self, x, y):
        print('x', x, 'y', y)
        if onScreen(x, y):
            click(x, y)

    def run(self, times: int, delay: int = 0.1):
        global x, y
        sleep(3)
        for r in range(times):
            h, w = size()
            a, b = randrange(0, h), randrange(0, w)
            moveTo(a, b)
            self.click_x(self._x, self._y, delay=delay)
            sleep(delay)
            try:
                x, y = locateCenterOnScreen('leave_group.png', minSearchTime=3) or locateCenterOnScreen('leave_group2.png', minSearchTime=3)
            except TypeError as e:
                if str(e) == 'TypeError: cannot unpack non-iterable NoneType object':
                    continue
            self.click_leave(x, y)
            if self.log:
                print(f'x {x}, y {y}')
            self.groups_left += 1
        if self.log:
            print(self.groups_left)


if __name__ == '__main__':
    lebe = Leave(285, 273, log=True)
    lebe.run(2000, delay=0)
