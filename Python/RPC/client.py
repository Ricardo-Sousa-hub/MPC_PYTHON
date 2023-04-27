import xmlrpc.client
import random;

s = xmlrpc.client.ServerProxy('http://localhost:8000')
#x= int(input("entre o 1-valor: "))
#y=int(input("entre o 2-valor: "))
#print(type(x))
#print(s.pow(x%150,y%10))  # Returns 2**3 = 8
#print(s.add(x,y))  # Returns 5
#print(s.sub(x,y)) # x - y
#print(s.mul(x,y))  # Returns 5*2 = 10
#print(s.ia())
#tabuada = s.tabuada(x)
#print(tabuada)
#print(s.somatorio(3))
print(s.complex_sum(2, 3, 4, 1))
print(s.complex_mul(2,3, 4,1))
print(s.complex_pot(2,3,5))
print(s.zeta(2, 3, 4))
print(s.zeta(2, 3, 4))
# Print list of available methods
#print(s.system.listMethods())