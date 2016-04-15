import tensorflow as tf

a = tf.Variable(tf.zeros([1]))
b = tf.Variable(1)
c = tf.Variable(tf.constant([0, 1], dtype=tf.float32))
d = tf.constant([0, 1], dtype=tf.float32)

init = tf.initialize_all_variables()


sess = tf.Session()

print sess.run(d)
sess.run(init)
print sess.run(a)
print sess.run(b)
print sess.run(c)

sess.run(b.assign(2))
print sess.run(b)
