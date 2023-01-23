---
date: 2022-01-01
title: closed-form diffeomorphic transformations
tags: [time series, warping, diffeomorphism, velocity fields, differential geometry, unsupervised learning, machine learning, deep learning]
technologies: python; pytorch; CUDA; C++; numpy; matplotlib;
thumbnail: temporal_transformers_006.webp
# img: temporal_transformers_002.jpg
carousel: [temporal_transformers_001.jpg, temporal_transformers_002.jpg]
video: temporal_transformers_007.mp4
link: https://arxiv.org/abs/2206.08107
github: https://github.com/imartinezl/difw
document: article.pdf
featured: 1
---

Time series alignment methods call for highly expressive, differentiable and invertible warping functions which preserve temporal topology, i.e diffeomorphisms. Diffeomorphic warping functions can be generated from the integration of velocity fields governed by an ordinary differential equation (ODE). Gradient-based optimization frameworks containing diffeomorphic transformations require to calculate derivatives to the differential equation's solution with respect to the model parameters, i.e. sensitivity analysis. Unfortunately, deep learning frameworks typically lack automatic-differentiation-compatible sensitivity analysis methods; and implicit functions, such as the solution of ODE, require particular care. Current solutions appeal to adjoint sensitivity methods, ad-hoc numerical solvers or ResNet's Eulerian discretization.<br>
In this work, we present a closed-form expression for the ODE solution and its gradient under continuous piecewise-affine (CPA) velocity functions. We present a highly optimized implementation of the results on CPU and GPU. Furthermore, we conduct extensive experiments on several datasets to validate the generalization ability of our model to unseen data for time-series joint alignment. Results show significant improvements both in terms of efficiency and accuracy.<br>
[📝 Paper] | [🖼️ Poster] | [📊 Slides] | [🎥 Video] | [📦 Code] 

[//]: # (References)
   [Iñigo Martinez]: <https://scholar.google.es/citations?user=_VGGVEgAAAAJ>
   [Elisabeth Viles]: <https://scholar.google.es/citations?user=-pRUC-8AAAAJ>
   [Igor G. Olaizola]: <https://scholar.google.es/citations?user=TihmWmAAAAAJ>
   [📝 Paper]:  <https://arxiv.org/abs/2206.08107>
   [🖼️ Poster]: <https://inigo.tech/closed-diffeomorphic/assets/poster.pdf>
   [📊 Slides]: <https://inigo.tech/closed-diffeomorphic/assets/slides.pdf>
   [🎥 Video]:  <https://slideslive.com/38984235/closedform-diffeomorphic-transformations-for-time-series-alignment>
   [📦 Code]:  <https://github.com/imartinezl/difw>