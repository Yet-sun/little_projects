# encoding: utf-8

'''
@author: sunyue
@contact: sunyue@mail.ynu.edu.cn
@software: pycharm
@file: wechat_avatar.py
@time: 2019/5/14
@desc: 微信好友图片墙
'''

from wxpy import *
import math
import os
from PIL import Image


def crete_filepath():
    '''
    创建头像存放文件夹
    :return:
    '''
    avatar_dir = os.getcwd() + "\\wechat\\"
    if not os.path.exists(avatar_dir):
        os.mkdir(avatar_dir)
    return avatar_dir


def save_avatar(avatar_dir):
    '''
    保存好友头像
    :param avatar_dir:
    :return:
    '''
    # 初始化机器人，扫码登录
    bot = Bot()
    friends = bot.friends(update=True)
    num = 0
    for friend in friends:
        friend.get_avatar(avatar_dir + '\\' + str(num) + '.jpg')
        print("好友昵称：{}".format(friend.nick_name))
        num = num + 1


def joint_avatar(path):
    '''
    拼接头像
    :param path:
    :return:
    '''
    # 获取文件夹内头像个数
    length = len(os.listdir(path))
    # 设置画布大小
    image_size = 2560
    # 设置每个头像大小
    each_size = math.ceil(2560 / math.floor(math.sqrt(length)))
    # 计算所需各行列的头像数量
    x_lines = math.ceil(math.sqrt(length))
    y_lines = math.ceil(math.sqrt(length))
    image = Image.new('RGB', (each_size * x_lines, each_size * y_lines))
    x = 0
    y = 0
    for (root, dirs, files) in os.walk(path):
        for pic_name in files:
            # 增加头像读取不出来的异常
            try:
                with Image.open(path + pic_name) as img:
                    img = img.resize((each_size, each_size))
                    image.paste(img, (x * each_size, y * each_size))
                    x += 1
                    if x == x_lines:
                        x = 0
                        y += 1
            except IOError:
                print("头像读取失败")
    img = image.save(os.getcwd() + "/wechat.png")
    print('微信好友头像拼接成功！')


if __name__ == '__main__':
    avatar_dir = crete_filepath()
    save_avatar(avatar_dir)
    joint_avatar(avatar_dir)
