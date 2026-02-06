from cga_utils.base_alg import *
import math

dist   = lambda x,y: (2*(x.rc(y)).norm)**0.5                                        # The distance between two unnormalized points
angle  = lambda x,y: math.acos(x.normalized().dual().rc(y.normalized().dual()))     # The angle between ?