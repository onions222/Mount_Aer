import os
from PIL import ImageFont, ImageDraw, Image
from pylab import *
import cv2 as cv
import pandas as pd
import numpy as np


# 不以科学计数法显示
np.set_printoptions(suppress = True)

def read_excel(excel_path, sheet_name):
    sheetname = sheet_name
    data = pd.read_excel(excel_path, sheet_name = sheetname)
    length = len(data)
    pixel = []
    frame = []
    real = []
    for i in range(length):
        pixel.append(data['x'][i])
        pixel.append(data['y'][i])
        frame.append(data['frame'][i])
        real.append(data['length'][i])
        real.append(data['height'][i])
    pixelarray=np.array(pixel).reshape(length,2)
    realarray=np.array(real).reshape(length,2)
    return pixelarray,frame,realarray

def write_image(image_path, save_path, frame, pixel, realxy, tai):
    # tai 指的是出台高度
    f = 0
    i = 0
    files = os.listdir(image_path)
    files.sort()
    for file in files:
        im_path = image_path + file + '/'
        paths = os.listdir(im_path)
        paths.sort()
        for path in paths:
            if f not in frame:
                img = cv.imdecode(np.fromfile(im_path + path, dtype=np.uint8), -1)
                cv.imwrite(save_path + "out" + str(f).rjust(3, '0') + ".jpg", img)
                f += 1
                continue
            else:
                # img = array(Image.open(imagepath+path))
                img = cv.imdecode(np.fromfile(im_path + path, dtype=np.uint8), -1)
                # 在运动员身上画轨迹点
                cv.circle(img, (pixel[i][0], pixel[i][1]), 10, (0, 0, 255),
                          -1)  # cv.circle(图片,元祖格式表示圆心,int类型半径,颜色,是否实心标志)
                # 在图片上标注高度远度信息
                # fontpath = '/usr/share/fonts/truetype/arphic/uming.ttc'
                fontpath = r'C:/Windows/Fonts/Times New Roman/times.ttf'
                font = ImageFont.truetype(fontpath, 50)
                img_pil = Image.fromarray(img)
                draw = ImageDraw.Draw(img_pil)
                length = 'length: ' + str(format(realxy[i][0], '.1f')) + str(tai)
                height = 'height: ' + str(format(realxy[i][1], '.1f')) + str(tai)
                draw.text((pixel[i][0] - 400, pixel[i][1] - 200), length, font=font, fill=(0, 0, 255))
                draw.text((pixel[i][0] - 400, pixel[i][1] - 150), height, font=font, fill=(0, 0, 255))
                img = np.array(img_pil)
                cv.imwrite(save_path + "out" + str(f).rjust(3, '0') + ".jpg", img)
                f += 1
                i += 1

# def pics_to_video():



def main():
    image_path = r'C:/Users/onions/Desktop/Mount_Aer/video2pic/'
    excel_path = r'C:/Users/onions/Desktop/Mount_Aer/qhd104425_final.xlsx'
    image_writed_save = r'C:/Users/onions/Desktop/Mount_Aer/img_writed_save/'
    video_save_path = r'C:/Users/onions/Desktop/Mount_Aer/'
    tai = 400
    pixel, frame, real_distance = read_excel(excel_path, 'Sheet4')
    write_image(image_path, image_writed_save, frame, pixel, real_distance, tai)


if __name__ == '__main__':
    main()

