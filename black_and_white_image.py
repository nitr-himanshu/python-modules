import cv2

def convertToBlackAndWhite(img_path, inplace=True, new_img_path=""):
    '''
    :param
        img_path
        [inplace] (default=True)
        [new_img_path] (required when inplace=false)
    :return
        new file path
    '''
    originalImage = cv2.imread(img_path)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(
        grayImage, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    if(inplace):
        new_img_path = img_path
    cv2.imwrite(new_img_path, blackAndWhiteImage)
    return new_img_path
