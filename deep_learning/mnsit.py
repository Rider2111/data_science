#!/bin/python3

import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255.
    return image, label

# Init
mnist_data, mnist_info = mnist_dataset = tfds.load(name="mnist", with_info=True, as_supervised=True) # (28, 28, 1)
mnist_train, mnist_test = mnist_data['train'], mnist_data['test']
train_count = mnist_info.splits['train'].num_examples
test_count = tf.cast(mnist_info.splits['test'].num_examples, tf.int64)
print(f"Train data entry count : {train_count}")
print(f"Test data entry count : {test_count}")

# Scaling
mnist_train = mnist_train.map(scale)
mnist_test = mnist_test.map(scale)

# Shuffling
mnist_train = mnist_train.shuffle(10000)
mnist_test = mnist_test.shuffle(10000)

#  Extracting validation
validation_count = tf.cast(0.1 * train_count, tf.int64)
print(f"Validation data entry count : {validation_count}")
mnist_validation = mnist_train.take(validation_count)
mnist_train = mnist_train.skip(validation_count)

# Creating batch
mnist_train = mnist_train.batch(100)
mnist_validation = mnist_validation.batch(validation_count)
mnist_test = mnist_test.batch(test_count)
validation_inputs, validation_target = next(iter(mnist_validation))

# Creating model - 2 hidden layer with 50 nodes each
flattened_input = tf.keras.layers.Flatten(input_shape=(28, 28, 1))
first_hidden_layer = tf.keras.layers.Dense(50, activation="relu")
second_hidden_layer = tf.keras.layers.Dense(50, activation="relu")
output_layer = tf.keras.layers.Dense(10, activation="softmax")
model = tf.keras.Sequential([flattened_input, first_hidden_layer, second_hidden_layer])

# Compiling
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy", metrics=['accuracy'])

# Training
model.fit(mnist_train, epochs=5, validation_data=(validation_inputs, validation_target), verbose=2)