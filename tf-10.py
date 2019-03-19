''' 读图片 '''
import tensorflow.examples.tutorials.mnist.input_data as input_data
import numpy as np
import matplotlib.pyplot as plt
import pylab

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

batch_xs, batch_ys = mnist.train.next_batch(100)   # 只取其中100条数据来看
for one_pic_vic in batch_xs:
    one_pic_arr = np.reshape(one_pic_vic,(28,28))
    pic_matrix = np.matrix(one_pic_arr,dtype = "float")
    plt.imshow(pic_matrix)
    pylab.show()
