import numpy as np
import tensorflow as tf

a = tf.Variable(tf.constant(0.0, dtype=tf.float32))
b = tf.Variable(tf.constant(0.0, dtype=tf.float32))
#x = tf.constant([-2.0, -1.0, 0.0, 1.0, 2.0], dtype=tf.float32)
x = tf.placeholder(tf.float32, [5])
xval = np.array([-2, -1, 0, 1, 2], dtype=np.float32)
#y_ = tf.constant([-3.0, -1.0, 1.0, 3.0, 5.0], dtype=tf.float32)
y_ = tf.placeholder(tf.float32, [5])
y_val = np.array([-3, -1, 1, 3, 5], dtype=np.float32)
y = a*x + b

error = tf.reduce_sum((y - y_)**2)
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(error)

init = tf.initialize_all_variables()

with tf.Session() as sess:
  sess.run(init)
  print "a: %f, b: %f" % (sess.run(a), sess.run(b))
  for i in range(10):
    sess.run(train_step, feed_dict={x: xval, y_: y_val})
    print "a: %f, b: %f" % (sess.run(a), sess.run(b))
