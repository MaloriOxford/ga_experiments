# Basics to construct 3D Conformal Geometric Algebra

from kingdon import Algebra

alg = Algebra(4, 1)
locals().update(alg.blades)

ni = e4 + e5                                    # The point at infinity
no = 0.5 * (e5 - e4)                            # The point at the origin
nino = ni ^ no

I3 = e123