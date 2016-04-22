import tensorflow as tf

a = tf.Variable(tf.constant(0.0, dtype=tf.float32))
b = tf.Variable(tf.constant(0.0, dtype=tf.float32))
x = tf.constant([-2.0, -1.0, 0.0, 1.0, 2.0], dtype=tf.float32)
y_ = tf.constant([-3.0, -1.0, 1.0, 3.0, 5.0], dtype=tf.float32)
y = a*x + b

error = (y - y_)**2
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(error)

init = tf.initialize_all_variables()

with tf.Session() as sess:
  sess.run(init)
  print "a: %f, b: %f" % (sess.run(a), sess.run(b))
  for i in range(50):
    sess.run(train_step)
    print "a: %f, b: %f" % (sess.run(a), sess.run(b))
