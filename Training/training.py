# importing libraries
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model,Sequential
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os

# testing the imported library 
img = image.load_img('image.jpg')
plt.imshow(img)

# generating the training and validation dataset

# initiating training and validation dataset
train = ImageDataGenerator(rescale = 1/255)
validation = ImageDataGenerator(rescale = 1/255)

# convert training images to dataset
training_dataset = train.flow_from_directory('training/',
                                            target_size = (300,300),
                                            batch_size = 5,
                                            class_mode = 'binary')
# convert validation images to dataset
validation_dataset = train.flow_from_directory('validation/',
                                              target_size = (300,300),
                                              batch_size = 5,
                                              class_mode = 'binary')

# checking the labels
training_dataset.class_indices

# classes inside the file
training_dataset.classes
validation_dataset.classes

# definig CNN model
model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3),activation = 'relu',input_shape = (300,300,3)),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    #
                                    tf.keras.layers.Conv2D(32,(3,3),activation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    #
                                    tf.keras.layers.Conv2D(64,(3,3),activation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    #
                                    tf.keras.layers.Flatten(),
                                    #
                                    tf.keras.layers.Dense(512,activation = 'relu'),
                                    #
                                    tf.keras.layers.Dense(1,activation = 'sigmoid')
                                    ])


# compiling the model
model.compile(loss = 'binary_crossentropy',
             optimizer = RMSprop(learning_rate=0.001),
             metrics = ['accuracy'])

# fit model
model_fit = model.fit(training_dataset,
                     steps_per_epoch = 5,
                     epochs = 80,
                     validation_data = validation_dataset)


# saving the model
model.save('model.h5') 
