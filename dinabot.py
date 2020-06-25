import time
import mss
import numpy
import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"{x},{y}")

    # Get raw pixels from the screen, save it to a Numpy array
    img = numpy.array(mss.mss().grab({"top": 260, "left": 503, "width": 80, "height": 35}))
    # img = numpy.array(mss.mss().grab({"top": y, "left": x, "width": 80, "height": 35}))

    if img.sum() != 2856000:
        pyautogui.press("space")
        time.sleep(.009)
    else:
        pass
