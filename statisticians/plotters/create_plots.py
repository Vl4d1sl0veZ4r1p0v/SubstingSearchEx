# import matplotlib.pyplot as plt
# import numpy as np
# from data_loaders import data_best
#
# n = 10
# pattern = 'adsfasdf'
# testing_data = data_best.generate(n)
#
#
# mean_acc = np.zeros((n - 1))
# std_acc = np.zeros((n - 1))
# for i in range(1, n):
#     mean_acc[i - 1] =
#     std_acc[i - 1] = np.std(yhat == y_test) / np.sqrt(yhat.shape[0])
#
# plt.plot(range(1,Ks),mean_acc,'g')
# plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
# plt.legend(('Accuracy ', '+/- 3xstd'))
# plt.ylabel('Accuracy ')
# plt.xlabel('Number of Nabors (K)')
# plt.tight_layout()
# plt.show()