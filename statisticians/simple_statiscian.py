import matplotlib.pyplot as plt
import numpy as np
import os
import plotly.graph_objects as go
import pytest


from scipy.optimize import curve_fit


class Statiscian:

    def __init__(self):
        pass

    def get_prepared_for_plotting(self, array: np.array):
        means = np.zeros(array.shape[0])
        stds = np.zeros(array.shape[0])
        for i in range(array.shape[0]):
            means[i] = array[i].mean()
            stds[i] = np.std(array[i]) / np.sqrt(array.shape[1])
        return means, stds

    def make_plot(self, running_times: np.array,
                  x_label_, y_label_, out_filename):
        means, stds = self.get_prepared_for_plotting(running_times)
        X = np.arange(running_times.shape[0])
        Y = means
        # fit a line
        k, b = self.approximate_curve(X, Y, self.line)
        fitted_line = X * k + b
        # fit a hyperbola
        a, b = self.approximate_curve(X, Y, self.hyperbola)
        fitted_hyperbola = X**b * a
        #
        plt.plot(X, Y, 'g')
        plt.fill_between(X, Y - 1 * stds, Y + 1 * stds, color='r', alpha=0.50)
        plt.plot(X, fitted_line, color='blue')
        plt.plot(X, fitted_hyperbola, color='yellow')
        plt.legend(('Complexity',
                    "Approximated 1",
                    "Approximated 2",
                    '+/- 3xstd'))
        plt.ylabel(y_label_)
        plt.xlabel(x_label_)
        plt.savefig(os.path.join("./results", out_filename + '.jpg'),
                    format='jpg',
                    )
        plt.tight_layout()

    def make_table(self, running_times: np.array,
                   occurences: list,
                   substrings_lengths: list):
        headerColor = 'grey'
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['<b>Substring length</b>',
                        '<b>Amount of occurrences</b>',
                        '<b>Algorithm running time</b>'],
                line_color='darkslategray',
                fill_color=headerColor,
                align=['center', 'center'],
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[
                    substrings_lengths,
                    occurences,
                    running_times,
                ],
                line_color='darkslategray',
                # 2-D list of colors for alternating rows
                fill_color=[[rowOddColor,
                             rowEvenColor,
                             rowOddColor,
                             rowEvenColor,
                             rowOddColor] * 3],
                align=['left', 'center'],
                font=dict(color='darkslategray', size=11)
            ))
        ])

        fig.show()

    def complete_statistic(self, config: dict):
        """Нужна, кодгда хотим подвести статистику по нескольким алгоритмам:
         несколько результатов на одном графике или общая сводная таблица."""
        raise NotImplementedError()

    def approximate_curve(self, X, Y, func):
        popt, popv = curve_fit(func, X, Y, maxfev=100)
        return popt[0], popt[1]

    @staticmethod
    def line(x, k, b):
        y = k * x + b
        return y

    @staticmethod
    def hyperbola(x, a, b):
        y = x**b * a
        return y


if __name__ == "__main__":
    pass
