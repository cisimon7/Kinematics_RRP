from ForwardImpl import forwardKinematics
from InverseImpl import inverseKinematics
from math import pi
from numpy import round


def forward_tests():
    # test cases
    # you can add more test cases here
    # angles input should be in degrees
    test_cases = [
        # q1, q2, a2, d1, d3
        [25, 45, 1, 2, 1],
        [30, 50, 1, 2, 1]
    ]

    f_function = forwardKinematics()

    for i, param in enumerate(test_cases):
        h = f_function((
            (param[0] * (pi/180)),  # q1
            (param[1] * (pi/180)),  # q2
            param[2],  # a2
            param[3],  # d1
            param[4]   # d3
        ))

        view = f"CASE {i + 1}:\n{round(h, 4)}\n"
        print(view)


def inverse_tests():
    # test cases
    # you can add more test cases here
    # angles input should be in degrees
    test_cases = [
        # px, py, pz, a2, d1
        [-0.597672, 1.28171, 3.41421, 1, 2],
        [-0.642788, 1.11334, 3.53209, 1, 2]
    ]

    func = inverseKinematics()
    q1, q21, q22, d3 = func[0], func[1], func[2], func[3]

    for i, param in enumerate(test_cases):
        x, y, z, a2, d1 = param
        h1 = [
            q1((y, x)) * (180/pi),
            q21((d1, z, x, y)) * (180/pi),
            d3((a2, x, y, d1, z))
        ]
        h2 = [
            q1((y, x)) * (180/pi),
            q22((d1, z, x, y)) * (180/pi),
            d3((a2, x, y, d1, z))
        ]

        view = f"CASE {i + 1}:\nsolution 1: {round(h1, 4)}\nsolution 2: {round(h2, 4)}\n"
        print(view)


if __name__ == '__main__':
    forward_tests()
    inverse_tests()
