import tensorflow as tf

# Tensorflow version
print(tf.__version__)

#  Zero dimension data
data = tf.constant(7)
print(data) # tf.Tensor(7, shape=(), dtype=int32)
print(data.ndim)

# One- Dimension Data
vec = tf.constant([12,23,4,5,6])
print(vec)
print(vec.ndim)

# Multi-Dimension Data
mat = tf.constant([[1,2,3,4], [3,4,5,6]])
print(mat)
print(mat.ndim)

# Complex Data -- Error
try:
    mat = tf.constant([[1,2,3,4], [3,4,5,6,7,8]])
    print(mat.ndim)
except Exception as ex:
    print(ex)

# Complex Data -- Error
try:
    an_mat = tf.constant([[1,2,3,4], [2,[3,4], 5,6]])
    print(an_mat.ndim)
except Exception as ex:
    print(ex)