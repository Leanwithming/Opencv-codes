import cv2
import os
import glob
#��ʼͼƬ·�����յ�·��
img_path = r'F:\picForOpencv'
dest_path = r'F:\destination'

i = 1
for img in glob.glob(img_path+'/*.*'):
    try:
        image = cv2.imread(img)
        #�ı䵱ǰ������ָ��Ŀ¼
        os.chdir(dest_path)
        filename = 'new_data_' + str(i) +'.png'
        #д��ͼƬ������
        cv2.imwrite(filename, image)
        i += 1

    except:
        print('{} is not saved'.format(image))