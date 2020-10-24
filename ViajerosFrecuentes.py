class ViajerosFree ():
    __Numero = 0
    __Dni = ""
    __nombre = ""
    __apellido = ""
    __millas = 0

    def __init__ (self, num, dni, nom, ape, millas):
        self.__Numero = num
        self.__Dni = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__millas = millas
    
    def getNumero (self):
        return self.__Numero
    def getMillas (self):
        return self.__millas
    def setMillas (self,millas):
        #print("Tipó de Milla al llegar a la clase ",type(millas))
        self.__millas += millas
    def CanjearMillas (self, cantidad):
        self.__millas -= cantidad
