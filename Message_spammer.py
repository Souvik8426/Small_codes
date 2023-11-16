#These are the modules time and random are inbuilt module but you have to install pyautogui
#command to install pautogui is 'pip install pyautogui'
import random
import pyautogui as pg
import time
spam = ('','')    #Enter the message you want to spam
name = ('','')    #This line is used to tag the user i have tested it in telegram and whatsapp dont forget to give a '@' before the name
time.sleep(8)
for i in range(5):
    a=random.choice(spam)
    b=random.choice(name)   #comment out this line if you dont want the tag feature
    pg.write(b)     #comment out this line if you dont want the tag feature
    pg.press("enter")   #comment out this line if you dont want the tag feature
    pg.write(" "+a)
    pg.press("enter")