import tensorflow as tf
'''tensorflow计算a=(b+c)∗(c+2)
    (b+c) 与 (c+2)没关系，所以可以并行计算
'''
# 创建常量
const =tf.constant(2.0,name='const')
# 创建变量
b = tf.Variable(2.0, name='b')
c = tf.Variable(1.0, dtype=tf.float32, name='c')
d= tf.add(b,c,name='d')
e=tf.add(c,const,name='e')

a=tf.multiply(d,e,name='a')

# 定义初始化操作
init_op=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    a_out=sess.run(a)
    print("Variable a is {}".format(a_out))
