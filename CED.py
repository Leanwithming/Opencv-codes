import cv2
import os
import glob


img_path = r'F:\picForOpencv'
dest_path = r'F:\destination'


i = 1

for img in glob.glob(img_path + '/*.*'):
    try:
        image = cv2.imread(img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        noise_free = cv2.bilateralFilter(gray, 11, 17, 17)
        edge_img = cv2.Canny(noise_free, 170, 200)
        
        os.chdir(dest_path)
        filename = 'CED' + str(i) +'.png'
        cv2.imshow('Original', image)
        cv2.imshow(filename, edge_img)
        cv2.imwrite(filename, edge_img)
        key = cv2.waitKey(0)
        i += 1

    except Exception as ex:
        print('not executed, report: '+ ex)

