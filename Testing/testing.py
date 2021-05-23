from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import os

dirPath = 'testing_images/'
model = load_model('model.h5')

for i in os.listdir(dirPath):
    img = image.load_img(dirPath +'//'+ i,target_size = (300,300))
    plt.imshow(img)
    plt.show()
    
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    images = np.vstack([x])
    option = model.predict(images)
    if option == 0:
        print('This is Jackfruit')
    else:
        print('this is Mango')
