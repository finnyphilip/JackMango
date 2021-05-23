from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np


app = Flask(__name__)

model = load_model('new_model.h5')

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    imagePath = './image/' +imagefile.filename
    imagefile.save(imagePath)
    
    img = load_img(imagePath, target_size=(300,300))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    images = np.vstack([x])
    option = model.predict(images)

    if option == 0:
        print('This is Jackfruit')
        object_is = 'Jackfruit'
    elif option == 1:
        print('this is Mango')
        object_is = 'Mango'
    else:
        print("I don't understand")
        object_is = "I don't understand'"
        

    return render_template('index.html', prediction = object_is)
if __name__=='__main__':
    app.run(port=3000, debug=True)
