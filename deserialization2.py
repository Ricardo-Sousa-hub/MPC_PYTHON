import pickle


class NewClass:
    def __init__(self, data):
        print(data)
        self.data = data
        self.x = 0

    def setX(self, x):
        self.x = x;


reconstructed = pickle.load(open('./files/outputser2', 'rb'))
print("Data from reconstructed object:", reconstructed.data, reconstructed.x)
reconstructed.setX(2)
print("Data from reconstructed object:", reconstructed.data, reconstructed.x)
