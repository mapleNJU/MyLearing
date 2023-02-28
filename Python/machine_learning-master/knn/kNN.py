import numpy as np
import os
import operator
import shutil
from PIL import Image


def img2vector(filename, width, height):
    """将txt文件转为一维数组"""
    return_vector = np.zeros((1, width * height))
    fr = open(filename)
    for i in range(height):
        line = fr.readline()
        for j in range(width):
            return_vector[0, height * i + j] = int(line[j])
    return return_vector


# test_set 单个测试样本
# train_set 训练样本二维数组
# labels 训练样本对应的分类
# k k值
def classify(test_set, train_set, labels, k):
    """对测试样本进行kNN分类,返回测试样本的类别"""
    # 获取训练样本条数
    train_size = train_set.shape[0]

    # 计算特征值的差值并求平方
    # tile(A,(m,n))，功能是将数组A行重复m次 列重复n次
    diff_mat = np.tile(test_set, (train_size, 1)) - train_set
    sq_diff_mat = diff_mat**2

    # 计算欧式距离 存储到数组 distances
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5

    # 按距离由小到大排序对索引进行排序
    sorted_index = distances.argsort()

    # 求距离最短k个样本中 出现最多的分类
    class_count = {}
    for i in range(k):
        near_label = labels[sorted_index[i]]
        class_count[near_label] = class_count.get(near_label, 0) + 1
    sorted_class_count = sorted(class_count.items(),
                                key=operator.itemgetter(1),
                                reverse=True)
    return str(sorted_class_count[0][0])


# train_data_path 训练样本文件夹
# test_data_path 测试样本文件夹
# k k个最近邻居
def get_error_rate(train_data_path, test_data_path, k):
    """统计识别错误率"""
    width, height = 32, 32
    train_labels = []

    training_file_list = os.listdir(train_data_path)
    train_size = len(training_file_list)

    # 生成全为0的训练集数组
    train_set = np.zeros((train_size, width * height))

    # 读取训练样本
    for i in range(train_size):
        file = training_file_list[i]
        file_name = file.split('.')[0]
        label = str(file_name.split('_')[0])
        train_labels.append(label)
        train_set[i, :] = img2vector(
            os.path.join(train_data_path, training_file_list[i]), width,
            height)

    test_file_list = os.listdir(test_data_path)
    # 识别错误的个数
    error_count = 0.0
    # 测试样本的个数
    test_count = len(test_file_list)

    # 统计识别错误的个数
    for i in range(test_count):
        file = test_file_list[i]
        true_label = file.split('.')[0].split('_')[0]

        test_set = img2vector(os.path.join(test_data_path, test_file_list[i]),
                              width, height)
        test_label = classify(test_set, train_set, train_labels, k)
        print(true_label, test_label)
        if test_label != true_label:
            error_count += 1.0
    percent = error_count / float(test_count)
    print("识别错误率是:{}".format(str(percent)))


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
    """从图片库中   每个字母挑选前140张图片作为样本(120个训练样本，20个测试样本)"""

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

                    # 前120张图片存入训练集 120-140 张图片存入测试集
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


# image_file_prefix  png图片所在的文件夹
# file_name png      png图片的名字
# txt_path_prefix    转换后txt 文件所在的文件夹
def generate_txt_image(image_file_prefix, file_name, txt_path_prefix):
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

    # 创建txt文件(mac下使用os.mknod()创建文件需要root权限，这里改用复制的方式)
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

# 计算识别错误率
get_error_rate("project/txt/train_data", "project/txt/test_data", 3)
