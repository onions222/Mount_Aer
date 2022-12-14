# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:26:10 2021

@author: Administrator
"""

'''
========================================================================================================================
                                              读取帧图像中的出台点像素坐标（a,b）
========================================================================================================================
'''
import cv2
from math import *
import numpy as np
import math
import os

from PIL import Image
from pylab import *

tai = []
#视频转化成图片
def video_to_picture(video_path, pictures_path):
    #video_path = r"/share/manage/Lu/zhuanghan/video/darknet/results/videos/"
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('.')[0]
        folder_name = pictures_path +'pics_floders'+'/'+ file_name
        os.makedirs(folder_name,exist_ok=True)
        vc = cv2.VideoCapture(video_path+video_name)
        print(video_name)
        frames= int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
        print(frames)
        c = len(str(frames))              # 帧的位数
        # print(c)
        pic_path = folder_name+'/'
        
        i=0
        while(vc.isOpened()):
            i=i+1
            ret, frame = vc.read()
            if ret==True:
                j = str(i)
                while len(j) < c:     #帧数小于100  while len(j) < c + 1
                    j = '0'+j
                cv2.imwrite(pic_path + file_name + '_' + j + '.jpg', frame) 
            if ret==False:
                i = i-1
            if i==frames:
                break
        vc.release()
        # print('save_success')
        #print(folder_name)
        
        biaodian_path = pictures_path +'pics_floders'
         
    return biaodian_path

def main():
    video_path = '/Users/onions/Desktop/Mount_Aer/fenzhenvideo/' #存放多个视频的文件夹，可以批量处理视频
    images_path = '/Users/onions/Desktop/Mount_Aer/fenzhenimg/'   #'D:/sport/videos/'生成图像路径
    if not os.path.exists(images_path):
        os.makedirs(images_path)

    #create_img(imgs_path,txts_path,degree)
    biaodian_path = video_to_picture(video_path,images_path)

if __name__ == '__main__' :
    main()
