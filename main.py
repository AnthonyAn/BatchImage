#-*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import sys
import os


# 创建边框，初始化风景图片，logo，文字
def init():
    # 白色边框
    im_edge = Image.new('RGB', (1799, 1232), color='#FFFFFF')
    
    # 风景图
    FileNames=os.listdir(sys.argv[1]) 
    print(FileNames)
    im_scenes=[]
    for filename in FileNames:
        im_scene = Image.open(sys.argv[1]+"/"+filename)
        box=((im_scene.width-1700/1232*im_scene.height)/2,0,(im_scene.width+1700/1232*im_scene.height)/2,im_scene.height)
        im_scene=im_scene.crop(box).resize((1757,1190))
        im_scenes.append(im_scene)

    # logo图
    im_logo = Image.open('logo/sd1.png')
    im_logo = im_logo.resize((im_logo.width//4*3,im_logo.height//4*3))

    #文字图
    im_text=Image.new('RGBA',(1100,100),(0,0,0,0))
    im_club=Image.open('logo/社团logo.png')
    im_club=im_club.resize((90,90))
    bans=im_club.split()
    im_text.paste(im_club.split()[0],box=(0,0),mask=bans[3])
    font=ImageFont.truetype('FZMWFont_0.ttf',70)
    draw=ImageDraw.Draw(im_text)
    draw.text((120,10),'| 愿你不辜负每一个清晨',fill='#FFFFFFAA',font=font)

    return im_edge,im_scenes,im_logo,im_text,FileNames

#组合边框，背景，logo，文字
def imcomposite():
    im_group = init()
    edge=im_group[0]
    scenes=im_group[1]
    logo=im_group[2]
    text=im_group[3]
    filenames=im_group[4]

    for scene,filename in zip(scenes,filenames):
        # 组合
        edge.paste(scene,box=(21,21))
        edge.paste(logo, box=(1450, 70), mask=logo.split()[3])
        edge.paste(text, box=(100, 1060), mask=text.split()[3])

        #保存文件
        edge.save('respic/res_'+filename, 'jpeg',dpi=(300,300))

def main():
    imcomposite()


if __name__ == '__main__':
    main()