import numpy as np
import pandas as pd
import os
from PIL import ImageFont, ImageDraw, Image
from pylab import  *
import cv2 as cv

def readdata(datapath):
    data = pd.read_excel(datapath,sheet_name='Sheet4')
    length=len(data)
    pixel=[]
    frame=[]
    real=[]
    for i in range(length):
        pixel.append(data['x'][i])
        pixel.append(data['y'][i])
        frame.append(data['frame'][i])
        real.append(data['length'][i])
        real.append(data['height'][i])
    pixelarray=np.array(pixel).reshape(length,2)
    realarray=np.array(real).reshape(length,2)
    return pixelarray,frame,realarray

if __name__ == '__main__' :
    datapath = r'C:/Users/lyj/Desktop/calulate_distance/Mount_Aer/qhd104425_final.xlsx'  #存储对应数据
    imagepath = r'C:/Users/lyj/Desktop/calulate_distance/Mount_Aer/video2pic/10445/'  #运动员图片 保留第一张检测错误的图片
    savepath = 'C:/Users/lyj/Desktop/calulate_distance/Mount_Aer/img_writed_save/'#需自建文件夹
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    if not os.path.exists(imagepath):
        os.mkdir(imagepath)
    pixel,frame,real=readdata(datapath)  #pixel and real are array,frame is list
    paths=os.listdir(imagepath)
    paths.sort()
    print(paths)
    tai=400
    f=0
    i=0
    for path in paths:
        if f not in frame:
            img = cv.imdecode(np.fromfile(imagepath + path, dtype=np.uint8), -1)
            cv.imwrite(savepath + "out" + str(f).rjust(3,'0') + ".jpg", img)
            f+=1
            continue
        else:
            # img = array(Image.open(imagepath+path))
            img = cv.imdecode(np.fromfile(imagepath+path, dtype=np.uint8),-1)
            ###在运动员身上画轨迹点
            cv.circle(img, (pixel[i][0], pixel[i][1]), 10, (0,0,255), -1)  # cv.circle(图片,元祖格式表示圆心,int类型半径,颜色,是否实心标志)
            #在图片上标注高度远度信息
            # fontpath = '/usr/share/fonts/truetype/arphic/uming.ttc'
            fontpath = r'C:/Windows/Fonts/Times New Roman/times.ttf'
            font = ImageFont.truetype(fontpath, 50)
            img_pil = Image.fromarray(img)
            draw = ImageDraw.Draw(img_pil)
            draw.text((pixel[i][0]-400, pixel[i][1]-200), "length："+str(real[i][0]), font=font, fill=(0, 0, 255))
            draw.text((pixel[i][0]-400, pixel[i][1]-150), "height:"+str(real[i][1]+tai), font=font, fill=(0, 0, 255))
            img=np.array(img_pil)
            cv.imwrite(savepath+"out"+str(f).rjust(3,'0')+".jpg", img)
            f+=1
            i+=1