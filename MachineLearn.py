import pandas

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy
import tkinter
from tkinter import *

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
# names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
names = ['FF', 'KG', 'GOW', 'class']
dataset = pandas.read_csv('ML.csv', names=names)
# dataset = pandas.read_csv(url, names=names)

array = dataset.values

X = array[:, 0:2]
# X = array[:, 0:4]
Y = array[:, 2]
# Y = array[:, 4]

# print(X)
# print(Y)
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)

scoring = 'accuracy'

# Spot Check Algorithms

models = [('LR', LogisticRegression(solver='liblinear', multi_class='ovr')), ('LDA', LinearDiscriminantAnalysis()),
          ('KNN', KNeighborsClassifier()), ('CART', DecisionTreeClassifier()), ('NB', GaussianNB()),
          ('SVM', SVC(gamma='auto'))]

# evaluate each model in turn
results = []
names = []

for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# print("X Train and Validation ")
# print(X_train)
# print(X_validation)


# print(accuracy_score(['Iris-versicolor'], predictions))
# print(confusion_matrix(['Iris-versicolor'], predictions))
# print(classification_report(['Iris-versicolor'], predictions))
# dataset.hist()
# plt.show()


window = tkinter.Tk()
window.title("PyBot")
# lbl = Label(window, text="Hello")


lbl = Label(window, text="Hello User, Enter for classification", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)


# 'sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'

lbl = Label(window, text="sepal-length", font=("Arial Bold", 10))
lbl.grid(row=1, column=0)
e1 = Entry(window)
e1.grid(row=1, column=1)

lbl = Label(window, text="sepal-width", font=("Arial Bold", 10))
lbl.grid(row=2, column=0)
e2 = Entry(window)
e2.grid(row=2, column=1)

# lbl = Label(window, text="petal-length", font=("Arial Bold", 10))
# lbl.grid(row=3, column=0)
# e3 = Entry(window)
# e3.grid(row=3, column=1)


# lbl = Label(window, text="petal-width", font=("Arial Bold", 10))
# lbl.grid(row=4, column=0)
# e4 = Entry(window)
# e4.grid(row=4, column=1)


T = Text(window, height=2, width=30)
T.grid(row=9, column=1)


def clicked():
    lbl.configure(text="Button was clicked !!")


def predictInput():
    # Make predictions on validation dataset
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)

    lda = LinearDiscriminantAnalysis()
    lda.fit(X_train, Y_train)

    lr = LogisticRegression()
    lr.fit(X_train, Y_train)

    cart = DecisionTreeClassifier()
    cart.fit(X_train, Y_train)

    nb = GaussianNB()
    nb.fit(X_train, Y_train)

    svc = SVC()
    svc.fit(X_train, Y_train)

    val = e1.get()
    val1 = e2.get()
    # val2 = e3.get()
    # val3 = e4.get()

    arr = (float(val), float(val1))
    print(arr)
    # predictions = knn.predict([[5.6, 3.0, 4.5, 1.5]])
    predictions = knn.predict([arr])
    predictionlda = lda.predict([arr])
    predictionlr = lr.predict([arr])
    predictioncart = cart.predict([arr])
    predictionnb = nb.predict([arr])
    predictionsvc = svc.predict([arr])
    print(predictionlr)
    print(predictionlda)
    print(predictions)
    print(predictioncart)
    print(predictionnb)
    print(predictionsvc)
    T.config(state=NORMAL)
    T.insert(END, predictionlda)
    T.insert(END, predictionlr)
    T.insert(END, predictions)
    T.insert(END, predictioncart)
    T.insert(END, predictionnb)
    T.insert(END, predictionsvc)
    T.config(state=DISABLED)

    print(accuracy_score(['GOW'], predictions))
    # print(confusion_matrix(['GOW'], predictions))
    # print(classification_report(['GOW'], predictions))


btn = Button(window, text="Submit", command=predictInput)
btn.grid(column=1, row=7)

window.geometry('600x150')

window.mainloop()
