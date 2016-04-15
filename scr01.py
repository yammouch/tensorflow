import tensorflow as tf

a = tf.constant([[2, 1], [3, 4]], dtype=tf.float32)
b = tf.constant([1, 2], dtype=tf.float32, shape=[2, 1])
c = tf.matmul(a, b)

with tf.Session() as sess:
  print sess.run(c)
