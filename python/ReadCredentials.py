# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 10:32
@Auth ： ndmiao
@Blog ：www.ndmiao.cn
@Function ：将 Credentials 文件夹下的所有凭证读取
"""

import csv
import os

class ReadCredentials:
    def __init__(self):
        self.file_dir = 'D:/BaiduNetdiskWorkspace/代码/python/aws/Credentials'

    def file_name(self):
        """
        :return: 返回credentials下所有的文件名
        """
        return os.listdir(self.file_dir)

    def aws_id(self):
        """
        :return: 返回aws_id
        """
        id_list = []
        for id in os.listdir(self.file_dir):
            id_list.append(id[:12])
        return id_list

    def read_csv(self, filename):
        """
        :param filename: Credential 的文件名
        :return: 将 Credential 里面的内容以 json 的格式返回
        """
        tableData = []
        filename = self.file_dir + '/' + filename
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tableData.append(dict(row))
            return tableData

    def get_credential(self):
        """
        :return: 把所有 credential 整合输出
        """
        file_names = self.file_name()
        credentials = []
        for file_name in file_names:
            credentials.append(self.read_csv(file_name)[0])
        return credentials


if __name__ == "__main__":
    print(ReadCredentials().aws_id())
