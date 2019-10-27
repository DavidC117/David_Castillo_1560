from Prueba_list import Linked_List

def main():
    lista=Linked_List()
    print(f"Esta vacia?:{lista.is_empty()}")
    lista.append(10)
    lista.append(20)
    lista.append(30)
    lista.append(40)
    lista.append(50)
    lista.transversal()
    print(lista.get_tail().data)
    lista.prepend(5)
    lista.remove(10)
    lista.transversal()
    lista.transversal()
    lista.add_after(15,35)
    lista.add_after(50,51)
    lista.transversal()
    lista.add_before(5,2)
    lista.transversal()
    lista.add_before(8,1)
    lista.transversal()

    
main()
