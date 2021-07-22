# yogAit | Yoga Pose Estimation App

[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)
<!--
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)-->


<p align="center">
  <a href="https://github.com/jay-munjapara/yogAit">
    <img src="https://developers.google.com/ml-kit/images/vision/card-pose_detection.png" alt="Logo">
  </a>
</p>


## Table of Content
  * [Demo](#demo)
  * [Overview](##overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [License](#license)
  * [Contact](#contact-)


## Overview:-

This is a Yoga Pose Estimation App which can be able to detect the yoga pose in real time by using posenet and KNN Classifier. Here the dataset used is custom data set which consists of 3 videos for representing 3 different postures. It is deployed in heroku. One Thing to be noted i.e this will work correctly for all mobile and edge devices.

## Motivation:-

This project is done as a part of my internship in ShapeAI in the role of Machine Learning Engineer Intern. This project can be extended to a perfect Yoga Trainer to track the poses and retain fitness using AI.


### Yoga Poses
| Class | Label |
| --- | --- |
| 0 | bridge |
| 1 | child |
| 2 | downwardog |
| 3 | mountain |
| 4 | plank |
| 5 | seatedforwardbend |
| 6 | tree |
| 7 | trainglepose |
| 8 | warrior1 |
| 9 | warrior2 |


*The training data structure look like this* 

<img src='images/train_dir.png'/>

The reason behind choosing this dataset among others-
- It has images categorized in one of the ten yoga poses
- Is publicly available
- The length of the dataset is suitble for our task with 

<img src='images/bridge.png'/>


# Features

For now Yoga Pose Detector can accpet any image from the user and classify it into one of the 10 predefined yoga poses. The predicted label is a string telling the yoga pose the person is trying.


## Used Libraries
- [Keras](https://keras.io/)- This is the main library used in this project. The model is entirely build on Keras including all the image augmentation, transfer learning, training, testing.

- [NumPy](http://numpy.org/docs)- Used for pixels manipulation

- [Matplotlib](http://matplotlib.org/)- To plot images and loss plots.

- [Flask](https://flask.palletsprojects.com/)- Used for deploying our classification model




## Network Architecture
The motivation of using transfer learning for out task came after we implemented a Deep Neural Network from Scratch. The model build from scratch gives accuracy only around 18%-20%. We can boost the accuracy with the help of transfer learning.

Keras application module has variety of pretrained networks which can be easily downloaded.

In our project, we tried multiple networks before settling to MobileNet.


## Model
The pretrained models are trained on the ImageNet Dataset classifying 1000 classes. Our task is to classify the yoga pose in one of the 10 classes, so we modified the classification layer and replaced it with our Dense layer.
The final model is a combination of transfer learning and custom trained classifier.
The training accuracy achieved is *81%* and validation accuracy acheived is *61%*.



## Performance
The model is completely built on the public free available dataset in contrast to the commercial projects that use large datasets with high resolution quality. However, the model is capable of being trained on any dataset and predicting the accurate yoga postures. 
Currently the accuracy is 61% which can be improved with diverse datasets.

<img src='images/mountain_predict.png'/>


# Future Work:

1. *Adding real time prediction feature*, so that person can perform yoga infront of the webcam and yoga pose detector can classify the pose in real time
2. *Adding scoring feature to tell how well your yoga posture is* Comparing the perfect pose with user's pose will help user to improve by correcting their posture.
3. *Adding Style Transfer*. The person will be able to add stylish backgrounds to their image.



## License
[*MIT License*](https://choosealicense.com/licenses/mit/)

**Inspired by 2020 MLH Fellowship Mini Hackathon Contest**.
