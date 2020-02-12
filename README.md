# python-modules
> Python functions
1. image_to_tiles
    - converts the image into patches in both manner overlapping and non-overlapping
    -  Input : image path, size (tuple), ratio (0<r<=1)
    size - size of each tiles
    ratio - overlapping ratio.
        1 = no overlapping
        0 = same patch.
        warning : ratio = 0 results to an infinite loop
    - Output : List of numpy array of image tiles
2. compress_image
    - reduce the height and width while maintaing the aspect ratio.
    - :param
        img_path
        new_height
        inplace(optional)
        new_img_path (required when inplace=false)
    - :return
        new file path
3. black_and_white
   - converts the image into black and white
   -  :param
        img_path
        [inplace] (default=True)
        [new_img_path] (required when inplace=false)
    - :return
        new file path
