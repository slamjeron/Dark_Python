from PIL import Image
import pyautogui

con = pyautogui


def brighter(plxs):
    red, blue, green = plxs
    return red > 30 and blue > 30 and green > 30


def boxClr(pix):
    red, blue, green = pix
    return red > 251 and green > 187 and blue > 103 and green < 199 and blue < 230


def findBox(image1):
    pix = image1.load()
    width, height = image1.size
    print(width)
    for x in range(0, width, 1):
        for y in range(0, height, 1):
            if not boxClr(pix[x, y]):
                image1.putpixel((x, y), (0, 0, 0))

    return image1


img = findBox(Image.open("bonesBox.png"))
img.save("bonesBox1.png")

img = findBox(Image.open("darkimage.png"))
img.save("darkimage1.png")
