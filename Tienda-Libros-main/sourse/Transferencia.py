class Transferencia:

    TIPO = {
        'venta':'venta',
        'abastecimiento':'abastecimiento' 

    }
    def __init__(self, pTipo, cantidad, fecha):
        self.__tipo = self.TIPO.venta if pTipo == 'venta' else self.TIPO.abastecimiento
        self.__catidad = cantidad
        self.__fecha =  fecha

    def getTipo(self):
        return self.__tipo
    
    def getCantida(self):
        return self.__catidad
    
    def getFecha(self):
        return self.__fecha