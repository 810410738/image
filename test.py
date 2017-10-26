from PIL import Image
import numpy
from pylab import *

#读取图片到数组中
# test = Image.open('1.jpg')
# test1 = test.convert('L')
# test_band = test.getbands()
# test_band1 = test1.getbands()
# print(len(test_band))
# print(test_band[:])
# print(test.size)
# # fan xiang
# im2 = 255 - im
# im3 = (100.0/255) * im + 100
# imshow(im)
# show()
test = Image.open('2.jpg')
# test.save('2.jpg')
im = array(test)
hist1 = numpy.histogram(test, bins=2)
plt.figure('hist1')
arr = im.flatten()
n,bins,patches = plt.hist(arr, bins=256, normed=1, facecolor='red')
plt.show()

