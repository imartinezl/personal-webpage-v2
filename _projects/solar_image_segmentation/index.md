---
date: 2020-10-01
title: solar cells electroluminiscence image segmentation
tags: [computer vision, machine learning, deep learning, segmentation, solar energy, energy, anomaly detection, images, detection, unsupervised learning]
technologies: python; tensorflow; r; latex; tikz;
thumbnail: solar_image_segmentation_004.png
img: solar_image_segmentation_004.png
carousel: [solar_image_segmentation_001.jpg, solar_image_segmentation_002.jpg, solar_image_segmentation_003.jpg]
link: https://doi.org/10.1016/j.solener.2021.03.058
document: article.pdf
---


In the operation & maintenance (O&M) of photovoltaic (PV) plants, the early identification of failures has become crucial to maintain productivity and prolong components’ life. Of all defects, cell-level anomalies can lead to serious failures and may affect surrounding PV modules in the long run. These fine defects are usually captured with high spatial resolution electroluminescence (EL) imaging. The difficulty of acquiring such images has limited the availability of data. <br>
For this work, multiple data resources and augmentation techniques have been used to surpass this limitation. Current state-of-the-art detection methods extract barely low-level information from individual PV cell images, and their performance is conditioned by the available training data. In this article, we propose an end-to-end deep learning pipeline that detects, locates and segments cell-level anomalies from entire photovoltaic modules via EL images. <br>
The proposed modular pipeline combines three deep learning techniques: 1. object detection (modified Faster-RNN), 2. image classification (EfficientNet) and 3. weakly supervised segmentation (autoencoder). The modular nature of the pipeline allows to upgrade the deep learning models to the further improvements in the state-of-the-art and also extend the pipeline towards new functionalities.