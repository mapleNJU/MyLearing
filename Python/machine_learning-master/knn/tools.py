import os
import shutil
from PIL import Image


def change_folder_2_char():
    """将十六进制的文件夹名改为ASCII 字符"""
    path = 'project/by_class/by_class'
    for file in os.listdir(path):
        file_name = os.path.join(path, file)
        if os.path.isdir(file_name) and len(file) == 2:
            try:
                # 计算出十进制数值
                asc_num = int(file[0], 16) * 16 + int(file[1], 16)
                # 生成新文件名
                new_name = chr(asc_num) + "_" + str(asc_num)
                os.renames(file_name, os.path.join(path, new_name))
            except ValueError:
                print(file + " is wrong !")


def generate_train_data():

    path = 'project/by_class/by_class'
    train_path = 'project/test/train_data'
    test_path = 'project/test/test_data'
    os.mkdir(train_path)
    os.mkdir(test_path)
    for file_name in os.listdir(path):
        first_path = os.path.join(path, file_name)
        if os.path.isdir(first_path):
            for second_file in os.listdir(first_path):
                if second_file.startswith('train'):
                    second_path = os.path.join(first_path, second_file)
                    # 前30张图片存入训练集 31-40 张图片存入测试集
                    index = 0
                    for third_file in os.listdir(second_path)[:40]:  #要改
                        third_path = os.path.join(second_path, third_file)
                        new_file_prefix = file_name + "_"
                        if index < 30:
                            shutil.copyfile(
                                third_path,
                                os.path.join(
                                    train_path,
                                    new_file_prefix + str(index) + ".png"))
                        else:
                            shutil.copyfile(
                                third_path,
                                os.path.join(
                                    test_path, new_file_prefix +
                                    str(index - 100) + ".png"))
                        index += 1
            print(file_name)


def generate_txt_image(image_file_prefix, file_name, txt_path_prefix):
    # image_file_prefix  png图片所在的文件夹
    # file_name png      png图片的名字
    # txt_path_prefix    转换后txt 文件所在的文件夹
    """将图片处理成只有0 和 1 的txt 文件"""
    # 将png图片转换成二值图并截取四周多余空白部分
    image_path = os.path.join(image_file_prefix, file_name)
    # convert('L') 将图片转为灰度图 convert('1') 将图片转为二值图
    img = Image.open(image_path, 'r').convert('1').crop((32, 32, 96, 96))

    # 指定转换后的宽 高
    width, height = 32, 32
    img.thumbnail((width, height), Image.ANTIALIAS)

    # 将二值图片转换为0 1，存储到二位数组arr中
    arr = []
    for i in range(width):
        pixels = []
        for j in range(height):
            pixel = int(img.getpixel((j, i)))
            pixel = 0 if pixel == 0 else 1
            pixels.append(pixel)
        arr.append(pixels)

    # 创建txt文件
    text_image_file = os.path.join(txt_path_prefix,
                                   file_name.split('.')[0] + '.txt')
    empty_txt_path = "project/empty.txt"
    shutil.copyfile(empty_txt_path, text_image_file)

    # 写入文件
    with open(text_image_file, 'w') as text_file_object:
        for line in arr:
            for e in line:
                text_file_object.write(str(e))
            text_file_object.write("\n")


image_prefix = "project/test/train_data/"
txt_image_prefix = "project/txt/train_data"
for file in os.listdir(image_prefix):
    # 排除 .DS_Store文件
    if not file.startswith('.'):
        generate_txt_image(image_prefix, file, txt_image_prefix)  #
    print(file)

image_prefix = "project/test/test_data"
txt_image_prefix = "project/txt/test_data"
for file in os.listdir(image_prefix):
    if not file.startswith('.'):
        generate_txt_image(image_prefix, file, txt_image_prefix)
    print(file)

# generate_train_data()
