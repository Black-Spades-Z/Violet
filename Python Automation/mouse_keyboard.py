import pyautogui as pag

pag.hotkey('win', 'd')
print(pag.size())
# Creating Test Text File

pag.PAUSE = 1
pag.moveRel(40, 0)
pag.PAUSE = 1
pag.rightClick()
pag.moveRel(0, 300)
pag.PAUSE = 1
pag.moveRel(-300, 280)
pag.PAUSE = 0.5
pag.click()
pag.PAUSE = 0.5
pag.typewrite('Test', 0.2)
pag.press('enter', 2)
pag.PAUSE = 5
pag.typewrite('Done ', 0.25)


# Opening Telegram (Hot key)

# pag.hotkey('ctrl', 'alt', 't')
# pag.PAUSE = 5
# pag.moveRel(30, 30)
# pag.typewrite('2601', 0.2)
# pag.press('enter')

# Opening Telegram (Via Cursor)


