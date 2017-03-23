#coding:utf-8
'''
Author:Django
Date:2017/03/23
'''

import numpy as np

class LogisticRegressionClassifier():
    def __init__(self):
        self._alpha = None

    # 定义一个sigmoid函数
    def _sigmoid(self, fx):
        return 1.0/(1 + np.exp(-fx))

    # alpha为学习率,maxCycles为最大迭代次数
    def _gradDescent(self, featData, labelData, alpha, maxCycles):
        dataMat = np.mat(featData)              # m*n
        labelMat = np.mat(labelData).transpose()    # m*1
        m, n = np.shape(dataMat)
        weight = np.ones((n, 1))    # 初始化权重
        for i in range(maxCycles):
            hx = self._sigmoid(dataMat * weight)
            error = labelMat - hx  #size:m*1
            weight = weight + alpha * dataMat.transpose() * error  #根据误差修改回归系数
        return weight

    # 使用梯度下降方法训练模型
    def fit(self, train_x, train_y, alpha=0.01, maxCycles=100):
        return self._gradDescent(train_x, train_y, alpha, maxCycles)

    # 使用学习到的参数进行分类
    def predict(self, test_X, test_y, weight):
        dataMat = np.mat(test_X)
        labelMat = np.mat(test_y).transpose()
        hx = self._sigmoid(dataMat*weight)  # size:m*1
        m = len(hx)  # 总共m条数据
        error = 0.0
        for i in  range(m):
            if int(hx[i]) > 0.5:
                print str(i+1) + '-the sample ', int(labelMat[i]), 'is classified as: 1'
                if int(labelMat[i]) != 1:
                    error += 1.0
                    print "classify error."
            else:
                print str(i+1) + '-the sample ', int(labelMat[i]), 'is classified as: 0'
                if int(labelMat[i]) != 0:
                    error += 1
                    print "classify error."
        error_rate = error/m
        print "error rate is:", "%.4f" %error_rate
        return error_rate
