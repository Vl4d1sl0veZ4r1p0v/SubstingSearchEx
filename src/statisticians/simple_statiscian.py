import os
import datetime

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit


class Statiscian:

    def __init__(self):
        pass

    @staticmethod
    def get_prepared_for_plotting(array: np.array):
        means = np.zeros(array.shape[0])
        stds = np.zeros(array.shape[0])
        for i in range(array.shape[0]):
            means[i] = array[i].mean()
            stds[i] = np.std(array[i]) / np.sqrt(array.shape[1])
        return means, stds

    def make_plot_time_by_length(
            self,
            running_times: np.array,
            x_label_="Length of input text, letters",
            y_label_="Time of working, seconds",
            out_filename="time" + str(datetime.datetime.now())):
        self.make_plot_by_length(
            usages=running_times,
            x_label_=x_label_,
            y_label_=y_label_,
            out_filename=out_filename
        )

    @staticmethod
    def make_table_time_by_many_strings(running_times: np.array,
                                        occurences: list,
                                        substrings_lengths: list):
        n = len(occurences)
        header_color = 'blue'
        row_even_color = 'lightskyblue'
        row_odd_color = 'white'

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['<b>Substring length</b>',
                        '<b>Amount of occurrences</b>',
                        '<b>Algorithm running time</b>'],
                line_color='darkslategray',
                fill_color=header_color,
                align='center',
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[
                    substrings_lengths,
                    occurences,
                    running_times,
                ],
                line_color='darkslategray',
                fill_color=[
                    [
                        [row_even_color, row_odd_color][i % 2]
                        for i in range(n)
                    ] * 3
                ],
                align='center',
                font=dict(color='black', size=13)
            ))
        ])
        fig.update_layout(width=600, height=600)
        fig.show()

    def complete_statistic(self, config: dict):
        """Нужна, когда хотим подвести статистику по нескольким алгоритмам:
         несколько результатов на одном графике или общая сводная таблица."""
        raise NotImplementedError()

    def make_plot_memory_by_length(
            self,
            memory_usages: np.array,
            x_label_="Length of input text, letters",
            y_label_="Used memory, MiB",
            out_filename="memory"+str(datetime.datetime.now())
    ):
        self.make_plot_by_length(
            usages=memory_usages,
            x_label_=x_label_,
            y_label_=y_label_,
            out_filename=out_filename
        )

    def make_plot_by_length(self, usages: np.array,
                            y_label_,
                            x_label_,
                            out_filename
                            ):
        fig, ax = plt.subplots(figsize=(9, 6))
        means, stds = self.get_prepared_for_plotting(usages)
        X = np.arange(1, usages.shape[0] + 1)
        Y = means
        lower_bounds = Y - 1 * stds
        upper_bounds = Y + 1 * stds
        intervals = [
            [lower_bounds[i],
             Y[i],
             upper_bounds[i]
             ] for i in range(Y.shape[0])
        ]
        n = len(intervals)
        # fit a line
        k, b = self.approximate_curve(X, Y, self.line)
        fitted_line = X * k + b
        # fit a hyperbola
        a, b = self.approximate_curve(X, Y, self.hyperbola)
        fitted_hyperbola = X ** b * a
        #
        plt.boxplot(intervals)
        line, = plt.plot(X,
                         fitted_line,
                         color='blue',
                         label='Approximated line')
        plt.xticks(np.arange(1, n + 1, n // 10),
                   labels=np.arange(0, n, n // 10))
        plt.ylabel(y_label_)
        plt.xlabel(x_label_)
        plt.legend(handles=[line])
        plt.savefig(os.path.join("./results", out_filename + '.jpg'),
                    format='jpg',
                    )
        plt.tight_layout()

    def make_plots_time_by_length(self):
        raise NotImplementedError()

    def make_tables_time_by_many_strings(self):
        raise NotImplementedError()

    def make_plots_memory_by_length(self):
        raise NotImplementedError()

    @staticmethod
    def approximate_curve(X, Y, func):
        popt, popv = curve_fit(func, X, Y, maxfev=100)
        return popt[0], popt[1]

    @staticmethod
    def line(x, k, b):
        y = k * x + b
        return y

    @staticmethod
    def hyperbola(x, a, b):
        y = x ** b * a
        return y
