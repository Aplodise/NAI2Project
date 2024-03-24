import FileHandler
from Iris import Iris
list = FileHandler.open_file("files/iris-train.txt")
test_data = FileHandler.open_file("files/iris-test.txt")
import random
class Perceptron:

    def __init__(self, learning_rate):
        self.weights = []
        for i in range(4):
            self.weights.append(random.uniform(-1,1))
        self.threshold = random.uniform(-1,1)
        self.learning_rate = learning_rate

    def classification_func(self, iris):
        weighted_sum = 0
        predicted_result = 0
        weighted_sum += iris.sepal_length * self.weights[0]
        weighted_sum += iris.sepal_width * self.weights[1]
        weighted_sum += iris.petal_length * self.weights[2]
        weighted_sum += iris.petal_width * self.weights[3]

        predicted_result += weighted_sum >= self.threshold
        return predicted_result


    def modification(self, data, predicted):
        iris_list = []
        iris_list.append(data.sepal_length)
        iris_list.append(data.sepal_width)
        iris_list.append(data.petal_length)
        iris_list.append(data.petal_width)
        iris_list.append(data.class_index)
        for i in range(4):
            iris_list[i] *= self.learning_rate * (iris_list[4] - predicted)
            self.weights[i] += iris_list[i]
        self.threshold += (iris_list[4] - predicted) * self.learning_rate * (-1)




    def train_data(self, train_data):
        for i in range(10):
            for iris in train_data:
                predicted_result = self.classification_func(iris)
                self.modification(iris, predicted_result)


    def test_data(self, test_data):
        correct_predictions = 0
        total_predictions = 0
        for iris in test_data:
            predicted_result = self.classification_func(iris)
            if predicted_result == iris.class_index:
                correct_predictions += 1
            total_predictions += 1

        accuracy = correct_predictions / total_predictions * 100
        print("Dokładność:", accuracy, "%")

    def test_one_entry(self, iris):
        predicted_result = self.classification_func(iris)
        match predicted_result:
            case 1:
                print("Predicted as: Iris-setosa")
            case 0:
                print("Predicted as: Iris-versicolor or Iris-virginica")


