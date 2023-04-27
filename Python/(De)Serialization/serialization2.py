import pickle


class NewClass:
    def __init__(self, data):
        print(data)
        self.data = data
        self.x = 0

    def setX(self, x):
        self.x = x


# Create an object of NewClass
new_class = NewClass(1)
new_class.x = 10
# Serialize o objecto new_class
outfile = open("files/outputser2", "wb")
pickle.dump(new_class, outfile)
