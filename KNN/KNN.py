#coding:utf-8
'''
Author:Django
Date:17/3/23
'''

import numpy as np
import operator

class KNNClassifier():
    '''这是一个K近邻分类器'''
    def __init__(self, k=3):
        self._k = k

    # 计算欧式距离
    def _calEDistance(self, inSample, dataset):
        m = dataset.shape[0]  # 样本的数目
        # tile函数的意思是将inSample 行方向上重复m次,列方向上1次
        diffMat = np.tile(inSample, (m, 1)) - dataset
        sqDiffMat = diffMat**2  # 每个元素的平方
        sqDistances = sqDiffMat.sum(axis=1)  #求和
        distances = sqDistances ** 0.5  # 开根号
        return distances.argsort()   # 按距离的从小到大进行排列,注意这边返回的是下标

    def _classify0(self, inX, dataSet, labels):
        k = self._k
        classCount = {}

        sortedDistIndicies = self._calEDistance(inX, dataSet)

        for i in range(k):
            voteIlabel = labels[sortedDistIndicies[i]]
            classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    # 对一个样本进行分类
    def _classify(self, sample, train_X, train_y):
        # 数据类型检测
        if isinstance(sample, np.ndarray) and isinstance(train_X, np.ndarray)
            and isinstance(train_y, np.ndarray):
            pass
        else:
            try:
                sample = np.array(sample)
                train_X = np.array(train_X)
                train_y = np.array(train_y)
            except:
                raise TypeError("numpy.ndarray required for train_X and ..")

        sortedDistances = self._calEDistance(sample, train_X)
        classCount = {}
        for i in range(self._k):
            oneVote = train_y[sortedDistances[i]]  # 获取最近的第i个点的类别
            classCount[oneVote] = classCount.get(oneVote, 0) + 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]


    # 对一组样本进行分类
    def classify(self, test_X, train_X, train_y):
        results = []
        #数据类型检测
        if isinstance(test_X, np.ndarray) and isinstance(train_X, np.ndarray) \
                and isinstance(train_y, np.ndarray):
            pass
        else:
            try:
                test_X = np.array(test_X)
                train_X = np.array(train_X)
                train_y = np.array(train_y)
            except:
                raise TypeError("numpy.ndarray required for train_X and ..")
        d = len(np.shape(test_X))
        if d == 1:
            sample = test_X
            result = self._classify(sample, train_X, train_y)
            results.append(result)
        else:
            for i in range(len(test_X)):
                sample = test_X[i]
                result = self._classify(sample, train_X, train_y)
                results.append(result)
        return results


if __name__ == '__main__':
    train_X = [[1, 2, 0, 1, 0],
               [0, 1, 1, 0, 1],
               [1, 0, 0, 0, 1],
               [2, 1, 1, 0, 1],
               [1, 1, 0, 1, 1]]
    train_y = [1, 1, 0, 0, 0]
    clf = KNNClassifier(k=3)
    sample = [[1, 2, 0, 1, 0], [1, 2, 0, 1, 1]]
    result = clf.classify(sample, train_X, train_y)
    print result