import tensorflow as tf

#hello is a constant string
hello=tf.constant('Hello TensorFlow')

#create a session
sess=tf.Session()
print(sess.run(hello))

#create a contant integer
a=tf.constant(10)
b=tf.constant(20)

#print sum of a and b
print(sess.run(a+b))
