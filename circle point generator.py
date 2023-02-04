import random
import math
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


def generate1():
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    return a * math.cos(2 * math.pi * b), a * math.sin(2 * math.pi * b)


def generate2():
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return x, y


num = 10
firstCoord = []
secondCoord = []
generate = []


for i in range(num):
    if i % 2 == 0:
        xCoord, yCoord = generate1()
        firstCoord.append(xCoord)
        secondCoord.append(yCoord)
        generate.append(1)
    else:
        xCoord, yCoord = generate2()
        firstCoord.append(xCoord)
        secondCoord.append(yCoord)
        generate.append(2)
print(firstCoord, secondCoord)


feature = pd.DataFrame({"x": firstCoord, "y": secondCoord})

X_train, X_test, y_train, y_test = train_test_split(feature, generate, test_size=0.2)

lr = LogisticRegression()
knn = KNeighborsClassifier()
clf = knn.fit(X_train, y_train)
score = clf.score(X_test, y_test)
print(score)









