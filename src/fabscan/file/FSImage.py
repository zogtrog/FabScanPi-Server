__author__ = "Mario Lukas"
__copyright__ = "Copyright 2015"

__license__ = "AGPL"
__maintainer__ = "Mario Lukas"
__email__ = "info@mariolukas.de"

import os
import cv2

from fabscan.FSConfig import Config

def save_images(imgs, prefix, dir_name="scans"):

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    prefix = os.path.join(dir_name, "%s_{0}" % prefix)
    for i, img in enumerate(imgs):
        i = str(i).zfill(3)
        cv2.imwrite(prefix.format(i) + ".jpg", img)


def save_image(img, number, prefix, dir_name="scans"):


    dir_name = Config.instance().folders.scans+dir_name
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    prefix = os.path.join(dir_name, "%s_{0}" % prefix)
    number = str(number).zfill(3)
    cv2.imwrite(prefix.format(number) + ".jpg", img)
    return prefix.format(number) + ".jpg"

def load_image(number, prefix, dir_name="scans"):
    dir_name =  Config.instance().folders.scans+dir_name
    prefix = os.path.join(dir_name, "%s_{0}" % prefix)
    number = str(number).zfill(3)
    if os.path.isfile(prefix.format(number) + ".jpg"):
        image = cv2.imread(prefix.format(number) + ".jpg")
        return image
    else:
        return None

