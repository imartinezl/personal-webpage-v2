---
date: 2017-07-01
title: active tilting control system for lightweight autonomous vehicles
tags: [design, control, suspension, frame, vehicle dynamics, sensor fusion, odometry, manufacturing]
technologies: solidworks; matlab; arduino; vesc; processing; latex; 3d printing; laser cutting; water cutting; 
thumbnail: active_tilting_control_001.jpg
link: https://www.media.mit.edu/projects/pev/people/
github: https://github.com/imartinezl/MIT-Media-Lab-latex-thesis
document: article.pdf
featured: 1
carousel: [active_tilting_control_001.jpg, active_tilting_control_002.png, active_tilting_control_003.jpg, active_tilting_control_004.jpg, active_tilting_control_005.png, active_tilting_control_006.jpg, active_tilting_control_007.png, active_tilting_control_008.png]
---

Most of the trips in the cities are one-person, low-speed, short distance. That is why [City Science](https://www.media.mit.edu/groups/city-science/overview/) group at the [MIT Media Lab](https://www.media.mit.edu/) has designed an autonomous, electric and shared urban vehicle that will take conventional cars out from urban areas. This vehicle concept is called Persuasive Electric Vehicle (PEV). An agile, on-demand, shared and functionally-hybrid tricycle, which is thought to minimize traffic congestion, energy consumption and pollutant emission. <br>
The PEV takes advantage of existing bicycle lanes, provides energy-efficient mobility, and addresses sedentary lifestyles. One meter wide, the PEV is also know as a narrow track vehicle. Due to its dimensions, roll stability is a real issue. The PEV would have to lean into corners in order to compensate for the lateral acceleration and maintain their stability. Therefore, this thesis has been dedicated to the design and fabrication of a three wheeler vehicle with an active tilting system. <br>
The proposed tilting strategy would be automatic and achieved by a dedicated tilting actuator, requiring no additional inputs from the driver. First, the dynamic model of a tilting three wheeler vehicle is replicated, from which a linear model is derived. Then the output feedback regulator is designed, by means of optimal control strategies (Linear-Quadratic Regulator), built to optimize the lateral acceleration of the PEV. This controller has the longitudinal velocity as a parameter, and leads to the minimization of the tilting torque and of the lateral acceleration perceived by the driver, and have good performances as well as good robustness properties.