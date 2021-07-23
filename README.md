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


## Yoga Poses

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

<!--
*The training data structure look like this* 

<img src='images/train_dir.png'/>

The reason behind choosing this dataset among others-
- It has images categorized in one of the ten yoga poses
- Is publicly available
- The length of the dataset is suitble for our task with 

<img src='images/bridge.png'/>
-->


# Features

Our project offers three main features which includes Learn, Practice and Meditate. Detailed overview is given below:

-Learn- Learn a multitude of yoga asanas with proper instructions and illustrations on how to perform them correctly.
-Practice- Practice your yoga poses by maximizing your score which will be provided on the basis of the correctness of the yoga pose.
-Meditate-

For now Yoga Pose Detector can accpet any image from the user and classify it into one of the 10 predefined yoga poses. The predicted label is a string telling the yoga pose the person is trying.


## Used Tools & Technologies

-[MediaPipe](https://google.github.io/mediapipe/solutions/pose_classification.html)- This is the main library used in this project. The Pose Classification model we are using is “*BlazePose*” which is the landmark model in MediaPipe Pose that predicts the location of 33 pose landmarks.

-[OpenCV](https://pypi.org/project/opencv-python/)- is a Python library that is used to solve computer vision problems. Computer vision includes understanding and analyzing digital images by the computer and processing the images or providing relevant data after analyzing the image. Used for getting the video feed in the project.

-[NumPy](http://numpy.org/docs)- Used for angle calculation between three particular landmarks fetched from Pose Classification model.

-[Time](https://docs.python.org/3/library/time.html)- module in Python provides various time-related functions. This module comes under Python’s standard utility modules. Used for adding timer in our project.

-[Flask](https://flask.palletsprojects.com/)- It is the backend used in our Project.

-[Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)- Used for deploying our flask app via GitHub.


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

<!--img src='images/mountain_predict.png'/-->


# Future Work:

1. *Adding real time prediction feature*, so that person can perform yoga infront of the webcam and yoga pose detector can classify the pose in real time
2. *Adding scoring feature to tell how well your yoga posture is* Comparing the perfect pose with user's pose will help user to improve by correcting their posture.
3. *Adding Style Transfer*. The person will be able to add stylish backgrounds to their image.



## License
[*MIT License*](https://choosealicense.com/licenses/mit/)

**Inspired by 2021 [AMU BATTLEGROUNDS](https://mlsa-amu.github.io/#/) Hackathon Contest**.
