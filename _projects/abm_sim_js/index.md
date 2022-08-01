---
date: 2021-02-01
title: simJS | process-based discrete-event simulation framework
tags: [agent-based simulation, discrete-event simulation, queue, framework]
technologies: js; html;
thumbnail: abm_sim_js_001.png
img: abm_sim_js_001.png
github: https://github.com/imartinezl/simjs
---

simJS is a process-based discrete-event simulation framework based on Javascript.<br>
Processes in simJS are defined by Javascript generator functions. All processes live in an environment. They interact with the environment and with each other via events. When a process yields an event, the process gets suspended. simJS resumes the process, when the event occurs (we say that the event is triggered).<br>
An important event type is the Timeout. Events of this type are triggered after a certain amount of (simulated) time has passed. They allow a process to sleep (or hold its state) for the given time. A Timeout and all other events can be created by calling the appropriate method of the Environment that the process lives in (Environment.timeout() for example).<br>
FlatQueue.js imported from [https://github.com/mourner/flatqueue](https://github.com/mourner/flatqueue).
This library has been inspired in the Python library Simpy [https://simpy.readthedocs.io](https://simpy.readthedocs.io)
