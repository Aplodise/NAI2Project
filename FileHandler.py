
from Iris import Iris
def open_file(fileName):
    list = []
    with open(fileName, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(',')
            parts[-1] = parts[-1].rstrip('\n')
            match parts[-1]:
                case "Iris-setosa":
                    parts[-1] = 1
                case 'Iris-versicolor':
                    parts[-1] = 0
                case 'Iris-virginica':
                    parts[-1] = 0
                case _:
                    parts[-1] = 0

            iris = Iris(float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3]), int(parts[4]))
            list.append(iris)
    return list