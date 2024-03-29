import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from cancer_data import CancerData
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

data = CancerData()

pipe_lr = Pipeline([('scl', StandardScaler()), 
                    ('clf', LogisticRegression(penalty='l2', C=0.5, random_state=0))])

train_sizes, train_scores, test_scores = learning_curve(estimator=pipe_lr,
                                                        X=data.X_train,
                                                        y=data.y_train,
                                                        train_sizes=np.linspace(0.1, 1.0, 10),
                                                        cv=10,
                                                        n_jobs=1)

train_mean = np.mean(train_scores, axis = 1)
train_std = np.std(train_scores, axis = 1)

test_mean = np.mean(test_scores, axis = 1)
test_std = np.std(test_scores, axis = 1)

plt.plot(train_sizes, train_mean, color='blue', marker='o', 
         markersize=5, label='traing accuracy')

plt.fill_between(train_sizes, 
                 train_mean + train_std,
                 train_mean - train_std,
                 alpha = 0.15, color='blue')

plt.plot(train_sizes, test_mean, color='green', linestyle='--', 
         marker='s', markersize=5, label='validation accracy')

plt.fill_between(train_sizes, 
                 test_mean + test_std,
                 test_mean - test_std,
                 alpha = 0.15, color='green')

plt.grid()
plt.xlabel('Number of training samples')
plt.ylabel('Accracy')
plt.legend(loc='lower right')
plt.ylim([0.8, 1.0])
plt.show()