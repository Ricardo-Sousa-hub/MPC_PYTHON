# A test object
import pickle

f = open("./files/demo2.txt", "r",encoding='utf8')
x=f.read()

# Serialization
with open("./files/outputser1.pickle", "wb") as outfile:
    pickle.dump(x, outfile)
print("Written object outputser1")