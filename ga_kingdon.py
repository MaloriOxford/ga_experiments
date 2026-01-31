from kingdon import Algebra
import numpy as np
from timeit import default_timer
from functools import wraps

import matplotlib.pyplot as plt

def tonp(func):
    @wraps
    def wrapped_func(*args, **kwargs):
        return np.array(func(*args, **kwargs))
    return func

alg = Algebra(2, 0, 1, wrapper=tonp)

l = 6
d = 3 / l
points = [alg.vector(e0=1, e1=i * d - 1.5, e2=0, e3=0).dual() 
               for i in range(l + 1)]

points[l] = alg.vector(e0=2, e1=3, e2=2, e3=4).dual()

def translator(line, dist):
    """ Translate along the line `line` by a distance `dist`. """
    e, e0 = alg.blades.e, alg.blades.e0
    return 1 - 0.5 * dist * (e0 * line.normalized()*e0.dual())

def inverse_kinematics(c):
    # Run four relaxation steps
    for j in range(4):
        # Set the tip to the target. (this will change the length of the last segment.)
        c[-2] = c[-1]
        # Run backwards to the base and restore the lengths along the chain.
        for i in range(l-2, 0, -1):
            c[i] = translator(c[i] & c[i + 1], d) >> c[i + 1]
        # Loop the other way from base to tip again restoring all lengths.
        for i in range(1, l):
            c[i] = translator(c[i - 1] & c[i], -d) >> c[i - 1]




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

inverse_kinematics(points)

xs = np.array([points[i].e02 for i in range(l)])
ys = np.array([points[i].e12 for i in range(l)])

ax.scatter(xs, ys)

plt.show()


# def graph_func():
#     inverse_kinematics(points)
#     return [
#         0x224488, f"Inverse Kinematics",
#         0x008844, *zip(points[1:-1], points[:-2]), # Render line segments [[A,B],[B,C],..]
#         0x880088, points[0], "Base",               # Render base
#         0x00DD88, *points[1:l],                    # Render joint points. [A,B,C,..]  
#         0x880088, points[l], "Target",             # Render target in purple
#     ]

# g = alg.graph(
#     graph_func, grid=True, lineWidth=6, labels=True,
# )