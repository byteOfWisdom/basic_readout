import numpy as np
from matplotlib import pyplot as plt
from sys import argv

if __name__ == "__main__":
    time, voltage = np.genfromtxt(argv[1], unpack=True, skip_header=12, delimiter=",")
    plt.plot(time, voltage)
    plt.show()
