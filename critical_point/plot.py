# used to plot the curve of p~V

import numpy as np
import matplotlib.pyplot as plt

class PlotFig:

    def __init__(self):
        pass

    def plot_p_V(self, t, a, b, r):

        for i in range(len(t)):
            def p(v):
                return r*t[i]/(v - b) - a/v**2
            v = np.arange(7e-5, 1e-3, 1e-6)
            plt.figure(i)
            plt.plot(v, p(v))
        plt.title('p-V curves')
        plt.ylabel('p')
        plt.xlabel('V')
        plt.show()




