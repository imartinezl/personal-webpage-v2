---
date: 2019-05-01
title: population density map - Europe
tags: [maps, visualization, tiles, gis, density, population]
technologies: r; ggplot2; dplyr; carto; mapbox; github; mbtiles; geojson;
thumbnail: population_map_006.webp
img: population_map_001.gif
carousel: [population_map_002.png, population_map_005.png]
link: https://imartinezl.github.io/population-map/
github: https://github.com/imartinezl/population-map
featured: 1
---


Analysis of the population density in Europe and in Spain. It covers the entire data ETL pipeline: data extraction from european and spanish public institutions, data transformation and analysis, and a visualization stage. Please, notice that the used datasets are quite large in size, and thus the project has been concieved from an educational point of view, always looking for the maximum efficiency in the entire pipeline.<br>
**Visualize the least populated regions in Europe**
I was very much inspired by [this article](https://www.citymetric.com/fabric/nine-things-we-learned-population-density-map-europe-3775) where John Elledge introduces the visualization of [Dan Cookson](https://twitter.com/danc00ks0n), a map with the EU Population at 2011 onto a 1km grid. This great visualization is available [here](https://dancooksonresearch.carto.com/u/dancookson/viz/49ca276c-adf9-454a-8f64-0ccf0e46eed0/embed_map).<br>
**Learn how to approach the visualization of large spatial datasets**
Prior to this project, I had some experience working with small spatial datasets. Therefore, a large dataset presented a nice challenge! The european 1km per 1km square grid dataset comprises over 2.000.000 features that need to be processed and rendered onto the map.
