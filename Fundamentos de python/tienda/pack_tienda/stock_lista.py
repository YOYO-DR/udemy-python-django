# from pelicula import Pelicula
# from libro import Libro

# p=Pelicula()
# l=Libro()

# p.agregarPelicula("Tarzan", "1:25:03", 15)
# p.agregarPelicula("Bourne", "1:35:03", 3)
# p.agregarPelicula("El Hobit", "1:40:00", 20)
# p.agregarPelicula("Rambo", "1:43:00", 6)
# l.agregarLibro("Matematica I", 120, 13)
# l.agregarLibro("Matematica II", 100, 21)
# l.agregarLibro("Matematica III", 90, 26)
# l.agregarLibro("Matematica IV", 95, 14)

def listarStock(numeroStock,obj_p,obj_l):
    lista_productos = []
    nueva_lista=[]

    for pel in obj_p.listarPeliculas():
        lista_productos.append(pel)

    for lib in obj_l.listarLibros():
        lista_productos.append(lib)
    
    for producto in lista_productos:
        if numeroStock >= producto['stock']:
            nueva_lista.append(producto)
    
    return nueva_lista

# print(listarStock(6))