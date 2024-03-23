
class Iris:
    def __init__(self,sepal_length, sepal_width, petal_length, petal_width, class_index):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.class_index = class_index

    def __str__(self):
        return (f"sepal_length: {self.sepal_length} sepal_width: "
                f"{self.sepal_width} petal_length: {self.petal_length} "
                f"petal_width: {self.petal_width} class_index: {self.class_index}")

    def __repr__(self):
        return self.__str__()