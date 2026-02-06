from cga_utils.base_alg import *
import cga_utils.primitives as pr
import cga_utils.mechanics as me
import math

f1 = 5 * e1 + 0 * e2 + 0 * e3
a1 = 0 * e1 + 0 * e2 + 0 * e3

m1 = 5 * pr.point(1, 0, 0)

forque1 = me.forque(f1, a1)

print(math.sqrt((forque1 * forque1).asmatrix()[0,0]))