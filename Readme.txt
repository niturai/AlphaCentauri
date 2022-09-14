Alpha Centauri is a three-body system,  Alpha Centauri A, Alpha Centauri B and Proxima Centauri also called Alpha Centauri C. In this system, the two objects (Alpha Centauri A & B) form a binary system and revolve around each other with 80 years periodicity. The Proxima Centauri object is situated very far from this binary system and revolves around it with approximately 547000 years of periodicity. In this project, we also have assumed the fourth object, a fictitious planet. This object rotates around Alpha Centauri A.  During the simulation work; we used different mass and semi-major axis of this planet.


For the orbit simulation, the computation program has been arranged (Run the program step by step) in the following way:- 

1. inicn.py:-        This file creates a txt ("alphacen_ini.txt") file with information about all four objects' parameters. The parameters of 
                     the planet (like mass M, periodicity p, and semi-major axis a (AU) ) can be changed using this python file.

2. pos_vel.py:-      This file creates a txt ("inic_out.txt") file with information about the initial value of position and velocity of all four 
                     objects.

3. parameter.py:-    This file creates the position and time coordinate of all objects in ".npy" format. "dAB.npy" is the x and y coordinate of 
                     the binary system's orbit (Alpha Centauri AB). "dxAB.npy" is for x coordinate and "dyAB.npy" is for y coordinate of the 
                     orbit (AB).

4. orbit_plot.py:-   This file plots the orbit of all objects according to the options given inside it.


Note:- For simulation work of Intensity Interferometry, we don't need the full path of Proxima Centauri. So, "nstep = 18000" has been taken in parameter.py.

The simulation of Intensity Interferometry, the computation program has been arranged in the following way:- 

1. obslen.py:-       This file contains information about the position of the source and the position of the telescope for observation. The 
                     input (like the wavelength of observation, the resolution time of photon detector, the day of observation, duration of  
                     observation, and the average time of observation with the number of nights) can be changed using this file. The arrangement 
                     of telescopes also can be changed using this file. Also the number of channel can be changed in this file.

2. aper.py:-         This file is related to the telescope's aperture. The shape and radius of the aperture also the mask's width and 
                     orientation is the input in this file.

3. intfer.py:-       This file defines the model of intensity interferometry to measure the squared visibility. The parameter value of the 
                     binary source system and general constant parameter value has been taken in this file. The function of the earth's rotation 
                     and the observation area's grids has been defined. 
                     The simulation package dynesty (dynamic nested sampling) has been used to estimate the parameter value.


Note:- Run the intfer.py to simulate intensity interferometry for binary system Alpha Centauri AB. The result will store in a ".pkl" file as "dres.pkl"


Plotting the interferometric data has been arranged in different python files like:-

1. teles_plot.py:-   This file generates the plot of telescope arrangement in meter range.

2. data_plot.py:-    This python file generates the model and simulated data for all baselines.

3. error_plot.py:-   This python file needs the interferometric data for different observation lengths (change "chnl = 1", and number of nights. 
                     Run intfer.py for each different nights.). Then it shows the error reduction to estimate the parameters.

4. corner_plot.py:-  This python file generates the corner plot of the posterior distribution of parameters.

5. fiting_plot.py:-  This file fits the orbit of Alpha Centauri AB with the least-square method and shows the comparison between fitting and  
                     interferometric errors. To check the threshold value of mass, change the mass parameter of the planet "obj2 = 1e-2" 
                     (example, in range 1e-2 to 1e-7) in the "obslen.py" file and then simulate orbit and intensity interferometry.
                     Similarly, to check the orbit (Habitable zone orbit) of the planet, change the period and semi-major axis of the planet 
                     "obj2 = 1" in "obslen.py" and then simulate orbit and intensity interferometry. You also need to change the   
                     "zs=2.5e-7" in "fiting.py" for different period of planet.     

6. mskwth.py:-       This file shows the effect of different widths of the mask strip on the interferometric signal. To see the precise impact 
                     of varying size of mask's width, change the value of observation "Nobs = 1/96" (for 15 minutes of observation) also         
                     take the number of the night "Night = 1" in "obslen.py".

7. mskorn.py:-       This file shows the effect of the different orientation angles of masked aperture on the signal. To see the precise impact  
                     of varying size of mask's width, change the value of observation "Nobs = 1/96" (for 15 minutes of observation) also take 
                     the number of the night "Night = 1" in "obslen.py".

8. varagl.py:-      This file plots a figure to show the variation in signal according to change in the different orientation angles of masked
                     aperture.    

9. varwdth.py:-     This file plots a figure to show the variation in signal according to change in the different widths angles of masked
                     aperture.

10. spflux.py:-       This file plots the spectral photon flux for two blackbodies approximating the alpha Centauri A and B. 

11. simu_data.py:-    This file plots the signal and noise for one baseline with 10 spectral channels for 15 minutes only.



Notes:- 

1. To see the effect of the habitable orbit of the planet, change the input value of the period (p yr) and semi-major axis (a (au)) of the planet in "inicn.py" defined as "obj2".

2. To see the effect of the threshold mass of the planet, change the input value of the planet's mass in "inicn.py", defined as "obj2".

3. To see the effect of observation length on interferometric error reduction, change the number of observation nights in "obslen.py," defined as "Night", also with only one channel, "chnl = 1".    
