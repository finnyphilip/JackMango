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
1. Explaining the working of project
2. Embed video of project demo
## Libraries Used
1. Tensorflow - 2.5.0
2. Keras - 2.4.3
3. Flask - 1.0.2
4. NumPy - 1.19.5
5. Matplotlib - 3.0.3
## How to Configure
Download the full file as zip . For trained model click [Here](https://drive.google.com/file/d/1T_zHntA7DccCJKorU_INCcRLe8HGqpDO/view?usp=sharing).
## Training 
Extract the downloaded file. Create two new folders in your working directory and name it traning and validation. In those training and validation folder 
create two new folders in the same name as jackfruit and mango. And put the traing images in training folder like mango images in mango folder and 
jackfruit images in jackfruit folder. Do the same in validation folder. Open the extracted file and open the python file for training in the training folder.
In the training python file give the appropriate directory for dataset creation 
(like eg:training_dataset = train.flow_from_directory('training_dataset=train.flow_from_directory('training/',........).
Give the proper directory for saving the trained model. Run the code , it will take some time depending upone your file. And check the model is saved.
## Testing
Open the testing folder from extracted file and open the testing python file. Create a folder give name as testing. Put the images of mangos and jackfruit different.
The image should be different from training and validation images.
Give the directory for import the saved model and run the code.

## How to Run
The downloaded file contain a main.py python file, also download the trained model from [Here](https://drive.google.com/file/d/1T_zHntA7DccCJKorU_INCcRLe8HGqpDO/view?usp=sharing). Open the python file and give the proper directory for importing the trained model. The html and css file is attached to the python file. Open the terminal and select directory and run the program. When it start to running the local ip print in the terminal and open the ip You can get the webapp. When starting the web app you can see the file selecting option click there and select the image you want to predict. After selecting you can preview the image you have been selected, then click the predic button and it predict the image of a mango or jackfruit.
This is a binary classification, so we can't get more than two result !.
