import os
from PIL import Image


def compress(img_path, new_height, comp_fol_path):
    '''
    Input : img_path, new_height, comp_fol_path
    Output : new file path
    '''
    if not os.path.exists(comp_fol_path):
        os.makedirs(comp_fol_path)
    fname = img_path.split("\\")[-1]
    img = Image.open(img_path)
    hpercent = (new_height / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, new_height), Image.ANTIALIAS)
    img.save(os.path.join(comp_fol_path, fname))
    return os.path.join(comp_fol_path, fname)
