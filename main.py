from Iris import Iris
import Perceptron
import FileHandler
Perceptron.train_data()
while True:
    print("Menu:")
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
                class_index = float(input("Podaj indeks klasy: "))

                iris = Iris(sepal_length, sepal_width, petal_length, petal_width, class_index)

                predicted_class = Perceptron.classification_func(iris)
                print("Przewidziana klasa:", predicted_class)
            except ValueError:
                print("Błąd: Wprowadzone dane nie są liczbami.")
            break

        case "2":
            print()
            choice = input("Wpisz ścieżkę do pliku ")
            list = FileHandler.open_file(choice)
            Perceptron.test_data(list)
            break
        case "3":
            print("Wychodzę z programu")
            break
        case _:
            print("Błąd: Nieprawidłowy wybór. Wybierz opcję 1, 2 lub 3.")