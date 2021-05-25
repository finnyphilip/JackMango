![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# JackMango ML Classifier
This project can be used to predict a given image is a Mango or Jackfruit using Machine Learning. A CNN algorithm is at the heart of this project which was implemented through tensorflow machine learning library. A web app can classify the given image is a Mango or Jackfruit.
## Team members
1. [Mohammed Fudhail P](https://github.com/mhdfudhail)
2. [Finny Philip Biju](https://github.com/finnyphilip)
## Team Id
BFH/recpYsFoGnBOXGQeF/2021
## Link to product walkthrough
[link to video]
## How it Works ?
1. A CNN algorithm is created using tensorflow an keras libraries. 
2. The training dataset is created using images of mango and Jackfruit from google images.
3. A trained model created using the dataset and saved as '.h5' file.
4. A web app is created using flask API with HTML5, CSS and Javascript.
5. The trained model is loaded in the web app backend.
6. When a image is imported to the web app, it is saved in the folder 'image'. 
7. Image is processed in the trained model and it will predict whether the image is of a Mango or Jackfruit. 
## Libraries Used
1. Tensorflow - 2.5.0
2. Keras - 2.4.3
3. Flask - 1.0.2
4. NumPy - 1.19.5
5. Matplotlib - 3.0.3
## How to Configure
Download the repository as zip. For downloading trained model click [Here](https://drive.google.com/file/d/1T_zHntA7DccCJKorU_INCcRLe8HGqpDO/view?usp=sharing).
## Training 
1. Extract the downloaded file.
2. Create two new folders in your working directory and name it 'traning' and 'validation'.
3. In these training and validation folder create two new folders in the same name as 'jackfruit' and 'mango'.
4. Keep the traing images in 'training' folder like mango images in 'mango' folder and jackfruit images in jackfruit folder. 
   Repeat the same for validation folder. 
5. Open the extracted file and python file for training in the 'training' folder.
6. In the training python file give the appropriate directory for dataset creation 
( eg:training_dataset = train.flow_from_directory('training_dataset=train.flow_from_directory('training/',........).
7. Give the proper directory for saving the trained model. Run the code , it will take some time depending upon your training file. And check the model whether is saved.
## Testing
1. Open the 'testing' folder from extracted file and open the testing python file. Create a folder and give name as 'test'. 
2. Keep images of both mango and jackfruit in the 'test' folder.The image should be different from training and validation images.
3. Give the directory to import the saved model and run the code.
## How to Run
1. The downloaded file contain a main.py python file, also download the trained model from [Here](https://drive.google.com/file/d/1T_zHntA7DccCJKorU_INCcRLe8HGqpDO/view?usp=sharing). 
2. Open the python file and give the proper directory for importing the trained model. The html and css file is attached to the python file. 
3. Open the terminal, select the directory and run the program. 
4. When it starts to run, the local IP print in the terminal. Open the IP in the browser and the webapp opens.
5. While starting the web app, you can see the file selection option. Click there and select the image you want to predict.
6. After selecting you can preview the image you have been selected. Click the 'predict' button and it predicts whether the image is a mango or jackfruit.

Note: This is a binary classification, so we can't get more than two result !
