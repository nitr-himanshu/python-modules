import numpy as np
from PIL import Image 

def makeTiles(img,size):
    '''Take input img and return tiles(non-overlapping) of given size
        img should be numpy array
        size should be tuple
    '''
    res = []
    th = size[0]
    tw = size[1]
    img_height = img.shape[0]
    img_width = img.shape[1]
    imobj = Image.fromarray(img)
    
    left = 0
    top = 0
    right = left + tw
    bottom = top + th
    
    while(bottom <= img_height):
        while(right <= img_width):
            im1 = imobj.crop((left,top,right,bottom))
            n = np.array(im1)
            res.append(n)
            left = right
            right = left + tw
        left = 0
        right = left + tw
        top = bottom
        bottom = top + th
    return res