import pandas as pd

df_wine = pd.read_csv(
'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
header=None)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

import numpy as np

cov_mat = np.cov(X_train_std.T)
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)

tot = sum(eigen_vals)
var_exp = [(i/tot) for i in sorted(eigen_vals, reverse=True)]

cump_var_exp = np.cumsum(var_exp)

import matplotlib.pyplot as plt
# plt.bar(range(1, 14), var_exp, alpha=0.5, align="center", label="individual explained variance")
# plt.step(range(1, 14), cump_var_exp, where="mid", label="cumlative explained variance")

# plt.ylabel('Explained variance ratio')
# plt.xlabel('Principal components')
# plt.legend(loc="best")
# plt.show()

eign_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:, i]) for i in range(len(eigen_vals))]
eign_pairs.sort(reverse=True)

w = np.hstack((eign_pairs[0][1][:, np.newaxis], eign_pairs[1][1][:, np.newaxis]))
print("Matrix W:\n", w)


print("---")
X_train_pca = X_train_std.dot(w)

colors = ['r', 'b', 'g']
markers = ['s', 'x', 'o']

for l, c, m in zip(np.unique(y_train), colors, markers):
  plt.scatter(X_train_pca[y_train==l, 0], X_train_pca[y_train==l, 1], c=c, label=l, marker=m)

plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.show()