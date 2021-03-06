import numpy as np
import tensorflow as tf
import random

class MyTrain:
  def __init__(self):
    self.rnd = random.Random()
    self.rnd.seed(0)
    self.inp = [ np.array([0., 0.], dtype=np.float32)
               , np.array([0., 1.], dtype=np.float32)
	       , np.array([1., 0.], dtype=np.float32)
	       , np.array([1., 1.], dtype=np.float32) ]
    self.exp = [ np.array([0.], dtype=np.float32)
               , np.array([1.], dtype=np.float32)
	       , np.array([1.], dtype=np.float32)
	       , np.array([0.], dtype=np.float32) ]
    self.n_subbatch = 3

  def next(self):
    idxs = map( lambda x: self.rnd.randint(0, 3)
              , range(self.n_subbatch) )
    return ( np.array(map(lambda i: self.inp[i], idxs))
           , np.array(map(lambda i: self.exp[i], idxs)) )

  def test_data(self):
    return np.array(self.inp), np.array(self.exp)

x = tf.placeholder(tf.float32, [None, 2])
y_ = tf.placeholder(tf.float32, [None, 1])
l1w = tf.Variable(tf.random_normal([2, 3], dtype=tf.float32, seed=0))
l1b = tf.Variable(tf.zeros([3], dtype=tf.float32))
l1s = tf.nn.sigmoid(tf.matmul(x, l1w) + l1b)
l2w = tf.Variable(tf.random_normal([3, 3], dtype=tf.float32, seed=1))
l2b = tf.Variable(tf.zeros([3], dtype=tf.float32))
l2s = tf.nn.sigmoid(tf.matmul(l1s, l2w) + l2b)
l3w = tf.Variable(tf.random_normal([3, 1], dtype=tf.float32, seed=2))
l3b = tf.Variable(tf.zeros([1], dtype=tf.float32))
y = tf.nn.sigmoid(tf.matmul(l2s, l3w) + l3b)
err = -tf.reduce_sum(y_*tf.log(y) + (1. - y_)*tf.log(1. - y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(err)

init = tf.initialize_all_variables();

td = MyTrain()
with tf.Session() as sess:
  sess.run(init)
  for j in range(200):
    for i in range(100):
      inp, exp = td.next()
      sess.run(train_step, feed_dict={x: inp, y_: exp})
    inp, exp = td.test_data()
    print sess.run(err, feed_dict={x: inp, y_: exp})
  print sess.run(l1w)
  print sess.run(l1b)
  print sess.run(l2w)
  print sess.run(l2b)
  print sess.run(l3w)
  print sess.run(l3b)
