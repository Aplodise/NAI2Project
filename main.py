import FileHandler
from Perceptron import Perceptron
from Iris import Iris
print("PERCEPTRON V1")

url = input("Podaj ścieżkę do pliku treningowego ")
train_data = FileHandler.open_file(url)
learning_rate = float(input("Podaj stałą uczącą "))
perceptron = Perceptron(learning_rate)
perceptron.train_data(train_data)

while True:
    print("Menu perceptrona:")
    print("1. Wprowadź wektor")
    print("2. Wgrać plik z danymi testowymi")

    choice = input("Wybierz opcję: ")

    match choice:
        case "1":
            try:
                sepal_length = float(input("Enter sepal length: "))
                sepal_width = float(input("Podaj szerokość działki kielicha: "))
                petal_length = float(input("Podaj długość płatka: "))
                petal_width = float(input("Podaj szerokość płatka: "))
                class_index = input("Podaj nazwę irysu: ")

                iris = Iris(sepal_length, sepal_width, petal_length, petal_width, class_index)
                perceptron.test_one_entry(iris)
            except ValueError:
                print("Błąd: Wprowadzone dane nie są liczbami.")
            break

        case "2":
            choice = input("Podaj ścieżkę do pliku testowego ")
            list = FileHandler.open_file(choice)
            perceptron.test_data(list)
            break
        case "3":
            print("Wychodzę z programu")
            break
        case _:
            print("Błąd: Nieprawidłowy wybór. Wybierz opcję 1, 2 lub 3.")