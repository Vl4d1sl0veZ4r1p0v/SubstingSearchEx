import matplotlib.pyplot as plt
import numpy as np
import os
import pytest

from scipy.optimize import curve_fit


class Statiscian:

    def __init__(self, array):
        self.array = array

    def get_prepared_for_plotting(self):
        means = np.zeros(self.array.shape[0])
        stds = np.zeros(self.array.shape[0])
        for i in range(self.array.shape[0]):
            means[i] = self.array[i].mean()
            stds[i] = np.std(self.array[i]) / np.sqrt(self.array.shape[1])
        return means, stds

    def make_plot(self, x_label_, y_label_, out_filename):
        means, stds = self.get_prepared_for_plotting()
        X = range(self.array.shape[0])
        Y = means
        k, b = self.approximate_line(X, Y)
        fitted_line = np.arange(self.array.shape[0]) * k + b
        plt.plot(X, Y, 'g')
        plt.fill_between(X, Y - 1 * stds, Y + 1 * stds, color='r', alpha=0.50)
        plt.plot(np.arange(self.array.shape[0]), fitted_line, color='blue')
        plt.legend(('Complexity', "Approximated", '+/- 3xstd'))
        plt.ylabel(y_label_)
        plt.xlabel(x_label_)
        plt.savefig(os.path.join("./results", out_filename + '.jpg'),
                    format='jpg',
                    )
        plt.tight_layout()

    def make_table(self):
        self.table_writer()

    def complete_statistic(self):
        pass

    def approximate_line(self, X, Y):
        popt, popv = curve_fit(self.line, X, Y, maxfev=100)
        return popt[0], popt[1]

    @staticmethod
    def line(x, k, b):
        y = k * x + b
        return y

    # Не уверен, что заработает.
    @staticmethod
    def hyperbola(x, a, b):
        y = x**b * a
        return y


if __name__ == "__main__":
    pass
