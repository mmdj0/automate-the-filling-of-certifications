import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import pandas as pd

#----------------------------
#fuction to drop the duplicates
def drop_dup(ary):
    res = []
    for i in ary:
        if i not in res:
            res.append(i)
    return (res)

items = []

with open('names_MKT - Feuille 1.csv') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        items.append(row[0])

items = drop_dup(items)

ln=len(items)
#-------------------------------
img= Image.open('certificate.jpg')
W,H = img.size
#img.show()
i=0
while i<ln:
    imgcp = img.copy()
    draw=ImageDraw.Draw(imgcp)
    font=ImageFont.truetype('/home/maroua/Documents/EB_Garamond/EBGaramond-VariableFont_wght.ttf',150)
    w1,h1=draw.textsize(items[i],font=font)
    draw.text(((W-w1)/2,(H-h1)/2),items[i],(0,0,0),font=font)
    
    imgcp.save(f'/home/maroua/Documents/omc_certif_final/omc_certif_mrkt/output_{i}.jpg')
    i+=1

