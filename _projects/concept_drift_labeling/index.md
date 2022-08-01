---
date: 2018-04-01
title: online machine learning | labelling concept drift
tags: [concept drift, anomaly detection, energy, wind turbine, condition based maintenance, labeling, machine learning]
technologies: r; keras; tensorflow; python; pandas; numpy;
thumbnail: concept_drift_labeling_001.jpg
carousel: [concept_drift_labeling_001.jpg, concept_drift_labeling_002.jpg]
link: https://doi.org/10.1007/978-3-319-99626-4_13
document: article.pdf
---

A failure detection system is the first step towards predictive maintenance strategies. A popular data-driven method to detect incipient failures and anomalies is the training of normal behaviour models by applying a machine learning technique like feed-forward neural networks (FFNN) or extreme learning machines (ELM). However, the performance of any of these modelling techniques can be deteriorated by the unexpected rise of non-stationarities in the dynamic environment in which industrial assets operate. This unpredictable statistical change in the measured variable is known as concept drift. <br>
In this article a wind turbine maintenance case is presented, where non-stationarities of various kinds can happen unexpectedly. Such concept drift events are desired to be detected by means of statistical detectors and window-based approaches. However, in real complex systems, concept drifts are not as clear and evident as in artificially generated datasets. <br>
In order to evaluate the effectiveness of current drift detectors and also to design an appropriate novel technique for this specific industrial application, it is essential to dispose beforehand of a characterization of the existent drifts. Under the lack of information in this regard, a methodology for labelling concept drift events in the lifetime of wind turbines is proposed. This methodology will facilitate the creation of a drift database that will serve both as a training ground for concept drift detectors and as a valuable information to enhance the knowledge about maintenance of complex systems.