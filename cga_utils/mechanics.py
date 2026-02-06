from cga_utils.base_alg import *
from cga_utils.primitives import *

dForque = lambda f, a: f * I3 - (a ^ f) * I3 * ni
forque = lambda f, a: line(up(a), up(a + f))