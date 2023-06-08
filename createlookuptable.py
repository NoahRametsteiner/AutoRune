from PIL import Image
import numpy as np
import json
import pandas

CreateLookUpTable = "Gold"

img = Image.open("./LookUpImages/"+CreateLookUpTable+".jpg")
pix = img.load()
cordX,cordY = img.size
arrayOfCords = []
for counterX in range(cordX):
    for counterY in range(cordY):
        color = img.getpixel((counterX,counterY))
        if(color[0] == 0 and color[1] == 0 and color[2] == 0):
            arrayOfCords.append([counterX,counterY])
            
#Write to csv
import csv 
import numpy as np
file = open(r'./LookUpTables/'+CreateLookUpTable+'.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(arrayOfCords) 


#Read from csv
import io
cordToClickAt = []
f = io.open("./LookUpTables/"+CreateLookUpTable+".csv", mode="r")
for line in f:
    splitString = line.split(",")
    stripString = splitString[1].strip("\n")
    cordToClickAt.append([splitString[0], stripString])
