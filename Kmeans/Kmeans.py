#coding:utf-8
from numpy import *

'''
Kmeans算法的流程：

1.创建k个点作为k个簇的起始质心（经常随机选择）。
2.分别计算剩下的元素到k个簇中心的相异度（距离），将这些元素分别划归到相异度最低的簇。
3.根据聚类结果，重新计算k个簇各自的中心，计算方法是取簇中所有元素各自维度的算术平均值。
4.将D中全部元素按照新的中心重新聚类。
5.重复第4步，直到聚类结果不再变化。
6.最后，输出聚类结果。

'''

'''
伪代码：

创建k个点作为K个簇的起始质心（经常随机选择）
当任意一个点的蔟分配结果发生变化时（初始化为True）
	对数据集中的每个数据点，重新分配质心
		对每个质心
			计算质心到数据点之间的距离
		将数据点分配到距其最近的蔟
	对每个蔟，计算蔟中所有点的均值并将均值作为新的质心

'''



# 加载训练数据
def loadDataSet(filename):
	dataMat = []
	openfile = open(filename)
	for line in openfile.readlines():
		curline = line.strip().split('\t')
		floatline = map(float, curline)
		dataMat = dataMat.append(floatline)
	return dataMat

# 定义计算欧式距离的函数
def Distance(vecA, vecB):
	return sqrt(sum(power(vecA-vecB,2)))

# 初始化K个簇的中心
# 传入的数据时numpy的矩阵格式
def rendCenter(dataMat, K):
	n = shape(dataMat)[1]
	# 把簇心以及其数据定义为K行n列，即每个簇有n个数据
	centroids = mat(zeros((k,n)))







