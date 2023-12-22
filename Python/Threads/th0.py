import threading
import time


def multiplos(nome,x):
    for i in range(0,21):
        z=nome+str(i*x)+"\n"
        print(z)
    z="\nA thread "+ nome + "terminou\n";
    print(z)

x1 = threading.Thread(target=multiplos, args=("th1 ",2))
x2 = threading.Thread(target=multiplos, args=("th2 ",3))
x3 = threading.Thread(target=multiplos, args=("th3 ",5))
x4 = threading.Thread(target=multiplos, args=("th4 ",7))
x1.start()
x2.start()
x3.start()
x4.start()
print("fim")