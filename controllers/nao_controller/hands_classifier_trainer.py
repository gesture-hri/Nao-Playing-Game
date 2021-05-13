from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier

import numpy as np
import pickle
import json

TEST_SIZE = 0.25
RANDOM_STATE = 42

config = json.load(open("cfg.json"))

paper = np.load(config["paper_path"])
rock = np.load(config["rock_path"])
scissors = np.load(config["scissors_path"])

X = np.concatenate((rock, paper, scissors), axis=0)
y = np.concatenate(
    (np.full(len(rock), 0), np.full(len(paper), 1), np.full(len(scissors), 2)), axis=0
)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
print("INFO: logistic regression test set accuracy: " + str(model.score(X_test, y_test)))

with open(config["logistic_regression_path"], "w+b") as f:
    pickle.dump(model, f)

model = SGDClassifier(max_iter=500)
model.fit(X_train, y_train)
print("INFO: sgd classifier test set accuracy: " + str(model.score(X_test, y_test)))

with open(config["sgd_classifier_path"], "w+b") as f:
    pickle.dump(model, f)

model = KNeighborsClassifier()
model.fit(X_train, y_train)
print("INFO: knn classifier test set accuracy: " + str(model.score(X_test, y_test)))

with open(config["knn_classifier_path"], "w+b") as f:
    pickle.dump(model, f)

