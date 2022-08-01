---
date: 2019-04-01
title: image classification hackathon
tags: [image-classification, supervised learning, deep-learning, neural-network, gpu, training]
technologies: python; pandas; numpy; tensorflow; matplotlib; scikit-learn;
thumbnail: picnic_hackathon_001.jpeg
img: picnic_hackathon_001.jpeg
github: https://github.com/imartinezl/picnic-hackathon-2019
---


The goal of [Picnic Image Classification Hackathon](https://picnic.devpost.com/) on [Devpost](https://devpost.com/) was to design a solution to help in the classification of images of products for customer support.<br>
**Summary**: gather labeled images and build a CNN model to predict the label of unclasssified images.<br>
**Workflow**
1. Setup a Tensorflow data pipeline
2. Image preprocessing: decode + resize + normalize
3. Prepare dataset: repeat + batch + prefetch + change_range
4. Model building on Keras +  Transfer Learning [InceptionV3](https://keras.io/applications/#inceptionv3) as the base model 
5. Model training: fine tuning of top dense layers
6. Predict test labels


<br>**Accomplishments that I'm proud of**

- *Fast training*
Given the amount of training data (almost 8000 images), I was quite surprised about the elapsed training times. I suppose that the pipeline strategy and the hardware (Jetson TX2) helped in rthe reduction of this time.

- *Surprisingly good results*
Given that I did not make any data exploration nor research about the influence of resizing or normalizing the images, it was wonderful to find that the results were very decent. Obtaining better classification scores will require more research and tests.

- *Rapid project*
Thanks to the Tensorflow documentation and the existing tutorials from the community, I was able to setup, learn the know-how and implement a solution in less than a week. It is also true that I was lucky the hackathon deadline was postponed for few days.

<br>**What I learned**
This was my first time attempting to design a image classifier. It was really fun, and I discovered several machine learning libraries that allow to build image classification models. Given my previous experience with Tensorflow on other type of models (regression models basically), and the vast community behind it, I decided to choose Tensorflow to train the image classifier.<br>
On other terms, I also learned the importance of transfer learning, and I was surprised that how well it works! Of course, I realized that the world of image classification is huge, and that there are no magical rules that you can follow to obtain a better solution. This requires experience, tests and a lot of time.