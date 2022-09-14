import numpy as np
import matplotlib.pyplot as plt

#********************************************#
# load all coordinates file
x = np.load("x_coord.npy")
y = np.load("y_coord.npy")
z = np.load("z_coord.npy")
t = np.load("t_coord.npy")

#*********************************************#
# coordinates plot of each object
plt.close()
plt.rcParams["figure.figsize"]=[8,8]
# alphaCen A
plt.subplot(4,2,1)
plt.plot(t*10**(-13), x[0,:]*10**(-5), color = 'red', linewidth =1)
plt.xlabel('time step t' r'($\times 10^{13}$s)')
plt.ylabel('x' r'($\times 10^5$ls)')
plt.title('x_Coordinate AlphaCen A')
plt.close('x_Coordinate AlphaCen A')

plt.subplot(4,2,2)
plt.plot(t*10**(-13), y[0,:]*10**(-5), color = 'red', linewidth =1)
plt.xlabel('time step t' r'($\times 10^{13}$s)')
plt.ylabel('y' r'($\times 10^5$ls)')
plt.title('y_Coordinate AlphaCen A')
plt.close('y_Coordinate AlphaCen A')
#alphaCen's exoplanet
plt.subplot(4,2,3)
plt.plot(t*10**(-13), x[1,:]*10**(-5), color = 'green', linewidth =1)
plt.xlabel('time step t' r'($\times 10^{13}$s)')
plt.ylabel('x' r'($\times 10^5$ls)')
plt.title('x_Coordinate Exoplanet')
plt.close('x_Coordinate Exoplanet')

plt.subplot(4,2,4)
plt.plot(t*10**(-13), y[1,:]*10**(-5), color = 'green', linewidth =1)
plt.xlabel('time step t' r'($\times 10^{13}$s)')
plt.ylabel('y' r'($\times 10^5$ls)')
plt.title('y_Coordinate Exoplanet')
plt.close('y_Coordinate Exoplanet')
#alphaCen B
plt.subplot(4,2,5)
plt.plot(t*10**(-13), x[2,:]*10**(-5), color = 'blue', linewidth =1)
plt.xlabel('time step t' r'($\times 10^{13}$s)')
plt.ylabel('x' r'($\times 10^5$ls)')
plt.title('x_Coordinate AlphaCen B')
plt.close('x_Coordinate AlphaCen B')

plt.subplot(4,2,6)
plt.plot(t*10**(-13), y[2,:]*10**(-5), color = 'blue', linewidth =1)
plt.xlabel('time step t' r'($\times 10^{13}$s)')
plt.ylabel('y' r'($\times 10^5$ls)')
plt.title('y_Coordinate AlphaCen B')
plt.close('y_Coordinate AlphaCen B')
#alphaCen C
plt.subplot(4,2,7)
plt.plot(t*10**(-13), x[3,:]*10**(-5), color = 'magenta', linewidth =1)
plt.xlabel('time step t' r'($\times 10^{13}$s)')
plt.ylabel('x' r'($\times 10^5$ls)')
plt.title('x_Coordinate AlphaCen C')
plt.close('x_Coordinate AlphaCen C')

plt.subplot(4,2,8)
plt.plot(t*10**(-13), y[3,:]*10**(-5), color = 'magenta', linewidth =1)
plt.xlabel('time step t' r'($\times 10^{13}$s)')
plt.ylabel('y' r'($\times 10^5$ls)')
plt.title('y_Coordinate AlphaCen C')
plt.close('y_Coordinate AlphaCen C')

plt.tight_layout()
plt.show()

#********************************************#
#Orbit plot of each four object
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]

plt.plot(x[0,:]*10**(-5), y[0,:]*10**(-5),color = 'red', linestyle= 'dashdot', linewidth = 1.2, label = r'$\alpha$''-Cen A')
plt.plot(x[1,:]*10**(-5), y[1,:]*10**(-5),color = 'green', linestyle= 'dotted', linewidth = 1.2, label = r'$\alpha$''-Cen A planet')
plt.plot(x[2,:]*10**(-5), y[2,:]*10**(-5),color = 'blue', linestyle= 'dashed', linewidth = 1.2, label = r'$\alpha$''-Cen B')
plt.plot(x[3,:]*10**(-5), y[3,:]*10**(-5),color = 'magenta', linestyle= 'solid', linewidth = 1.2, label = r'$\alpha$''-Cen C')

plt.title('Orbit Plots for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 10)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.legend()
plt.show()

#*********************************************#
#Orbit plot of binary system with planet
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]

plt.plot(x[0,:18000]*10**(-5), y[0,:18000]*10**(-5),color = 'red', linestyle= 'dashdot', linewidth = 1.2, label = r'$\alpha$''-Cen A')
plt.plot(x[1,:18000]*10**(-5), y[1,:18000]*10**(-5),color = 'green', linestyle= 'dotted', linewidth = 1.2, label = r'$\alpha$''-Cen A planet')
plt.plot(x[2,:18000]*10**(-5), y[2,:18000]*10**(-5),color = 'blue', linestyle= 'dashed', linewidth = 1.2, label = r'$\alpha$''-Cen B')

plt.title('Orbit Plots for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 10)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)' , fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.legend()
plt.show()

#*********************************************#
#Orbit plot of binary system AlphaCen-AB  
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]

plt.plot(x[0,:18000]*10**(-5), y[0,:18000]*10**(-5),color = 'red', linestyle= 'dashdot', linewidth = 1.2, label = r'$\alpha$''-Cen A')
plt.plot(x[2,:18000]*10**(-5), y[2,:18000]*10**(-5),color = 'blue', linestyle= 'dashed', linewidth = 1.2, label = r'$\alpha$''-Cen B')

plt.title('Orbit Plots for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 10)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.legend()
plt.show()

#*********************************************#
#Orbit plot of AlphaCen A with planet
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]

plt.plot(x[0,:18000]*10**(-5), y[0,:18000]*10**(-5),color = 'red', linestyle= 'dashdot', linewidth = 1.2, label = r'$\alpha$''-Cen A')
plt.plot(x[1,:18000]*10**(-5), y[1,:18000]*10**(-5),color = 'green', linestyle= 'dotted', linewidth = 1.2, label = r'$\alpha$''-Cen A planet')

plt.title('Orbit Plots for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 10)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)' , fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.legend()
plt.show()

#*********************************************#
#Respective Orbit plot of Binary System AlphaCen-AB
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]

plt.plot((x[0,:18000]-x[2,:18000])*10**(-5), (y[0,:18000]-y[2,:18000])*10**(-5),color = 'red', linestyle= 'solid', linewidth = 1.2, label = r'$\alpha$-Cen A w.r.t $\alpha$-Cen B')

plt.title('Orbit Plots for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 10)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)' , fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.subplots_adjust(left=0.16, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.legend()
plt.show()

#********************************************#
# Orbit plot of alphaCen A w.r.t. alphaCen C
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]

plt.plot((x[0,:18000]-x[3,:18000])*10**(-5), (y[0,:18000]-y[3,:18000])*10**(-5),color = 'red', linestyle= 'dashdot', linewidth = 1.2, label = r'$\alpha$-Cen A w.r.t $\alpha$-Cen C')

plt.title('Orbit Plots for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 10)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)' , fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.subplots_adjust(left=0.14, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.legend()
plt.show()

#*********************************************#
# One Orbit plot of alphaCen A w.r.t. planet
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]

plt.plot((x[0,:28]-x[1,:28])*10**(-5), (y[0,:28]-y[1,:28])*10**(-5),color = 'red', linestyle= 'solid', linewidth = 1.2, label = r'$\alpha$-Cen A w.r.t. planet')

plt.title('Orbit Plots for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 35)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)' , fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.subplots_adjust(left=0.16, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.legend(bbox_to_anchor=(0., 1.00, 1., .102), loc='lower left', ncol=2, mode = "expand", borderaxespad= 0.0)
plt.show()

#***********************************************#
# plot of alpha cen-A for approximatly 6 years to see the wobble 
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]
plt.plot(x[0,:200]*10**(-5), y[0,:200]*10**(-5),color = 'red', linestyle= 'solid', linewidth = 1.5)
plt.title('Wobble nature of 'r'$\alpha$-Cen A for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 20)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)' , fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.subplots_adjust(left=0.16, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.show()

#***********************************************#
# plot the orbit of alpha cen-B for approximatly 6 years
plt.close()
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = [8,8]
plt.plot(x[2,:200]*10**(-5), y[2,:200]*10**(-5),color = 'blue', linestyle= 'solid', linewidth = 1.5)
plt.title('Orbit plot of 'r'$\alpha$-Cen B for Mass Ratio ' r'$\frac{M_P}{M_A} = 0.009 $', fontweight = 'bold', pad = 20)
plt.xlabel('x-Coordinates (' r'$\times 10^{5}$ ls)' , fontsize=18, color='black')
plt.ylabel('y-coordinate (' r'$\times 10^{5}$ ls)', fontsize=18, color='black')
plt.subplots_adjust(left=0.16, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.show()

