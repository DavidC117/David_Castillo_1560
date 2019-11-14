#Arboles parte 2 (parte 1 en el cuaderno)

'''
Arboles binarios
Es aquel arbol que esta vacio o cuenta con una raiz con subarboles que contienen
nodos con 0, 1 o maximo 2 hijos, los cuales se conocen hijo izquierdo e hijo derecho.
Ejemplos:
------
Para implementar un arbol binario en Python se utiliza el siguiente Nodo:
class NodoArbol:
    def __init__ (self, value, izquierdo = None, derecho =  None):
        self.data = value
        self.left = izquierdo
        self.right = derecho

    def main():
        root = NodoArbol('A',NodoArbol(B),NodoArbol(C))
'''
class NodoArbol:
    def __init__ (self, value, izquierdo = None, derecho =  None):
        self.data = value
        self.left = izquierdo
        self.right = derecho


'''
Arbol Binario de Busqueda
Es aquel arbol binario que tiene un orden especifico, al tener los nodos balanceados
y con una regla de insercion muy simple. La logica de ordenamiento esta basada:
-En que dado un nodo, todos los nodos del subarbol izquierdo son de valor menor al nodo
y el subarbol de lado derecho contiene valores mayores al nodo. Esto permite que la busqueda de
informacion sea rapida.

Considere el siguiente numero de datos a insertar en un arbol binario de busqueda:
60,29,73,81,40,5
'''

class ArbolBinarioBusqueda:
    def __init__(self):
        self.__root = None

    def insert ( self, value):
        if self.__root == None:
            self.__root = NodoArbol(value)
        else:
            self.__inserta_nodo( self.__root, value)

    def __inserta_nodo (self, nodo, value):
        if nodo == None:
            return False
        elif value < nodo.data:
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            else:
                return self.__inserta_nodo(nodo.left, value)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                return self.__inserta_nodo(nodo.right, value)

    def transversal (self, formato='inorden'):
        if formato == 'inorden':
            self.__inorden (self.__root)
        elif formato == 'preorden':
            self.__preorden (self.__root)
        elif formato == 'posorden':
            self.__posorden (self.__root)

    def __inorden ( self, nodo ):
        if nodo != None:
            self.__inorden(nodo.left)
            print(nodo.data)
            self.__inorden(nodo.right)

    def __preorden ( self, nodo ):
        if nodo != None:
            print(nodo.data)
            self.__preorden(nodo.left)
            self.__preorden(nodo.right)

    def __posorden ( self, nodo ):
        if nodo != None:
            self.__inorden(nodo.left)
            self.__inorden(nodo.right)
            print(nodo.data)

    def search ( self, value):
        if self.__root == None:
            return False # Arbol vacio
        else:
            return self.__search_nodo(self.__root,value)

    def __search_nodo (self, nodo, value):
        if nodo == None:
            return False
        elif nodo.data == value:
            print("Encontrado")
            return nodo
        elif value < nodo.data:
            print("busca izquierda")
            return self.__search_nodo (nodo.left,value)
        elif value > nodo.data:
            print("busca derecha")
            return self.__search_nodo (nodo.right,value)
            
            
        
