# ray_sphere_intersection.py
# Written by Andres Sanchez
# Other contributors: None

# import Python modules
import math # math 
import sys # argv

#constants 
REKM = 6378.137
EE    = 0.081819221456

# initialize script arguments
d_l_x = float('nan') 
d_l_y = float('nan') 
d_l_z = float('nan') 
c_l_x = float('nan') 
d_l_y = float('nan') 
d_l_z = float('nan') 

# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
    )
    exit()
#write below 

a = d_l_x*d_l_x + d_l_y*d_l_y + (d_l_z*d_l_z)/(1-EE*EE)
b = 2*(d_l_x*c_l_x+d_l_y*c_l_y+(d_l_z*c_l_z)/(1-EE**2))
c = c_l_x**2+c_l_y**2+(c_l_z**2)/(1-EE**2)-REKM**2
discr = b*b-4.0*a*c

#calculate the discriminant 
#from slides
discr = (b**2 -4*a*c)
if discr >= 0:
    d = (-b - math.sqrt(discr))/(2*a)
    if d < 0:
        d = (-b + math.sqrt(discr))/(2*a)
    if d > 0:
        l_d = [d*d_l_x+c_l_x, d*d_l_y+c_l_y, d*d_l_z+c_l_z]

print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point
