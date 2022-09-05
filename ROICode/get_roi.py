from PIL import Image
from random import randint 

import random
import openslide as ops 

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

#plt.style.use('seaborn')

print('hello')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def get_rois(list_of_roi_cords, wsi_loc):
    wsi_obj = ops.OpenSlide(wsi_loc)
    rois =  list()
    for cord in list_of_roi_cords:
        img = wsi_reader_v1.read_bounds(cord, resolution=0, units="level")
        rois.append(img)
    return rois

wsi_path = f'X'
wsi_reader_v1 = WSIReader.open(input_img=wsi_path)

ipath_bounds_dict = {
    f'X': [[26661, 108025, 29154, 110513],[50887,98094, 53405, 100595]],
    f'X': [[41800,87510,44292,90007],[48108,86317,50610, 88781]]
    
}


count = 0
for key, values in ipath_bounds_dict.items():
    
    wsi_path = key
    wsi_reader_v1 = WSIReader.open(input_img=wsi_path)
    wsi_info = wsi_reader_v1.info.as_dict()
    
    for item in values:
        count += 1
        bounds = item
        img = wsi_reader_v1.read_bounds(bounds, resolution=0, units="level")
        im = Image.fromarray(img)
        print(np.array(im).shape)
        im1 = im.save("roi_folder_3/"+str(count)+".jpg")

#images = get_rois()

#plt.imshow(images[0])
