import numpy as np
from matplotlib import pyplot as plt
from sys import argv
import std

if __name__ == "__main__":
    time, voltage = np.genfromtxt(argv[1], unpack=True, skip_header=12, delimiter=",")
    plt.plot(time, voltage)
    std.default.plt_finish("time relative to trigger / s", "voltage / v")
