---
date: 2019-02-01
title: newspaper | rss + article scraping
tags: [newspaper, web-development, scraping, front-end, back-end]
technologies: python; flask; heroku; feedparser; rss;
thumbnail: newspaper_scraping_001.png
img: newspaper_scraping_001.png
github: https://github.com/imartinezl/newspaper-scraping
---

Open & free access to subscription-based regional newspaper through RSS + article scraping. <br>
The [diariovasco](https://www.diariovasco.com/) is a regional newspaper from Gipuzkoa, in Spain. The online version of the newspaper was open-access until 2017, but since then an over-priced subscription is necessary. Even though we usually read the national news through other mediums, we were missing lots of info about local matters. That is the reason why I set out to provide a open and free access to this regional newspaper.<br>
Fortunately the articles are indexed through RSS every 30 minutes. The articles can be accessed, but the content is blocked by a pop-up, so I use a simple article scraper ([Newspaper3k](https://newspaper.readthedocs.io/en/latest/)) for extrating the title, subtitle, main image and text. Finally, a simple [Flask](http://flask.pocoo.org/) webpage was built to allocate the content and deployed on [Heroku](https://www.heroku.com/).