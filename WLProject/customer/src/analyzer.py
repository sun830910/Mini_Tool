# -*- coding: utf-8 -*-

"""
Created on 3/4/21 8:23 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import pandas as pd
import os


class ExcelHelper(object):
    def __init__(self, data_path):

        self.column_name = {"customer": "客户名称", "num": "金额", "month": "月份"}
        self.customer_attr_name = self.column_name.get("customer")
        self.num_attr_name = self.column_name.get("num")
        self.month_attr_name = self.column_name.get("month")

        if not os.path.exists(data_path):
            print("地址或命名错误，请确认文件是否为【total.xlsx】")
            return
        self.data = pd.read_excel(data_path)
        if not self.column_check():
            print("数据列名错误")
            return
        self.per_total_record = dict()  # 用来存储【客户-总销售额】的关系
        self.per_month_record = dict()  # 用来存储【月份-总销售额】的关系
        self.pre_cal()
        print("数据分析器初始化成功")

    def pre_cal(self):
        for _, row in self.data.iterrows():
            if row[self.customer_attr_name] not in self.per_total_record:
                self.per_total_record.setdefault(row[self.customer_attr_name], row[self.num_attr_name])  # 写入【客户-消费金额】
            else:
                self.per_total_record[row[self.customer_attr_name]] += row[self.num_attr_name]
            if row[self.month_attr_name] not in self.per_month_record:
                self.per_month_record.setdefault(row[self.month_attr_name], row[self.num_attr_name])
            else:
                self.per_month_record[row[self.month_attr_name]] += row[self.num_attr_name]

    def column_check(self):
        data_columns = self.data.columns.tolist()
        for key in self.column_name.keys():
            if self.column_name.get(key) not in data_columns:
                print("{}不存在，请检查列名是否正确".format(self.column_name.get(key)))
                return False
        return True

    def get_customer_monthly_data(self, customer: str):
        temp_df = self.data[self.data[self.customer_attr_name] == customer]
        temp_dict = temp_df.set_index(self.month_attr_name)[self.num_attr_name].to_dict()
        return temp_dict

    def get_top_customer(self):
        return sorted(self.per_total_record.items(), key=lambda item: item[1], reverse=True)

    def show_top_customer(self):
        sorted_result = self.get_top_customer()
        print("共有 {} 位顾客，依照消费总价排行后如下：".format(len(sorted_result)))
        for idx in range(len(sorted_result)):
            print("第 {} 名 ：【{}】的消费额为: 【{}】".format(idx + 1, sorted_result[idx][0], sorted_result[idx][1]))

    def show_top_month(self):
        sorted_result = sorted(self.per_month_record.items(), key=lambda item: item[1], reverse=True)
        print("共有{}个月的数据".format(len(sorted_result)))
        for idx in range(len(sorted_result)):
            print("第 {} 名 ：【{}月】的消费额为: 【{}】".format(idx + 1, sorted_result[idx][0], sorted_result[idx][1]))

    def show_customer_top_month(self, customer):
        data = self.get_customer_monthly_data(customer)
        sorted_result = sorted(data.items(), key=lambda item: item[1], reverse=True)
        print("{} 共有 {}个月的消费额".format(customer, len(sorted_result)))
        for idx in range(len(sorted_result)):
            print(
                "第 {} 名 ：【{}】【{}月】的消费额为: 【{}】".format(idx + 1, customer, sorted_result[idx][0], sorted_result[idx][1]))


if __name__ == '__main__':
    data_path = '../data/total.xlsx'
    test = ExcelHelper(data_path)
    customer = '亚力士'
    test.show_top_customer()
    print("-" * 30)
    test.show_top_month()
    print("-" * 30)
    test.show_customer_top_month(customer)
