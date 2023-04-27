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
        HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        HSV = cv2.resize(HSV, (1000, 700))
        os.chdir(dest_path)

        filename = 'new_data '+str(i) + '.png'
        cv2.imshow("Demo" + str(i), image)
        cv2.imshow("Demo" + str(i) +"(HSV)", HSV)
        cv2.imwrite(filename, HSV)
        i += 1
        key = cv2.waitKey(0)

    except:
        print("not saved")
        print("!")