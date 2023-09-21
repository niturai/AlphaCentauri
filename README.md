The Alpha Centauri system consists of three celestial bodies: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri, also known as Alpha Centauri C. Within this system, Alpha Centauri A and Alpha Centauri B comprise a binary system, orbiting each other with a periodicity of 80 years. Proxima Centauri is located significantly from this binary system and has an orbital period of approximately 547,000 years around it. In the context of this project, we have introduced a fictional planet that orbits Alpha Centauri A. Throughout the simulation, we have varied the planet's mass and semi-major axis.


**The computation program for the orbit simulation has been organized to run step by step in the following manner:**

**1.** _inicn.py_ :- It creates a txt ("alphacen_ini.txt") file with information about all four objects' parameters. The parameters of the planet (like mass M, periodicity p, and semi-major axis a (AU) ) can be changed using this Python file.

**2.** _pos_vel.py_ :- It creates a txt ("inic_out.txt") file with information about the initial position and velocity value of all four objects.

**3.** _parameter.py_ :- It creates the position and time coordinate of all objects in ".npy" format. "dAB.npy" is the x and y coordinate of the binary system's orbit (Alpha Centauri AB). "dxAB.npy" is for x coordinate and "dyAB.npy" is for y coordinate of the orbit (AB).

**4.** _orbit_plot.py_ :- It plots the orbit of all objects according to the options.

**Note**  We do not need the full path of Proxima Centauri to simulate the orbit of Alpha Centauri AB. However, we would like to see the effect of it on binary. So, "nstep = 18000" has been taken in parameter.py.

**The simulation of Stellar Intensity Interferometry, the computation program has been arranged in the following way** 

**1.** _obslen.py_ :- It contains information about the position of the source and the telescope's position for observation. The input (like the wavelength of observation, the resolution time of the photon detector, the day of observation, the duration of observation, the number of channels, and the average time of observation with the number of nights) can be changed using this file. The arrangement of telescopes also can be changed here.

**2.** _aper.py_ :- It is related to the telescope's aperture. The input in this file is the shape and radius of the aperture and the mask's width and orientation for the masked aperture.

**3.** _intfer.py_ :- It defines the model of stellar intensity interferometry to measure the squared visibility. The parameter value of the binary source system and general constant parameter value have been taken in this file. The function of the earth's rotation and the observation area's grids has been defined. The simulation package dynesty (dynamic nested sampling) estimates the parameter value here.


Run the intfer.py to simulate intensity interferometry for binary system Alpha Centauri AB. The result will be stored in a ".pkl" file as "dres.pkl"


**Plotting the interferometric data has been arranged in different Python files**

**1.** _teles_plot.py_ :- It generates the plot of telescope arrangement in the meter range.

**2.** _data_plot.py_ :- It generates the model and simulated data for all baselines.

**3.** _error_plot.py_ :- It needs the interferometric data for different observation lengths (change "chnl = 1", and the number of nights. Run intfer.py for each different night.). Then, it shows the error reduction to estimate the parameters.

**4.** _corner_plot.py_ :- It generates the corner plot of the posterior distribution of parameters.

**5.** _fiting_plot.py_ :- It fits the orbit of Alpha Centauri AB with the least-square method and compares fitting and interferometric errors. To check the threshold value of mass, change the mass parameter of the planet "obj2 = 1e-2" (example, in range 1e-2 to 1e-7) in the "obslen.py" file and then simulate orbit and intensity interferometry. Similarly, to check the orbit (Habitable zone orbit) of the planet, change the period and semi-major axis of the planet "obj2 = 1" in "obslen.py" and then simulate orbit and intensity interferometry. You also need to change the "zs=2.5e-7" in "fiting.py" for different periods of the planet.     

**6.** _mskwth.py_ :- It shows the effect of different widths of the mask strip on the interferometric signal. To see the precise impact of varying size of the mask's width change the value of observation "Nobs = 1/96" (for 15 minutes of observation), also take the number of the night "Night = 1" in "obslen.py"

**7.** _mskorn.py_ :- It shows the effect of the signal's different orientation angles of masked aperture. To see the precise impact of varying size of mask's width, change the value of observation "Nobs = 1/96" (for 15 minutes of observation) and also take the number of the night "Night = 1" in "obslen.py"

**8.** _spflux.py_ :- It plots the spectral photon flux for two blackbodies approximating the Alpha Centauri A and B.  


**Notes** 

**1.** To see the effect of the habitable orbit of the planet, change the input value of the period (p yr) and semi-major axis (a (au)) of the planet in "inicn.py" defined as "obj2".

**2.** To see the effect of the threshold mass of the planet, change the input value of the planet's mass in "inicn.py," defined as "obj2".

**3.** To see the effect of observation length on interferometric error reduction, change the number of observation nights in "obslen.py," defined as "Night," also "chnl = 1". 
