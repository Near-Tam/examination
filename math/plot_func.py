import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')

if __name__ == '__main__':
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # y_cos = np.cos(np.exp(x))
    y1 = np.cos(np.power(x[0:128], 2)) + 1.5
    y2 = np.cos(np.power(x[128:], 2))
    plt.figure(1)
    plt.plot(x[0:128], y1)
    plt.plot(x[128:], y2)
    plt.savefig('o.png')
