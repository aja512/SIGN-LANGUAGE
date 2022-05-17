import tensorflow as tf

# Convert the modelMNIST_Sign_tf/saved_model.pb
converter = tf.lite.TFLiteConverter.from_saved_model("/Users/amanda/Projects/SIGN LANGUAGE/MNIST_Sign_tf") # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('sign_lang.tflite', 'wb') as f:
  f.write(tflite_model)