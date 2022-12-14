import cv2
import os

image_path = r'C:/Users/lyj/Desktop/calulate_distance/Mount_Aer/video2pic/'

path = os.listdir(image_path)
path.sort()
print(path)
img = cv2.imread('')

def write_image(image_path, save_path, frame, pixel, realxy, tai):
    # tai 指的是出台高度
    # image_path = r'C:/Users/lyj/Desktop/calulate_distance/Mount_Aer/video2pic/'
    f = 0
    i = 0
    paths = os.listdir(image_path)
    paths.sort()
    for path in paths:
        if f not in frame:
            img = cv.imdecode(np.fromfile(image_path + path, dtype=np.uint8), -1)
            cv.imwrite(save_path + "out" + str(f).rjust(3,'0') + ".jpg", img)
            f += 1
            continue
        else:
            # img = array(Image.open(imagepath+path))
            img = cv.imdecode(np.fromfile(image_path+path, dtype=np.uint8),-1)
            # 在运动员身上画轨迹点
            cv.circle(img, (pixel[i][0], pixel[i][1]), 10, (0,0,255), -1)  # cv.circle(图片,元祖格式表示圆心,int类型半径,颜色,是否实心标志)
            #在图片上标注高度远度信息
            # fontpath = '/usr/share/fonts/truetype/arphic/uming.ttc'
            fontpath = r'C:/Windows/Fonts/Times New Roman/times.ttf'
            font = ImageFont.truetype(fontpath, 50)
            img_pil = Image.fromarray(img)
            draw = ImageDraw.Draw(img_pil)
            # print(type(realxy))
            length = 'length: ' + str(realxy[i][0]) + str(tai)
            height = 'height: ' + str(realxy[i][1]) + str(tai)
            draw.text((pixel[i][0]-400, pixel[i][1]-200), length, font=font, fill=(0, 0, 255))
            draw.text((pixel[i][0]-400, pixel[i][1]-150), height, font=font, fill=(0, 0, 255))
            img=np.array(img_pil)
            cv.imwrite(save_path + "out" + str(f).rjust(3,'0')+".jpg", img)
            f+=1
            i+=1
