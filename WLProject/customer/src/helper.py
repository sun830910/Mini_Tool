# -*- coding: utf-8 -*-

"""
Created on 3/5/21 9:30 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import pandas as pd
import os


class DataRemaker(object):
    def __init__(self, data_path):
        if not os.path.exists(data_path):
            print("文件不存在，请检查路径与档名")
            return
        self.data = pd.read_excel(data_path)
        self.column_name = {"customer": "客户名称", "num": "金额", "month": "月份"}
        self.customer_attr_name = self.column_name.get("customer")
        self.num_attr_name = self.column_name.get("num")
        self.month_attr_name = self.column_name.get("month")
        self.customer_dict = dict()
        self.month_price_dict = dict()
        self.customer_set = set()

        self.set_customer_set()

    def set_customer_set(self):
        for idx in self.data[self.customer_attr_name]:
            if idx not in self.customer_set:
                self.customer_set.add(idx)

    def search_customer(self, customer_name):
        return self.data[self.data[self.customer_attr_name] == customer_name]

    def get_month_dict(self, df):
        result = dict()
        repeat_month = set()
        customer_name = ""
        total = 0
        for _, row in df.iterrows():
            if row[self.month_attr_name] not in result:
                result.setdefault(row[self.month_attr_name], row[self.num_attr_name])
            else:
                customer_name = row[self.customer_attr_name]
                repeat_month.add(row[self.month_attr_name])
                result[row[self.month_attr_name]] += row[self.num_attr_name]
            total += row[self.num_attr_name]
        if len(repeat_month) != 0:
            print("【{}】的【{}】月数据有重复，请确认".format(customer_name, repeat_month))
        return [total, result]

    def get_all_customer_month(self):
        result_dict = dict()
        for name in self.customer_set:
            customer_data = self.search_customer(name)
            customer_dict = self.get_month_dict(customer_data)
            # print("{}的总消费为{}，消费记录为{}".format(name, customer_dict[0], customer_dict[1]))
            result_dict.setdefault(name, customer_dict)
        return result_dict


if __name__ == '__main__':
    data_path = './total.xlsx'
    test = DataRemaker(data_path)
    sample = "亚力士"
    result = test.search_customer(sample)
    res = test.get_all_customer_month()
    print(res)
