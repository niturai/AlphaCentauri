import numpy as np

N_body = 4
mass = np.zeros(N_body)
pos = np.zeros(shape=(N_body,3))
vel = np.zeros(shape=(N_body,3))

def checks():
    cmx = 0*pos[0]
    cmp = 0*pos[0]
    for i in range(N_body):
        cmx += mass[i]*pos[i]
        cmp += mass[i]*vel[i]
    print('cmx: ',cmx)
    print('cmp: ',cmp)
    kin = pot = 0
    for i in range(N_body):
        kin += mass[i]*np.sum(vel[i]*vel[i])/2
        for j in range(i):
            dr = pos[i]-pos[j]
            r = np.sum(dr*dr)**.5
            pot -= mass[i]*mass[j]/r       
    print('E and vir',kin+pot,-kin/pot)       

checks()

fil = open("inic_out.txt","r")
l = fil.readline().split()                     
 
for i in range(len(l)):                           
    mass[i] = float(l[i])
print('mass = ', mass)

for i in range(N_body):
    l = fil.readline().split()
    for j in range(len(l)):
        pos[i][j] = float(l[j])
print('pos = ', pos)

for i in range(N_body):
    l = fil.readline().split()
    for j in range(len(l)):
        vel[i][j] = float(l[j])
print('vel = ', vel)

cmx = 0*pos[0]
cmv = 0*vel[0]
for i in range(N_body):
    cmx += mass[i]*pos[i]
    cmv += mass[i]*vel[i]

cmx /= np.sum(mass)
cmv /= np.sum(mass)

for i in range(N_body):
    pos[i] -= cmx
    vel[i] -= cmv

print('cmx :', cmx)
print('cmv :', cmv)

dt=1000000
nstep = 17251000

GMsun = 4.9254909e-6

x = np.zeros((N_body, nstep), dtype = float)
y = np.zeros((N_body, nstep), dtype = float)
z = np.zeros((N_body, nstep), dtype = float)
t_stp = np.zeros((nstep,1), dtype = float)

for t in range(nstep):
    if t % 1000000 == 0:
         checks()
    pos += vel*dt/2
    acc = 0*pos
    t_stp[t] = t_stp[t-1]+ dt
    for i in range(N_body):
        for j in range(i):
            dr = pos[i]-pos[j]
            r2 = dr[0]**2 + dr[1]**2 + dr[2]**2
            r3 = r2**1.5
            acc[j,:] += mass[i]*dr/r3
            acc[i,:] -= mass[j]*dr/r3
            
    vel += acc*dt
    pos += vel*dt/2

    x[:,t] = pos[:,0]
    y[:,t] = pos[:,1]
    z[:,t] = pos[:,2]

# save all coordinates in file
np.save('x_coord',x)           
np.save('y_coord',y)           
np.save('z_coord',z)           
np.save('t_coord',t_stp)              

# load all coordinates file 
x = np.load('x_coord.npy')
y = np.load('y_coord.npy')
z = np.load('z_coord.npy')
t = np.load('t_coord.npy')

slice = 1
xs_0 = x[0,::slice]                 
ys_0 = y[0,::slice]                 
xs_1 = x[1,::slice]                 
ys_1 = y[1,::slice]                 
xs_2 = x[2,::slice]                 
ys_2 = y[2,::slice]                 
xs_3 = x[3,::slice]                 
ys_3 = y[3,::slice]                 
ts = t[::slice]

dxAB = np.zeros((N_body, nstep), dtype = float)
dyAB = np.zeros((N_body, nstep), dtype = float)
dAB = np.zeros((2,len(xs_0)), dtype = float)

dAB[0,:] = xs_0 - xs_2            
dAB[1,:] = ys_0 - ys_2            
dxAB = x[0,::] - x[2,::]         
dyAB = y[0,::] - y[2,::]          

np.save('dxAB', dxAB)     # x-coordinate of binary AB        
np.save('dyAB', dyAB)     # y coordinate of binary AB
np.save('dAB', dAB)       # (x,y) coordinate of binary AB


