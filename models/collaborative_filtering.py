# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: collaborative_filtering.py
@time: 2019/7/15 15:07

这一行开始写关于本文件的说明与解释
"""
from utils.similarity import similarity

class collaborative_filtering:
    def __init__(self, matrix):
        self.matrix = matrix
        pass

    def item_based_CF(self):
        pass

    def user_based_CF(self):
        # 1，计算相似性
        sm_mat = similarity.Jaccard(self.matrix)
        # 2，找到最相似的n个用户，推荐item

        pass