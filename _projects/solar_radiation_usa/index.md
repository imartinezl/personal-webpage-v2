---
date: 2019-03-01
title: solar radiation database visualization
tags: [solar radiation, radiation, visualization, visual analytics]
technologies: r; shiny; leaflet; ggplot2; 
thumbnail: solar_radiation_usa_001.png
img: solar_radiation_usa_001.png
link: https://imartinezl.shinyapps.io/solar-radiation-usa/
github: https://github.com/imartinezl/solar-radiation-usa
---

[DataViz Battle for the month of March 2019](https://www.reddit.com/r/dataisbeautiful/comments/axknia/battle_dataviz_battle_for_the_month_of_march_2019/). The interactive visualization is available [here](https://imartinezl.shinyapps.io/solar-radiation-usa/), and it was built using R and the packages Shiny, ggplot2 and leaflet. Every month, the subreddit [r/dataisbeautiful/](https://www.reddit.com/r/dataisbeautiful/) challenges people across the globe to work with a new dataset. These challenges range in difficulty, filesize, and analysis required. What I love about this competition is the freedom it gives the participants to visualize the dataset. <br>
Typical meteorological year (TMY) stations over all United States were included as circle-markers in an interactive map built with the library Leaflet for R. When an station is hovered, information such as name, location, state and class is pop-up. Moreover, when an station is clicked, the server loads the corresponding *.csv* data file about that station. The solar radiation data is visualized on three different polar graphs. The user can select the variable of interest from the input selector.