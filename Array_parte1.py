# Array

"""""
Métodos del Array

Array() -> Método constructor
get_lenght() -> tamaño
get_item(index) -> obtener el elemento en la posición index
set_item(index, valor) -> ingresa un valor en la posición index
clearing(valor) -> Inicializa el arreglo con el valor dado
"""""
'''ADT
-Tipo de dato definido por usuario
-tiene una estructura especifica
-Encapsula datos y operaciones
Ventajas ADT
-Reducir errores logicos
-Te permite concentrate en soluciones
-Divide y venceras'''
'''
Array
ADT que almacena datos consecutivos ordenados por indice
Operaciones
Array(tam) --> constructor
get_length() --> Regresa el tamaño del array
set_item(index, valor) --> Ingresa/camiba un valor en la direccion dada 
get_item(index) --> Devuelve el valor en la posicion pedida
clearing(valor) --> Limpia el array y deja un valor establecido en todas las posiciones''' 
class Array:
    def __init__(self, n):
        self.__data = []
        for i in range(n):
            self.__data.append(None)
    
    def to_string(self):
        print(self.__data)
        
    def get_lenght(self):
        return len(self.__data)
    
    def set_item(self, index, value):
        if index>=0 and index <=len(self.__data):
            self.__data[index]=value
        else:
            print("Fuera de rango")
    
    def get_item(self,index):
        if index>=0 and index <=len(self.__data):
            return self.__data[index]
        else:
            print("Fuera de rango")        
    
    def clearing(self,value):
        for i in range(len(self.__data)):
            self.__data[i]=value
    
def main():
    arreglo = Array(10)
    arreglo.to_string()
    print(f"El tamaño del arreglo es de {arreglo.get_lenght()}")
    arreglo.set_item(1,10)
    arreglo.to_string()
    print(f"La posición 1 es = {arreglo.get_item()}")
    arreglo.clearing(73)
    arreglo.to_string()
    
main()
