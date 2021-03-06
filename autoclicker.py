
import pyautogui
from pynput.keyboard import *
import random
import numpy as np
import os

#for detectChanges
from PIL import ImageChops # $ pip install pillow
from pyscreenshot import grab
from telethon.tl.types import messages # $ pip install pyscreenshot
import time

#for tele
import telegram_send
import telebot

#for mouse logger
from pynput.mouse import Listener
import logging

#thread
import threading


#  ======== settings ========
delay = 45  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

pause = True
running = True

xyList = []


def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')

def detectChanges():


    textFileHandling()

    #2DArrayFormat
    #0: To click on teams
    #1: Top Left Bounding Box
    #2: Bottom Right Bounding Box
    #3: First Chat
    #4: Second Chat
    #5: Third Chat
    #6: Idle Clicking Position

    while True: # http://effbot.org/zone/pil-comparing-images.htm
        
        im = grab(bbox=(int(xyList[1][0]), int(xyList[1][1]), int(xyList[2][0]), int(xyList[2][1])))
        diff = ImageChops.difference(grab(bbox=(int(xyList[1][0]), int(xyList[1][1]), int(xyList[2][0]), int(xyList[2][1]))), im)
        bbox = diff.getbbox()
        

        if bbox is not None: # exact comparison
            print("bounding box of non-zero difference: %s" % (bbox,))
            # superimpose the inverted image and the difference
            test = ImageChops.screen(ImageChops.invert(im.crop(bbox)), diff.crop(bbox))
            xCenter = (bbox[2]- bbox[0])/2
            yCenter = (bbox[3]- bbox[1])/2
            print(xCenter, yCenter)
            pyautogui.click(int(xyList[3][0]), int(xyList[3][1]))
            time.sleep(1)
            finalScreenshot = grab()
            finalScreenshot = finalScreenshot.save("image.jpg")
            
            #telegram_send.send(messages=["Wow that was easy!"])
            with open("image.jpg", "rb") as f:
                telegram_send.send(images=[f])
        
        else:
            pyautogui.click(int(xyList[6][0]), int(xyList[6][1]))
            

            
            #finalScreenshot.show()

def mouselogger():

    #logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
    logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format= '%(message)s')

    def on_move(x, y):
        #logging.info("Mouse moved to ({0}, {1})".format(x, y))
        pass

    def on_click(x, y, button, pressed):
        if pressed:
            #logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
            logging.info('{0},{1}'.format(x,y))

    def on_scroll(x, y, dx, dy):
        #logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
        listener.stop()

    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

def telebotReply():

    #2DArrayFormat
    #0: To click on teams
    #1: Top Left Bounding Box
    #2: Bottom Right Bounding Box
    #3: First Chat
    #4: Second Chat
    #5: Third Chat
    #6: Idle Clicking Position

    bot = telebot.TeleBot("5042340263:AAEJv2Q5hSexHrng_Koqhqc4AzeZ2XF0XTs")

    def handle_messages(messages):
        for message in messages:
            # Do something with the message
            print(message.text)
            bot.reply_to(message, 'Message Received')
            messageHolder = message.text

            #message format: #1:Your message (this means the first chat)
            #message format: #2:Your message (this means the second chat)
            #message format: #3:Your message (this means the third chat)

            if messageHolder[0] == "#":
                if messageHolder[1] == "1":
                    splitMessage = messageHolder.split(":")
                    pyautogui.click(int(xyList[3][0]), int(xyList[3][1]))
                    time.sleep(1)
                    pyautogui.write(splitMessage[1])
                    time.sleep(1)
                    pyautogui.press('enter')
                
                elif messageHolder[1] == "2":
                    splitMessage = messageHolder.split(":")
                    pyautogui.click(int(xyList[4][0]), int(xyList[4][1]))
                    time.sleep(1)
                    pyautogui.write(splitMessage[1])
                    time.sleep(1)
                    pyautogui.press('enter')

                elif messageHolder[1] == "3":
                    splitMessage = messageHolder.split(":")
                    pyautogui.click(int(xyList[5][0]), int(xyList[5][1]))
                    time.sleep(1)
                    pyautogui.write(splitMessage[1])
                    time.sleep(1)
                    pyautogui.press('enter')
                
            else: #default first
                    pyautogui.click(int(xyList[3][0]), int(xyList[3][1]))
                    time.sleep(1)
                    pyautogui.write(messageHolder)
                    time.sleep(1)
                    pyautogui.press('enter')

                

            


    bot.set_update_listener(handle_messages)
    bot.infinity_polling()

def textFileHandling():
    
    os.remove("mouse_log.txt")
    
    mouselogger()
    with open("mouse_log.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            if stripped_line[0].isalpha() == False:
                #print(stripped_line[0].isalpha())
                splitList = stripped_line.split(",")
                xyList.append(splitList)

    print(xyList)
    


def main():
    t1 = threading.Thread(target=telebotReply)
    t2 = threading.Thread(target=detectChanges)
    t1.start()
    t2.start()
    
    


if __name__ == "__main__":
    main()