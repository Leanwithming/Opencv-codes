import cv2
import os
import glob


img_path = r'F:\picForOpencv'
dest_path = r'F:\destination'


i = 1

for img in glob.glob(img_path + '/*.*'):
    try:
        image = cv2.imread(img)
        grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(9,(10, 10))
        new_clahe = clahe.apply(grayScale)
        os.chdir(dest_path)
        filename = 'CLAHE' + str(i) +'.png'
        cv2.imshow(filename, new_clahe)
        cv2.imshow('image1', image)
        cv2.imwrite(filename, new_clahe)
        i += 1
        key = cv2.waitKey(0)

    except:
        print('not executed')