def suma_lista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista[0]+suma_lista(lista[1:])

def main():
    I =[1,2,3,4]
    print(suma_lista(I))
main()
