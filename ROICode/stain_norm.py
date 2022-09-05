from PIL import Image
from random import randint 
import PIL
import random
import openslide as ops 
import cv2 
#from torch.utils.data import Dataset, DataLoader
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.transforms.functional as F
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt 
from tiatoolbox.tools import patchextraction
import time
import os
import copy
import numpy as np
from tiatoolbox.wsicore.wsireader import WSIReader
from tiatoolbox import utils
from tiatoolbox.wsicore.slide_info import slide_info
from tiatoolbox.wsicore import wsireader
from tiatoolbox import data
from tiatoolbox.tools import stainnorm
import skimage.color

def vahadane_stain_norm(image,target):
    io_image=Image.open(image)

    io_target = Image.open(target)
    io_image = np.array(io_image,dtype = np.uint8)
    io_target = np.array(io_target,dtype = np.uint8)
    
    #stain_matrix = skimage.color.fgx_from_rgb[:2]
    #custom_normalizer = stainnorm.CustomNormalizer(stain_matrix)
    #custom_normalizer.fit(io_target)

    stain_normalizer = stainnorm.get_normalizer('Reinhard')
    stain_normalizer.fit(io_target)
    return stain_normalizer.transform(io_image.copy())
UHCW_directory = 'roi_folder_3/'

UHCW_strings = list()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

for image_string in os.listdir(UHCW_directory):
    UHCW_strings.append(os.path.join(UHCW_directory+image_string))


#im_original = f'/mnt/user-temp/joseph-tia/MSDissertation/roi_folder/4.jpg'
im_target = f'/mnt/user-temp/joseph-tia/MSDissertation/random/34.png'
count  = 0

for image_str in UHCW_strings:
    count += 1
    vahadane_stain = vahadane_stain_norm(image_str,im_target)
    vahadane_stain = Image.fromarray(vahadane_stain)
    vahadane_stain.save('/mnt/user-temp/joseph-tia/MSDissertation/stain_normed_3/'+str(count)+'.jpg', 'JPEG')