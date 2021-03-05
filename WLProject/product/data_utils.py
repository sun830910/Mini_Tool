# -*- coding: utf-8 -*-

"""
Created on 3/5/21 2:39 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import pandas as pd
import os


class ProductMaker(object):
    def __init__(self, file_path):
        if not self.init_check(file_path):
            print("文件检测未通过")
        self.data = pd.read_excel(file_path)
        self.column_name = {"product": "型号", "color": "颜色", "size": "尺寸", "num": "数量", "month": "月份"}
        self.product_attr_name = self.column_name.get("product")
        self.color_attr_name = self.column_name.get("color")
        self.size_attr_name = self.column_name.get("size")
        self.num_attr_name = self.column_name.get("num")
        self.month_attr_name = self.column_name.get("month")

    def init_check(self, file_path):
        if not os.path.exists(file_path):
            return False
        return True


data_path = "./product.xlsx"
data = pd.read_excel(data_path)
print(data)
