import cv2
import os
import glob
#初始图片路径和终点路径
img_path = r'F:\picForOpencv'
dest_path = r'F:\destination'

i = 1
for img in glob.glob(img_path+'/*.*'):
    try:
        image = cv2.imread(img)
        #改变当前工作到指定目录
        os.chdir(dest_path)
        filename = 'new_data_' + str(i) +'.png'
        #写入图片和名字
        cv2.imwrite(filename, image)
        i += 1

    except:
        print('{} is not saved'.format(image))