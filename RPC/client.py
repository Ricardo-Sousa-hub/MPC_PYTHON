import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
x= int(input("entre o 1-valor: "))
y=int(input("entre o 2-valor: "))
print(type(x))
print(s.pow(x%150,y%10))  # Returns 2**3 = 8
print(s.add(x,y))  # Returns 5
print(s.mul(x,y))  # Returns 5*2 = 10
print(s.ia())
lista = s.tabuada(x)
for i in range(len(lista)):
    print(lista[i])
# Print list of available methods
print(s.system.listMethods())