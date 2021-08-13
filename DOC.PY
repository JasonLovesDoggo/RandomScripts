""" Google doc filler/spammer by Jake CEO of annoyance#1904"""

from pyautogui import *
from tkinter import *
from urllib.request import urlopen
import io
import base64
import webbrowser

PATH = "whattosay.txt"  # str(input("Please enter the name of your file"))
FILE = open(PATH, mode="r+", encoding="UTF-8")
GOOGLE_DOC_INPUTS = 14
KEY = 'tab'
canrun = False
timesran = 0
def Generator(File):
    for line in File.read().split("\n"):
        yield line
g = Generator(FILE)
time.sleep(2)

def main(file):
    time.sleep(1.5)
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
    press('down') #This is for the "How old are ou"
    press('down')
    press('down')
    press('down')
    press('down')
    press('down')
    press('enter')
    time.sleep(.5)
    # downarrorw enter tab
    press(k)
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
    time.sleep(1)
    # (text) tab (text) tab (text) tab (text) tab (text) tab enter


def runmanytimes(times):
    for x in range(times):
        timesran + 1
        text = f"times ran {timesran}"
        print(text, end='')
        print('\b' * len(text), end='', flush=True)
        try:
            main(FILE)
            press('browserrefresh')
            press('enter')
            press('pageup')
            sleep(.5)
            
            click(clicks=1) 
        except StopIteration:
            press('browserrefresh')
            press('enter')
            press('pageup')
            sleep(.5)
            click(clicks=1) 
            g = Generator(FILE)         
            main(FILE)



def startthis():
    print(f'Hello, {os.getlogin()}! How are you?')
    runmanytimes(1200)

def stop():
    print("\nstopped")
    exit()

canv = Tk()
canv.title("RelaxCraft Doc spammer")
canv.geometry('370x170')
btn1 = Button(canv,
            text='Start',
            command=startthis,
            bg='#7289da',            
            fg='#ffffff',
            height = 7, 
            width = 15)
btn2 = Button(canv,
            text='Stop',
            command=stop,
            bg='#e96060',            
            fg='#ffffff',
            height = 7, 
            width = 15)
image_url = "https://cdn.discordapp.com/icons/694604110665613342/19f0085df1176f07400ddf021dbdc01e.jpg"
webbrowser.open_new_tab("http://bitly.ws/g2My")

canv.configure(bg='#282b30')
btn1.place(x=25, y=22) 
btn2.place(x=225, y=22)   
canv.mainloop()
