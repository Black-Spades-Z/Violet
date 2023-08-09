#Importing Libraries

import pyautogui as pg
import numpy as np
import cv2
import pyscreeze

#Creating objects


pg.hotkey('win', 'd')
pg.PAUSE = 2

screenshot = pg.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

telegram = pg.locateOnScreen('images/postman.png', confidence = 0.8)
print(telegram)
try:
    cv2.rectangle(
        screenshot,
        (telegram.left, telegram.top),
        (telegram.left + telegram.width, telegram.top + telegram.height),
        (0, 255, 255),
        2
    )
    cv2.imshow('Screenshot', screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    print('Could not find')
    AttributeError




