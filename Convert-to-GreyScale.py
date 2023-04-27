import cv2
import os
import glob

img_path = r'F:\picForOpencv'
dest_path = r'F:\destination'

i = 1

for img in glob.glob(img_path + '/*.*'):
    try:
        image = cv2.imread(img)
        image = cv2.resize(image, (1000, 700))
        GreyScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        GreyScale= cv2.resize(GreyScale, (1000, 700))
        os.chdir(dest_path)

        filename = 'new_data '+str(i) + '.png'
        cv2.imshow("Demo" + str(i), image)
        cv2.imshow("Demo" + str(i) +"(GreyScale)", GreyScale)
        cv2.imwrite(filename, GreyScale)
        i += 1
        key = cv2.waitKey(0)

    except:
        print("not saved")