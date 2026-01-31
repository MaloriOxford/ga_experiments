from base_alg import *
from primitives import *

dForque = lambda f, a: f * I3 - (a ^ f) * I3 * ni
forque = lambda f, a: line(up(a), up(a + f))