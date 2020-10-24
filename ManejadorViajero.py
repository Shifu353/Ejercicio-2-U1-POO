class ListaViajero ():
    __lista = None
    
    def __init__ (self):
        self.__lista = []

    def LeerArchivo (self):
        import csv
        from ViajerosFrecuentes import ViajerosFree

        archivo = open("viajero.csv")
        leer = csv.reader(archivo, delimiter=";")

        for viajero in leer:
            self.__lista.append(ViajerosFree(int(viajero[0]),viajero[1],viajero[2],viajero[3],int(viajero[4])))
        archivo.close()

    def getLongitud (self):
        return len(self.__lista)

    def BuscarViajero (self, numero):
        i = 0
        while(i<len(self.__lista) and int(self.__lista[i].getNumero()) != int(numero)):
            #print(self.__lista[i].getNumero())
            i += 1
        if(i<len(self.__lista)):
            return i
        return -1

    def Item1 (self, numViajero):
        posicion = self.BuscarViajero(numViajero)
        #print(posicion)
        if posicion != -1:
            print("La cantidad de Millas es de {}".format(self.__lista[posicion].getMillas()))
        else:
            print("No se encontro Numero de Viajero")
    
    def item2 (self,num, cant):
        posicion = self.BuscarViajero(num)
        if posicion != -1:
            #print(type(cant))
            self.__lista[posicion].setMillas(cant)
            print("La cantidad nueva de millas es de: {}".format(int(self.__lista[posicion].getMillas())))
        else:
            print("No se encontro numero de viajero")
    
    def Item3 (self, num, cant):
        posicion = self.BuscarViajero(num)
        if posicion != -1:
            if cant <= int(self.__lista[posicion].getMillas()):
                self.__lista[posicion].CanjearMillas(cant)
                print("La cantidad de millas restantes es: {}".format(self.__lista[posicion].getMillas()))
            else:
                print("Error,la cantidad solicitada es mayor que la que tiene el viajero")
        else:
            print("No se encontro numero de viajero")
