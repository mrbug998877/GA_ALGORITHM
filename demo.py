import numpy as np
from geatpy import crtpc
help(crtpc)
"""
    定义种群数规模（个体数目）
"""
Nind = 3
Encoding = 'RI' #采用“实整数编码”，即变量可以是连续的也可以是离散的

"""
    创建“区域描述器”，表明有3个决策变量，范围分别是[1,4][1,3][1,5]
    fielddr第三行[0,0,0,]表示所有的决策变量都是连续型，若为1，才是离散型；
"""