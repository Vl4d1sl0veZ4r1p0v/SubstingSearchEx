import os
import datetime
from copy import deepcopy

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

    def make_tables_time_by_many_strings(
            self,
            runing_times: np.array,
            occurences: list,
            substrings_lengths: list,
            algorithms: list,
    ):
        headers = ['<b>Substring length, letters</b>',
                   '<b>Amount of occurrences</b>']
        headers.extend(['<b>' + algorithm + '</b>'
                        for algorithm in algorithms])
        values = [
            substrings_lengths,
            occurences,
        ]
        values.extend(runing_times)
        self.make_table_by_many_strings(
            headers=headers,
            occurences=occurences,
            substrings_lengths=substrings_lengths,
            out_filename=os.path.join(
                "results",
                "time_" + str(datetime.datetime.now()) + '.png'
            ),
            values=values,
        )

    def make_tables_memory_by_many_strings(
            self,
            memory_usage: np.array,
            occurences: list,
            substrings_lengths: list,
            algorithms: list,
    ):
        headers = ['<b>Substring length, letters</b>',
                   '<b>Amount of occurrences</b>']
        headers.extend(['<b>' + algorithm + '</b>'
                        for algorithm in algorithms])
        values = [
            substrings_lengths,
            occurences,
        ]
        values.extend(memory_usage)
        self.make_table_by_many_strings(
            headers=headers,
            occurences=occurences,
            substrings_lengths=substrings_lengths,
            out_filename=os.path.join(
                "results",
                "memory_" + str(datetime.datetime.now()) + '.png'
            ),
            values=values,
        )

    @staticmethod
    def make_table_by_many_strings(values: list,
                                   headers: list,
                                   occurences: list,
                                   substrings_lengths: list,
                                   out_filename: str):
        n = len(occurences)
        header_color = 'blue'
        row_even_color = 'lightskyblue'
        row_odd_color = 'white'
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=headers,
                line_color='darkslategray',
                fill_color=header_color,
                align='center',
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=values,
                line_color='darkslategray',
                fill_color=[
                    [
                        [row_even_color, row_odd_color][i % 2]
                        for i in range(n)
                    ] * 3
                ],
                align='left',
                font=dict(color='black', size=13)
            ))
        ])
        fig.update_layout(width=1800, height=600)
        fig.write_image(out_filename)
        #fig.show()

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

    def make_plot_memory_by_length(
            self,
            memory_usages: np.array,
            x_label_="Length of input text, letters",
            y_label_="Used memory, MiB",
            out_filename="memory" + str(datetime.datetime.now())
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

    def complete_statistic(self, config: dict):
        """Нужна, когда хотим подвести статистику по нескольким алгоритмам:
         несколько результатов на одном графике или общая сводная таблица."""
        experiment_dir = config.get("out_dirname", None)
        if not experiment_dir:
            experiment_dir = os.path.join(
                "results",
                str(datetime.datetime.now())
            )
        if not os.path.isdir(experiment_dir):
            os.makedirs(experiment_dir)
        config['out_filename'] = experiment_dir
        self.make_plots_time_by_length(config)
        self.make_plots_memory_by_length(config)

    def make_plots_time_by_length(self, config):
        new_config = deepcopy(config)
        new_config['y_label_'] = "Time of working, seconds"
        new_config['out_filename'] = os.path.join(
            config["out_filename"],
            "time_" + str(datetime.datetime.now())
        )
        new_config['usages'] = config['usages']['running_times']
        self.make_plots_by_length(new_config)

    def make_plots_memory_by_length(self, config):
        new_config = deepcopy(config)
        new_config['y_label_'] = "Used memory, MiB"
        new_config['out_filename'] = os.path.join(
            config["out_filename"],
            "memory_" + str(datetime.datetime.now())
        )
        new_config['usages'] = config['usages']['memory_usage']
        self.make_plots_by_length(new_config)

    def make_plots_by_length(self, config):
        usages = config['usages']
        algorithms_names = config['algorithms_names']
        x_label_ = config['x_label_']
        y_label_ = config['y_label_']
        out_filename = config['out_filename']
        fig, ax = plt.subplots(figsize=(9, 6))
        lines_for_legend = []
        for i in range(len(usages)):
            print(algorithms_names[i])
            means, stds = self.get_prepared_for_plotting(usages[i])
            X = np.arange(1, usages[i].shape[0] + 1)
            Y = means
            # Delete outliers
            #
            n = usages[i].shape[0]
            # fit a line
            k, b = self.approximate_curve(X, Y, self.line)
            fitted_line = X * k + b
            plt.scatter(X, Y, alpha=0.5)
            line, = plt.plot(X,
                             fitted_line,
                             label=algorithms_names[i])
            lines_for_legend.append(line)
        plt.xticks(np.arange(1, n + 1, n // 10),
                   labels=np.arange(0, n, n // 10))
        plt.ylabel(y_label_)
        plt.xlabel(x_label_)
        plt.legend(handles=lines_for_legend)
        plt.savefig(out_filename, format='jpg', )
        plt.tight_layout()

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
