# mini_photoshop/main.py

import argparse
import cv2
import os
from filters import blur
def main():

    # Parsing the command arguments

    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--filter', help='Applying blur filter')
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if args.filter == 'blur':
        blurry = blur(img)
        cv2.imshow("Filtered img", blurry)
        cv2.waitKey(5000)

if __name__ == "__main__":
    main()
