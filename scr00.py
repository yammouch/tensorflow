import tensorflow as tf

a = tf.Variable(tf.zeros([1]))
b = tf.Variable(1)

init = tf.initialize_all_variables()

sess = tf.Session()

sess.run(init)
print sess.run(a)
print sess.run(b)
