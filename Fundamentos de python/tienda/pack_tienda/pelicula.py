peliculas = []

class Pelicula:
    def __init__(self,nombre='',duracion='',stock=0):
        self.nombre = nombre
        self.duracion = duracion
        self.stock = stock
    
    def agregarPelicula(self,nombre,duracion,stock):
        self.nombre = nombre
        self.duracion = duracion
        self.stock = stock

        peliculas.append({'pelicula':nombre,
                          'duracion':duracion,
                          'stock':stock})
    
    def listarPeliculas(self):
        return peliculas


# p = Pelicula()
# p.agregarPelicula('Tarzan','1:35:00', 21)
# p.agregarPelicula('Rambo','1:32:00',12)

# print(p.listarPeliculas())