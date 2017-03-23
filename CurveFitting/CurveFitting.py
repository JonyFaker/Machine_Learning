#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

# 主要实现的是正弦函数加上偏置的计算,生成样本的y值
def y(x, delta):
	PI = 3.14
	y = np.sin(2*PI*x) + delta
	# y为一个1*10的向量
	return y

# 采用随机梯度下降来进行曲线拟合
def fitting_SGD(x, y):
	learning_rate = 0.005
	iters = 1
	Eps = 0.001
	w = np.random.normal(1,10,4)  # 初始化参数w，为一个1*5
	loss = 1
	# 随机下降的过程
	while loss > Eps and iters < 1000:
		loss = 0;
		i = np.random.randint(1,9)
		h = w[0] + w[1]*x[i] + w[2]*np.square(x[i]) + w[3]*pow(x[i],3)
		# 随机选择一个样本，更新所有参数
		w[1] = w[1] + learning_rate*(y[i] - h)*w[1]
		w[2] = w[2] + learning_rate*(y[i] - h)*w[2]
		w[3] = w[3] + learning_rate*(y[i] - h)*w[3]
		Error = 0
		Error = w[0] + w[1]*x[i] + w[2]*np.square(x[i]) + w[3]*pow(x[i],3)
		Error = Error*Error
		loss += Error
		iters += 1
		print('loss=', loss)
		print('w=', w)
		print('iters=', iters)

	print('Training Completed!')
	print('w=', w)
	print('iters=', iters)

	# 接下来画出拟合的曲线
	# 先画出原来数据在图中的位置
	plt.plot(x, y)
	plt.show()


	# 再画出曲线



# 采用正则方程来进行曲线拟合
def fitting_normalize():
	pass


if __name__ == '__main__':
	# 生成均匀分布的numpy数组，0-1之间,形状为（10，）
	x = np.random.uniform(0,1,10)

	# delta的分布服从正态分布，均值为0，标准差为0.001，delta为y函数的一个偏置
	mean = 0
	sigma = 0.001
	delta = np.random.normal(mean, sigma, 10)
	y = y(x, delta)  # 真实的y值
	# M = 3   # M为设置多项式的次方数，即y = w0 + w1x + w2x平方 + w3x平方
	fitting_SGD(x, y)
	# fitting_normalize(x, y)

