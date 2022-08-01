---
date: 2018-09-01
title: drought index observatory - Spain
tags: [maps, visualization, drought, heatmaps]
technologies: r; ggplot2; ggmap; rgdal; dplyr; tidyr; ncdf4;
thumbnail: drought_map_001.gif
img: drought_map_001.gif
github: https://github.com/imartinezl/drought-map
---

This project attempts to find an accesible and friendly way to visualize data of drought indices in Spain from 1961 until 2017. The dataset was downloaded from [http://monitordesequia.csic.es](http://monitordesequia.csic.es "http://monitordesequia.csic.es") under the Open Database License. The purpose of this project is to summarise in a simple way the information of the dataset and hopefully help to identify interesting climate phenomena during the last 50 years in Spain. The first attempt was to visualize the SPEI index heatmap and the timeline of a given space point. The following example represents the overall situation on November 2017, and the series of values in the city of Madrid.