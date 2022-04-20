from __future__ import division
from asyncio import run_coroutine_threadsafe
from re import X
from turtle import width
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored
import cv2
import random

I = Image.open("image.jpeg")
I = I.convert("RGB")

datas = I.getdata()

new_image_data = []

# width, height = I.size

# pixel_size = width * height
x = random.randint(0, 250)
y = random.randint(0, 250)
z = random.randint(0, 250)
for item in datas:
    if item[0] in list(range(random.randint(0, 256), random.randint(0, 256))):

        
        new_image_data.append((x, y, z))
    else:
        new_image_data.append(item)

I.putdata(new_image_data)

I.save("image1.jpeg")




