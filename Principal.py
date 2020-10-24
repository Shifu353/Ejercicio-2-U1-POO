from ManejadorViajero import ListaViajero
if __name__ == "__main__":
    lista = ListaViajero()
    lista.LeerArchivo()

    def op1 ():
        lista.Item1(numero)
    def op2 ():
        millas = int(input("Ingrese la cantidad de millas a acumular: "))
        lista.item2(numero,millas)
    def op3 ():
        canjear = int(input("Ingrese cantidad de millas a Canjear: "))
        lista.Item3(numero,canjear)
    def op4 ():
        input("Presione una tecla....")
    opcion = None

    diccionario = {1:op1,2:op2,3:op3,4:op4}
    numero = int(input("Ingrese Numero del viajero Finalice con -1: "))
    #print(lista.getLongitud())
    while int(numero) > int(lista.getLongitud() and int(numero) != -1):
        while opcion != 4:
            print("|--------------------------------------|")
            print("| Ingrese 1 para Consultar Cant Millas |")
            print("| Ingrese 2 para Acumular Millas       |")
            print("| Ingrese 3 para Canjear Millas        |")
            print("| Ingrese 4 para Salir                 |")
            print("|--------------------------------------|")
            opcion = int(input("Ingrese Opcion: "))
            
            op=diccionario.get(opcion,lambda: print("Usted Ingreso una Opcion Incorrecta"))

            op()
        numero = int(input("Ingrese Numero del viajero: "))
