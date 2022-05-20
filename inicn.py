par =  "#M (Msun),      P (yr),         a (au),         e,            I (deg),       Omega (deg),     epoch (yr),     omega (deg)"


obj1 = ['1.1']                                                                  # parameters for alphacen A (mass M)

obj2 = ['1e-2', '1', '1', '0', '80', '0', '0', '0']                             # parameters for a planet

obj3 = ['0.9', '79.9', '23.5', '0.518', '79', '204.85', '1875.66', '231.65']    # parameters for alphacen B

obj4 = ['0.1221', '547e3', '8700', '0.5', '107', '126', '285e3', '72']          # parameters for proxima Centauri


f = open("alphacen_ini.txt", "w")


f.write(par)
f.write('\n')

for i in obj1:
    f.write(i + str('\t\t'))

f.write('\n')

for i in obj2:
    f.write(i + str('\t\t'))

f.write('\n')

for i in obj3:
    f.write(i + str('\t\t'))

f.write('\n')

for i in obj4:
    f.write(i + str('\t\t'))
   
f.close()
