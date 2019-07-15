# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: matrix.py
@time: 2019/7/15 15:43

该文档实现各种矩阵变换
"""
import numpy as np

class vink_matrix:
    def __init__(self):
        pass

    # 将所有非0的元素修改成为1，方便计算某些距离
    def martix_one_hot(mat):
        mat[mat != 0] = 1
        return mat
