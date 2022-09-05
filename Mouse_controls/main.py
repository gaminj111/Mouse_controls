import pyautogui
import time
print('Where do you want mouse to be:(middle,right,left) and what height(up,middle,down)ex:right,up or middle,middle')
a=input('   ')
#a=input('Where do you want mouse to be:(middle,right,left) and what height(up,middle,down)ex:right,up or middle,middle')

if str(a.lower()) == ('middle,middle'):
    pyautogui.moveTo(960, 540)
elif str(a.lower()) == ('middle,up'):
    pyautogui.moveTo(960, 216)
elif str(a.lower()) == ('middle,down'):
    pyautogui.moveTo(960, 864)


elif str(a) == ('right,middle'):
    pyautogui.moveTo(192, 540)
elif str(a) == ('right,up'):
    pyautogui.moveTo(192, 216)
elif str(a) == ('right,down'):
    pyautogui.moveTo(192, 864)

elif str(a) == ('right,middle'):
    pyautogui.moveTo(1728, 540)
elif str(a) == ('right,up'):
    pyautogui.moveTo(1728, 216)
elif str(a) == ('right,down'):
    pyautogui.moveTo(1728, 864)
else:
    print('I did not understand pls use the model "right,middle"')


