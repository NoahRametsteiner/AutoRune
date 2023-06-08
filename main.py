import mouse
import random
import time
import csv
import keyboard
from varname import nameof
from python_imagesearch.imagesearch import *
from PIL import Image
import io
import csv
import numpy as np


# VARIABLES
cordToClickAt = []

# 5 seconds before program starts
time.sleep(5)


def CreateLookUpTable(CreateLookUpTableOfImage):
    img = Image.open("./LookUpImages/"+CreateLookUpTableOfImage+".jpg")
    pix = img.load()
    cordX, cordY = img.size
    arrayOfCords = []
    for counterX in range(cordX):
        for counterY in range(cordY):
            color = img.getpixel((counterX, counterY))
            if (color[0] == 0 and color[1] == 0 and color[2] == 0):
                arrayOfCords.append([counterX, counterY])

    # Write to csv
    file = open(r'./LookUpTables/'+CreateLookUpTableOfImage +
                '.csv', 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(arrayOfCords)


def RandomNumberFromZero(randomNumber):
    return random.randrange(randomNumber)


def RandomNumberBetweanTwoNumbers(number1, number2):
    return random.uniform(number1, number2)


def FindCordOfImage(image):
    image = "./SearchImages/"+image+".png"
    pos = imagesearch(image)
    if pos[0] != -1:
        cord = pos
        return cord
    else:
        print("error: position of "+image+" was not found!")
        exit()


def MoveMouseToCord(xCord, yCord):
    mouse.move(
        xCord-(mouse.get_position())[0],
        yCord-(mouse.get_position())[1],
        absolute=False,
        duration=RandomNumberBetweanTwoNumbers(0.1, 0.3)
    )


def WaitForImageToBeOnScreen(imageToSearch):
    while (imagesearch_count("./SearchImages/"+imageToSearch+".png") == 0):
        pass


def HandelingSkillLevelUp(imageToSearch):
    if (imagesearch_count("./SearchImages/"+imageToSearch+".png") > 0):
        time.sleep(0.3)
        AutoRune("FurnAtLvlUp")
        time.sleep(0.4)
        mouse.click("left")
        time.sleep(1)
        keyboard.press('space')


def WaitForImageToBeOffScreen(imageToSearch):
    while (imagesearch_count("./SearchImages/"+imageToSearch+".png") != 0):
        HandelingSkillLevelUp("RefLevelUp")


def ReadInLookUpTable(ReadLookUpTable):
    # Read from csv
    if (len(cordToClickAt) != 0):
        cordToClickAt.clear()

    openFile = io.open("./LookUpTables/"+ReadLookUpTable+".csv", mode="r")
    for line in openFile:
        splitString = line.split(",")
        stripString = splitString[1].strip("\n")
        cordToClickAt.append([splitString[0], stripString])
    openFile.close()


def AutoRune(imageToSearch):

    # If you have more monitors.
    # If only one monitor, set both to zero!
    monitorOffset = [1920, 1080]
    ReadInLookUpTable(imageToSearch)
    cord = FindCordOfImage(imageToSearch)
    index = RandomNumberFromZero(len(cordToClickAt))
    MoveMouseToCord(
        cord[0]+int(cordToClickAt[index][0])-monitorOffset[0],
        cord[1]+int(cordToClickAt[index][1])-monitorOffset[1]
    )
    print("ClickLog:")
    print(cordToClickAt[index])
    print(cord[0]+int(cordToClickAt[index][0])-monitorOffset[0],
          cord[1]+int(cordToClickAt[index][1])-monitorOffset[1])
    print()


CreateLookUpTable("Furn")
CreateLookUpTable("FurnAtLvlUp")
CreateLookUpTable("Gold")
CreateLookUpTable("Bank")
CreateLookUpTable("Sap")
CreateLookUpTable("SapAmulet")


while True:

    # Get Items From Bank:
    AutoRune("Gold")
    mouse.click("left")
    AutoRune("Sap")
    mouse.click("left")

    # Go to furnace
    time.sleep(0.1)
    AutoRune("Furn")
    time.sleep(0.3)
    mouse.click("left")
    time.sleep(1)

    # Wait to be at the furnace
    WaitForImageToBeOnScreen("WhatWouldYouLikeToMake")
    time.sleep(0.3)
    keyboard.press('space')

    # Wait to be finished
    WaitForImageToBeOffScreen("Gold")

    # Go back to the bank
    AutoRune("Bank")
    time.sleep(0.3)
    mouse.click("left")
    WaitForImageToBeOnScreen("Trash")

    # Deposit
    AutoRune("SapAmulet")
    mouse.click("left")
