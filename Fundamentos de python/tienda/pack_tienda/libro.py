libros = []

class Libro:
    def __init__(self,nombre='',hojas='',stock=0):
        self.nombre = nombre
        self.hojas = hojas
        self.stock = stock
    
    def agregarLibro(self,nombre,hojas,stock):
        self.nombre = nombre
        self.hojas = hojas
        self.stock = stock

        libros.append({'libro':nombre,
                        'hojas':hojas,
                        'stock':stock})
    
    def listarLibros(self):
        return libros


# l = Libro()
# l.agregarLibro('Matenaticas I',100, 23)
# l.agregarLibro('Programación',87,12)

# print(l.listarLibros())