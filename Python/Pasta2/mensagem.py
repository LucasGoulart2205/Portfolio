import pyautogui as spam
import time

limite= input('Numero de msgs: ')
msg= input('Coloque a msg: ')

i= 0

time.sleep(2)
while i<int(limite):
    spam.typewrite(msg)
    spam.press('Enter')
    i+=1