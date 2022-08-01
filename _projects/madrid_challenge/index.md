---
date: 2019-03-01
title: route optimization for waste collection  - Madrid challenge 
tags: [optimization, routing, data, city, traffic, visualization, visual analytics, simulated annealing]
technologies: r; shiny; leaflet; ggplot2; igraph;
thumbnail: madrid_challenge_001.gif
img: madrid_challenge_001.gif
link: https://imartinezl.shinyapps.io/madrid-challenge/
github: https://github.com/imartinezl/madrid-challenge
---

Open data challenge promoted by [Kopuru](http://kopuru.com/). The [challenge](http://kopuru.com/desafio/reto-open-data-optimizacion-de-la-recogida-de-vidrio-en-madrid-central/) here is to calculate and show on a map which is the shortest route for the collection of glass containers within the district of Madrid Central. In doing so, we could help the City Council of Madrid through the use of data to improve the service to its citizens.  The final result is hosted on [shinyapps.io](https://www.shinyapps.io/).
<br>**Challenge Objectives**
- To create a visualization platform that delimits the area of Central Madrid and collects the geolocation of the different types of containers.
- To calculate and visualize the route to be followed identifying the starting point, route, end point and distance travelled. The team that identifies the shortest route (measured in meters) respecting the direction of the streets will win.

<br>**Route Optimization**
The route optimization was inspired by Todd W. Schneider [approach](https://github.com/toddwschneider/shiny-salesman), where he designs a Shiny app to solve the traveling salesman problem with simulated annealing. Route distances and travel times were queried from [HERE](https://developer.here.com/) maps API. The number of queries were reduced as much as possible, reducing the number of neighbours to a fixed value N, given that the *completeness* of the graph remained untouched. 