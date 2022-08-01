---
date: 2021-01-01
title: time series clustering for data streams
tags: [time series, clustering, functional data analysis, warping, data analysis, unsupervised learning, machine learning, deep learning]
technologies: python; numba; pytorch; numpy; matplotlib;
thumbnail: time_series_clustering_002.png
carousel: [time_series_clustering_001.png, time_series_clustering_002.png]
link: https://tsclust.readthedocs.io/
github: https://github.com/imartinezl/tsclust
featured: 1
---

Clustering techniques for data streams under limited computational and time resources. These novel unsupervised learning methods can efficiently cluster millions of time series data to understand the underlying dynamics of complex systems and detect anomalies. <br>
We applied these methods in real-world industry projects to identify electrical consumption patterns, monitor underlying machine states, and manufacturing process quality control, among others. There is a wide range of applications for these techniques, including urban trajectories, financial market data, climate data, and biomedical measurements for activity recognition or wellbeing. <br>
Given a infinite stream of time series instances, we cluster these instances into an undetermined number of groups. The data is not bounded in terms of scale, variability, and the number of different normal states of the data is also unbounded. Thus, we can not preset a finite number of groups. This has to be a dynamically changing process.