# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: similarity.py
@time: 2019/7/15 15:19

通过numpy计算数组的相似性。
改进方向：
1. 引入多线程
"""
import numpy as np
import math

class similarity:
    def __init__(self):
        pass


    # 某些距离要求矩阵必须为0,1. 这部分过滤待做
    def get_similarity(self, mat, type = 'euclidean'):
        if type == 'Euclidean':
            return self.Euclidean(mat)
        elif type == 'Manhattan':
            return self.Manhattan(mat)
        elif type == 'Jaccrd':
            return self.Jaccard(mat)
        elif type == "Cosine":
            return self.Cosine(mat)
        elif type == "Pearson":
            return self.Pearson(mat)
        else:
            return "TODO"

    # 计算欧式距离
    def Euclidean(self, mat):
        return_amt = np.zeros(shape=(len(mat),len(mat)),dtype=float)
        for i in range(len(mat)):
            for j in range(i+1,len(mat)):
                return_amt[i][j] = np.linalg.norm(mat[i] - mat[j])
        return return_amt

    # 计算曼哈顿距离
    def Manhattan(self, mat):
        return_mat = np.zeros(shape=(len(mat), len(mat)), dtype=float)
        for i in range(len(mat)):
            for j in range(i+1, len(mat)):
                return_mat[i][j] = np.linalg.norm(mat[i]-mat[j],ord=1)
        return return_mat

    # 计算Jaccard相似性
    def Jaccard(self, mat):
        return_mat = np.zeros(shape=(len(mat), len(mat)), dtype=float)
        for i in range(len(mat)):
            for j in range(len(mat)):
                x = mat[i]
                y = mat[j]
                up = np.double(np.bitwise_and((x != y), np.bitwise_or(x != 0, y != 0)).sum())
                down = np.double(np.bitwise_or(x != 0, y != 0).sum())
                return_mat[i][j] = up / down
        return return_mat

    def Jaccard_List(self, item_list1, item_list2):
        

    # 计算夹角余弦距离
    def Cosine(self, mat):
        return_mat = np.zeros(shape=(len(mat), len(mat)), dtype=float)
        for i in range(len(mat)):
            for j in range(len(mat)):
                x = mat[i]
                y = mat[j]
                return_mat[i][j] = np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))
        return return_mat

    # 计算皮尔逊相关系数
    def Pearson(self, mat):
        return_mat = np.zeros(shape=(len(mat), len(mat)), dtype=float)
        for i  in range(len(mat)):
            for j in range(len(mat)):
                X = np.vstack([mat[i],mat[j]])
                return_mat[i][j] =  np.corrcoef(X)[0][1]
        return return_mat

