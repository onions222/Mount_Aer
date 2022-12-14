# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 14:16:04 2021

@author: MSJ
"""
import os
import cv2
import numpy as np
from cv2.gapi import video

file_dir= r'C:C:/Users/onions/Mount_Aer/img_writed_save/10445/'
video_save_path = r'C:/Users/onions/Desktop/Mount_Aer/video_save/10445/10445.mp4'

list=[]
for root,dirs,files in os.walk(file_dir):
    for file in files:
       list.append(file)  #获取目录下文件名列表
list.sort() 

video.release()