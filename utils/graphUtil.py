import matplotlib.pyplot as plt

robot_x = 0.9
robot_y = 0.1


def draw(points):
    x = [p[0] for p in points]
    y= [p[1] for p in points]
    plt.plot(x, y, "ro")
    plt.plot([robot_x], [robot_y], "go")
    plt.axis([-0.1, 1.2, -0.1, 1.2])
    plt.show()
