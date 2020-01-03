import numpy as np
from PIL import Image 

def makeTiles(img_path,size,ratio=1):
    '''
    Input : image path, size (tuple), ratio (0<r<=1)
    size - size of each tiles
    ratio - overlapping ratio.
        1 = no overlapping
        0 = same patch. 
        warning : ratio = 0 results to an infinite loop
    Output : List of numpy array of image tiles
    '''
    imobj = Image.open(img_path)
    img = np.array(imobj)
    res = []
    th = size[0]
    tw = size[1]
    img_height = img.shape[0]
    img_width = img.shape[1]
    
    left = 0
    top = 0
    right = left + tw
    bottom = top + th
    
    while(bottom <= img_height):
        while(right <= img_width):
            im1 = imobj.crop((left,top,right,bottom))
            n = np.array(im1)
            res.append(n)
            left = left + int(tw*ratio)
            right = left + tw
        left = 0
        right = left + tw
        top = bottom
        bottom = top + th
    return res