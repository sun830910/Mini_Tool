# -*- coding: utf-8 -*-

"""
Created on 2020-08-14 15:12
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com

计算当月累计发票数与金额，文件夹中的各发票应以【2020_01_01_店家名_金额】进行命名
"""

import os


def read_ticket(file_path):
    if not os.path.exists(file_path):
        print("文件夹不存在，请检查路径")
        return
    print("即将扫描文件夹，路径为：{}".format(file_path))
    files = os.listdir(file_path)  # 得到文件夹下的所有文件名称
    total = 0.0  # 计算总金额
    file_cnt = 0  # 发票数量计数器
    for file in files:
        file_name = os.path.splitext(file)[0]  # 分割出副档名
        filename_splited = file_name.split('_')
        try:
            if len(filename_splited) > 4:
                price = filename_splited[-1]
                total += float(price)
                file_cnt += 1
            else:
                print("命名不规范档案: {} ".format(file))
        except:
            print("命名不规范档案: {} ".format(file))
    print('-' * 30)
    print("当前发票张数: {} 张".format(file_cnt))
    print("当前发票总额: {} 元".format(total))
    return total


def get_target(current, target):
    if current >= target:
        print("当月发票已达标，超出金额为{}".format(current - target))
    else:
        print("当月发票未达标，差距金额为{}".format(target - current))


if __name__ == '__main__':
    file_path = '/Users/chiang/Downloads/发票/2021_03'
    current = read_ticket(file_path)
    target_price = 5400
    get_target(current, target_price)
