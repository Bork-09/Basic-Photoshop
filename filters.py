# mini_photoshop/filters.py

import cv2
import numpy as np

def blur(img):
    blur = cv2.GaussianBlur(img, (15,15), 0)
    return blur