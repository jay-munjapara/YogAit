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

# Idea:

Because of the ongoing pandemic situation and a high alert of third wave individuals would confront lock down once more. Such countless individuals who are going for disconnected yoga classes or individuals who need to do yoga yet can’t manage the cost of the yoga classes, our application is assembled consummately for this sort of crowd.
Our application tackles every one of the essential requirements of the above issue proclamation. Also it not only displays the yoga pose but also confirms whether we are performing the posture effectively, essentially like a fitness coach.
There are numerous yoga and exercise applications that work till now however very few of them group the ability to instruct simultaneously.

# Features:

Our project offers three main features which includes Learn, Practice and Meditate. Detailed overview is given below:

-Learn- Learn a multitude of yoga asanas with proper instructions and illustrations on how to perform them correctly.
-Practice- Practice your yoga poses by maximizing your score which will be provided on the basis of the correctness of the yoga pose.
-Meditate- Practice mindfulness and achieve a mentally clear and emotionally calm and stable state.

# Feasibility: 

Yoga brings together physical and mental disciplines to achieve a peaceful body and mind which everyone is on a quest to find.
This upholds the likelihood of the project being implemented and brought to life  in the real world.
A very major component for the project is a CNN based “BlazePose” model. This is very lightweight hence easy to work and integrate with.


# Tech Stack: 

-MediaPipe- This is the main library used in this project. The Pose Classification model we are using is “BlazePose” which is the landmark model in MediaPipe Pose that predicts the location of 33 pose landmarks.

-OpenCV- is a Python library that is used to solve computer vision problems. Computer vision includes understanding and analyzing digital images by the computer and processing the images or providing relevant data after analyzing the image. Used for getting the video feed in the project.

-NumPy- Used for angle calculation between three particular landmarks fetched from Pose Classification model.

-Time- It’s a module in Python that provides various time-related functions. This module comes under Python’s standard utility modules. Used for adding timers in our project.

-Flask- Flask is a micro web framework written in Python. It is the backend used in our Project.

-Heroku- Used for deploying our flask app via GitHub.


**Inspired by 2021 [AMU BATTLEGROUNDS](https://mlsa-amu.github.io/#/) Hackathon Contest**.
