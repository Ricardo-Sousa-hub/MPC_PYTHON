from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name
    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    def sub_function(x, y):
        return x - y
    server.register_function(sub_function,'sub')


    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    class MyFuncs:
        def mul(self, x, y):
            return x * y

        def ia(self):
            return "Inteligencia Artifical"

        def tabuada(self, x):
            frase = ""
            for i in range(11):
                frase = frase + f"{i} * {x} = {x*i}\n"
            return frase

        def somatorio(self, x):
            resultado = 0.0
            for i in range(1,x+1):
                resultado = resultado + (i ** 3)
            return resultado

        def complex_sum(self, a1, a2, b1,b2):
            return f'z1 + z2 = {a1 + a2}+i{b1+b2}'

        def complex_mul(self, a1, a2, b1, b2):
            return f'z1 * z2 = {(a1*a2)-(b1*b2)} + i{(a2*b1)+(a1*b2)}'

        #TODO
        def zeta_4(self,a, b):
            resultado = 0
            c = complex(f'{b}j')
            y = 1
            for i in range(0, 4):
                resultado = resultado + (1/(y**(a+c)))
                y = y + 1
            return str(resultado).replace('(','').replace(')','')

        def zeta(self,a, b, n):
            resultado = 0
            c = complex(f'{b}j')
            y = 1
            for i in range(0, n):
                resultado = resultado + (1/(y**(a+c)))
                y = y + 1
            return str(resultado).replace('(','').replace(')','')


        def complex_pot(self, a1, b1, x):
            complex_string = str(a1) + str('+') + str(b1) + str('j')
            complex_number = complex(complex_string)
            resultado = complex_number**x
            return str(resultado).replace('(', '').replace(')','')

    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()

