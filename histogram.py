from PIL import Image
import numpy
from pylab import *


def histeq(image_array, image_bins=256):
    # 将图像矩阵转化成直方图数据，返回元组(频数，直方图区间坐标)
    image_array2, bins = np.histogram(image_array.flatten(), image_bins)
    # 计算直方图的累积函数
    cdf = image_array2.cumsum()
    # 将累积函数转化到区间[0,255]
    cdf = (255.0 / cdf[-1]) * cdf
    # 原图像矩阵利用累积函数进行转化，插值过程
    image2_array = np.interp(image_array.flatten(), bins[:-1], cdf)
    # 返回均衡化后的图像矩阵和累积函数
    return image2_array.reshape(image_array.shape), cdf


# 读取图片
test = Image.open('test2.jpg').convert('L')
# 把图片转成二维数组
im = numpy.array(test)
# 计算直方图
# hist1 = numpy.histogram(test, bins=2)
# plt.figure('hist1')
# 把二维数组变为一维数组
arr = im.flatten()
hist1 = numpy.histogram(test, bins=256)
print(hist1)

# # 绘制直方图
# plt.hist(arr, bins=256, normed=0, facecolor='red')
# plt.show()
#
# # 调用直方图均衡化方法
# a = histeq(im)
# plt.hist(a[0].flatten(), bins=256, normed=0, facecolor='red')
# plt.show()
# Image.fromarray(a[0]).convert('RGB').save('test2_histep.jpg')

