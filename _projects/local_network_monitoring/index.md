---
date: 2019-08-01
title: Wi-Fi signal data gathering, analysis and visualization
tags: [monitoring, analysis, visualization, wi-fi, network]
technologies: raspberry-pi; r; python; plotly; express;
thumbnail: local_network_monitoring_001.png
img: local_network_monitoring_001.png
github: https://github.com/imartinezl/local-network-monitoring
---

Wi-Fi signal data gathering, analysis and visualization. The main goal of this project is to check the quality signal and coverage of a local Wi-Fi router.
<br>*Wi-Fi network analysis*
- [iwlist](https://linux.die.net/man/8/iwlist): detailed wireless information from a wireless interface
- [python-iwlist](https://github.com/iancoleman/python-iwlist): python scanner and parser for wireless networks
 
<br>*Connected devices*
  - [nmap](https://nmap.org/): open source utility for network discovery and security auditing
  - [nmap python](https://xael.org/pages/python-nmap-en.html): python library which helps in using nmap port scanner

<br>*Data exploration*
  - [R](https://www.r-project.org/) - Programming Language / 3.6.0
  - [RStudio](https://www.rstudio.com/) - IDE for R / 1.2.1335
  - [dplyr](https://dplyr.tidyverse.org/) - A grammar of data manipulation / 0.8.1
  - [ggplot2](https://ggplot2.tidyverse.org/) - Create graphics with R / 3.1.1
  - [jsonlite](https://github.com/jeroen/jsonlite) - JSON Parser and Generator for R / 1.6
  - [lubridate](https://lubridate.tidyverse.org/) - Library for date-times / 1.7.4

<br>*Deployment*
The python script [wifi_analysis2.py](wifi_analysis2.py) was run every minute on a [RaspberryPi3B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) using [crontab](https://crontab.guru/), a cron (time-based job scheduler) expression editor.

<br>*Data visualization*
Every minute, requested data was appended to a csv file. In order to visualize this information, a local server was designed using Node.js [express](https://expressjs.com/) server. This server makes a call to request the csv data and builts a plot using [Plotly.js](https://plot.ly/javascript/)

