---
date: 2021-07-01
title: archABM | architectural agent based modeling
tags: [air quality, covid-19, agent-based simulation, building, aerosol model]
technologies: python; simpy; numpy; pandas; matplotlib;
thumbnail: abm_air_quality_005.jpg
carousel: [abm_air_quality_004.jpg, abm_air_quality_002.jpg, abm_air_quality_003.jpg, abm_air_quality_001.jpg]
link: https://vicomtech.github.io/ArchABM
github: https://github.com/Vicomtech/ArchABM
document: article.pdf
featured: 1
---

Recent evidence suggests that SARS-CoV-2, which is the virus causing a global pandemic in 2020, is predominantly transmitted via airborne aerosols in indoor environments. This calls for novel strategies when assessing and controlling a building’s indoor air quality (IAQ). IAQ can generally be controlled by ventilation and/or policies to regulate human–building-interaction. However, in a building, occupants use rooms in different ways, and it may not be obvious which measure or combination of measures leads to a cost- and energy-effective solution ensuring good IAQ across the entire building. <br>
Therefore, in this article, we introduce a novel agent-based simulator, ArchABM, designed to assist in creating new or adapt existing buildings by estimating adequate room sizes, ventilation parameters and testing the effect of policies while taking into account IAQ as a result of complex human–building interaction patterns. A recently published aerosol model was adapted to calculate time-dependent carbon dioxide (CO2) and virus quanta concentrations in each room and inhaled CO2 and virus quanta for each occupant over a day as a measure of physiological response. <br>
ArchABM is flexible regarding the aerosol model and the building layout due to its modular architecture, which allows implementing further models, any number and size of rooms, agents, and actions reflecting human–building interaction patterns. We present a use case based on a real floor plan and working schedules adopted in our research center. This study demonstrates how advanced simulation tools can contribute to improving IAQ across a building, thereby ensuring a healthy indoor environment.

