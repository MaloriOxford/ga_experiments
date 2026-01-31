from base_alg import *

up = lambda x: no + x + 0.5 * x * x * ni                                    # Up project a Euclidean vector to a homogeneous point
point  = lambda x, y, z: no + x*e1 + y*e2 + z*e3 + 0.5*(x*x+y*y+z*z)*ni     # Same as up but with separate arguments

dSphere = lambda x,y,z,r: (point(x,y,z) - r**2/2*ni).dual()                 # Generate a dual sphere from Euclidean parameters
sphere = lambda p1, p2, p3, p4: p1 ^ p2 ^ p3 ^ p4                           # Generate a sphere as the intersection of four points

# dPlane = lambda: 1
plane = lambda p1, p2, p3: sphere(p1, p2, p3, ni)                           # Generate a plane as the intersection of three points with the point at infinity

# dCircle = lambda:
circle = lambda p1, p2, p3: p1 ^ p2 ^ p3                                    # Generates a circle as the intersection of three points

# dLine   = lambda a,b,c,d: (a*e1 + b*e2 + d*ni).dual()                       
line = lambda p1, p2: circle(p1, p2, ni)                                    # Generates a line as the intersection of two points with the point at infinity

# dPointPair = lambda:
# pointPair = lambda: