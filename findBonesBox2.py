import pyautogui
from tkinter import *

con = pyautogui


def brighter(plxs):
    red, blue, green = plxs
    return red > 30 and blue > 30 and green > 30


def boxClr(pix):
    red, blue, green = pix
    return red > 251 and green > 187 and blue > 103 and green < 199 and blue < 230


def findBox():
    image = con.screenshot()
    pix = image.load()

    width, height = image.size
    for y in range(30, width - 50, 10):
        for x in range(100, height - 50, 10):
            if brighter(pix[x, y]):
                for x1 in range(x - 9, x + 60):
                    for y1 in range(y - 9, y + 60):
                        if boxClr(pix[x1, y1]):
                            con.moveTo(x1, y1)
                            return


page = Tk()
startBtn = Button(page, text="start", command=findBox)
startBtn.pack()
page.mainloop()
