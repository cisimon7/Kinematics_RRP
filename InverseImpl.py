from utils import *
from sympy import symbols, trigsimp, lambdify, diff, init_printing, sqrt, atan2, expand, factor


def inverseKinematics():

    init_printing(use_unicode=True)

    # Constant Joint parameters declaration
    a2, d1 = symbols("a2 d1", real=True)

    # Position of end effector
    px, py, pz = symbols("px, py, pz")

    # From top view of Robot
    # One solution
    q1 = atan2(py, px)

    # Projection of a2 and d3 on the x-y plane
    r = sqrt(px ** 2 + py ** 2)

    # View of Robot from side
    # Possible two solutions
    q21 = atan2(pz - d1, r)

    # Possible two solutions
    q22 = atan2(pz - d1, -r)

    # Length of a2 + d3, denoted as D, from side view of robot
    D = sqrt(r ** 2 + (pz - d1) ** 2)

    # Length of d3 from D
    d31 = D - a2

    q01 = lambdify([(px, py)], q1, "numpy")
    q021 = lambdify([(d1, pz, px, py)], q21, "numpy")
    q022 = lambdify([(d1, pz, px, py)], q22, "numpy")
    d03 = lambdify([(a2, px, py, d1, pz)], d31, "numpy")

    return [q01, q021, q022, d03]
