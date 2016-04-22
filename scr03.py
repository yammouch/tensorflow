import tensorflow as tf
import random

random.seed(0)
for i in range(5):
  print random.random()

r = tf.random_uniform([5], seed=0)

with tf.Session() as sess:
  print sess.run(r)
