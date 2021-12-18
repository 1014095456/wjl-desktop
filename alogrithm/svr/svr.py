# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:27:12 2020

@author: wujinlv
"""
from sklearn.svm import SVR
from sklearn.svm import NuSVR
from sklearn.model_selection import train_test_split
import numpy as np
#import xlrd
from sklearn import preprocessing
import scipy.io as scio
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score



xfile='F:/Paper/paper_data_code/oinputpointdata.mat'
yfile='F:/Paper/paper_data_code/b3.mat'
n_sample=521
datax=scio.loadmat(xfile)
datay=scio.loadmat(yfile)
x=datax['oinputpointdata'][0:n_sample].astype(np.float32)
y=datay['b3'][0:n_sample].astype(np.float32)
min_max_scaler = preprocessing.MinMaxScaler()
x  = min_max_scaler.fit_transform(x)
y  = min_max_scaler.fit_transform(y)
y=y.ravel()#改为列向量
'''
十次随机验证
'''
scores1=[]
scores2=[]
for i in range(10):
    x_t,x_v,y_t,y_v=train_test_split(x,y,test_size=0.2)
    svr1=SVR()
    svr2=NuSVR()
    svr1.fit(x_t,y_t)
    svr2.fit(x_t,y_t)
    score1=svr1.score(x_v,y_v)
    score2=svr2.score(x_v,y_v)
    scores1.append(round(score1,2))
    scores2.append(round(score2,2))
print('svr十次r方为：\n',scores1,'\nnusvr十次r方为：\n',scores2)
score1_m = np.mean(scores1)
score2_m = np.mean(scores2)
print('{:.2f},{:.2f}'.format(score1_m,score2_m))  

#x_t,x_v,y_t,y_v=train_test_split(x,y,test_size=0.2)
#svr = GridSearchCV(SVR(), param_grid={"kernel": ("poly", 'rbf'),\
#      "C": np.logspace(1,20, 5), "gamma": np.logspace(0, 1, 5)},scoring='r2')

#svr.fit(x_t,y_t)
#svr=SVR()
#scores = cross_val_score(svr, x, y, cv=5, scoring='r2')  
#print(scores)
#print(scores.mean())  
#print('r方为：%.3f'%metrics.r2_score(x_v,y_v))
#print('the best patams is{}'.format(svr.best_params_))


'''
def excel_to_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]#获取第一个sheet表
    row = table.nrows  # 行数
    col = table.ncols  # 列数
    datamatrix = np.zeros((row, col))#生成一个nrows行ncols列，且元素均为0的初始矩阵
    for x in range(col):
        cols = np.matrix(table.col_values(x))  # 把list转换为矩阵进行矩阵操作
        datamatrix[:, x] = cols # 按列把数据存进矩阵中
    #数据归一化   
    min_max_scaler = preprocessing.MinMaxScaler()
    datamatrix  = min_max_scaler.fit_transform(datamatrix)
    return datamatrix
'''
