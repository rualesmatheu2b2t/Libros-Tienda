from Libro import Libro
from Transferencia import Transferencia
class TiendaLibrios:
    
    def __init__(self): 
        self.__caja = 1000000
        self.__catalogo = []
        self.__transferencias = []
    def buscarLibroIsbn(self, isbn):
        buscado = None
        for libro in self.__catalogo: 
            if Libro.getIsbn() == isbn:
                buscado = libro 
                break 
        return buscado
        
    def buscarLibroTitulo(self, titulo):
        buscado = None 
        for libro in self.__catalogo:
            if Libro.getTitulo == titulo:
                buscado = libro
                break 
        return buscado

    def registrarLibros(self, titulo, isbn, precioVenta, PrecioCompra, cantidad, rutaImagen): 
        buscar = self.buscarLibroIsbn(isbn)
        nuevo = None 
        if buscar is None:
            nuevo = Libro(titulo, isbn, precioVenta, PrecioCompra, cantidad, rutaImagen)
            self.__catalogo.append(nuevo)
        return nuevo
    
    def EliminarLibro(self, isbn): 
        buscar = self.buscarLibroIsbn(isbn)
        eliminado = False
        if buscar: 
            if buscar.getCantidadActual() == 0:
                self.__catalogo.remove(buscar)
                eliminado = True 
        return eliminado
    def nuevaTransferencia(self, pTipo, cantidad, fecha):
        nTansferencia = Transferencia(pTipo, cantidad, fecha)
        self.__transferencias.append(nTansferencia)
    
    def VenderLibro(self,isbn,cantidadVender,): 
        buscar = self.buscarLibroIsbn(isbn)
        cantidadLibros = buscar.getCantidad()
        precio = 0
        nCantidad = 0
        if buscar:
            if cantidadVender <= cantidadLibros:
                nCantidad = cantidadLibros - cantidadVender
                buscar.setCantidadActual(nCantidad)
                precio = buscar.getPrecioVenta() * cantidadVender
                self.nuevaTransferencia(cantidad = precio, pTipo = 'venta')
                self.__caja += precio
        return precio
    
    def busacarLibroMasCostoso(self):
        venta = 0
        for i in range(len(self.__catalogo)):
            if self.__catalogo[i].precioVenta > venta:
                venta = self.__catalogo[i].precioVenta
                