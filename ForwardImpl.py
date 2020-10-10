from numpy import set_printoptions
from sympy import trigsimp, lambdify
from utils import *

# Joint parameters declaration
q1, q2, a2, d1, d3 = symbols("q1 q2 a2, d1 d3", real=True)

# Forward Kinematics Homogeneous Matrix
#   Rz(q1)*Tz(d1)*Rx(q2)*Ty(a2)*Ty(d3)
H = Rz(q1)*Tz(d1)*Rx(q2)*Ty(a2)*Ty(d3)
H = trigsimp(H)

set_printoptions(suppress=True)


def forwardKinematics():
    return lambdify([(q1, q2, a2, d1, d3)], H, "numpy")
