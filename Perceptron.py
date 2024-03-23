import FileHandler
from Iris import Iris
list = FileHandler.open_file("files/iris-train.txt")
test_data = FileHandler.open_file("files/iris-test.txt")

w0 = [0,0,0,0,0]
nn = 0.01



def classification_func(data):
    predict = (w0[0] * data.sepal_length +
           w0[1] * data.sepal_width +
           w0[2] * data.petal_length +
           w0[3] * data.petal_width +
           w0[4] * data.class_index)
    return 1 if predict >= 0 else 0

def modification(data, predicted, actual):
    error = actual - predicted
    w0[0] += w0[0] + error * nn * data.sepal_length
    w0[1] += w0[1] + error * nn * data.sepal_width
    w0[2] += w0[2] + error * nn * data.petal_length
    w0[3] += w0[3] + error * nn * data.petal_width
    w0[4] += w0[4] + error * nn * data.class_index

def train_data():
    for data in list:
        predicted = classification_func(data)
        modification(data, predicted, data.class_index)
        print(data.class_index)


def test_data(test_data):
    correct_predictions = 0
    total_predictions = 0
    for data in test_data:
        predicted = classification_func(data)
        if predicted == data.class_index:
            correct_predictions += 1
        total_predictions += 1

    accuracy = correct_predictions / total_predictions * 100
    print("Dokładność:", accuracy, "%")
