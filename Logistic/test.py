#coding:utf-8
'''
Author:Django
Date:2017/03/23
'''

from logistics import LogisticRegressionClassifier

#每行数据以\t隔开,最后一列为类标号
def loadDataSet(datafile):
    featData = []
    labelData = []
    with open(datafile, 'r') as fr_file:
        for eachline in fr_file:
            oneline = eachline.split('\t')
            tempArr = []
            for i in range(len(oneline) - 1):
                tempArr.append(float(oneline[i]))
            featData.append(tempArr)
            labelData.append(int(float(oneline[-1].strip())))
    return featData, labelData   # 返回的数据是list


def main():
    trainfile = r"data/train.txt"
    testfile = r"data/test.txt"
    train_X, train_y = loadDataSet(trainfile)
    test_X, test_y = loadDataSet(testfile)
    clf = LogisticRegressionClassifier()
    weight = clf.fit(train_X, train_y, alpha=0.01, maxCycles=500)
    clf.predict(test_X, test_y, weight)


if __name__ == '__main__':
    main()