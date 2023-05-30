from pack_tienda.libro import Libro
from pack_tienda.pelicula import Pelicula
from pack_tienda.stock_lista import listarStock # como este tiene importado pelicula y liro, no hay necesidad de importar aqui libro y pelicula

print('-'*5+'Bienvenido Admin'+'-'*5)
while True:
  print()
  print('''1. Agregar una pelicula
2. Listar Peliculas
3. Agregar un Libro
4. Listar Libros
5. Ver productos con poco stock
6. Salir''')
  opcion = input('Que quieres hacer? (1-6): ').strip()
  print()
  p=Pelicula()
  l=Libro()
  if int(opcion)==1:
    print('----Datos de la pelicula---')
    nom=input('Nombre de la pelicula: ').strip().capitalize()
    dur=input('Duracion: ').strip()
    stock=int(input('Stock: ').strip())
    p.agregarPelicula(nom,dur,stock)
  elif int(opcion)==2:
    lista = p.listarPeliculas()
    print(lista)
  elif int(opcion)==3:
    print('----Datos del libro---')
    nom=input('Nombre del libro: ').strip().capitalize()
    hojas=int(input('Hojas: ').strip())
    stock=int(input('Stock: ').strip())
    l.agregarLibro(nom,hojas,stock)
  elif int(opcion)==4:
    lista = l.listarLibros()
    print(lista)
  elif int(opcion)==5:
    stock = int(input('Cantidad a evaluar: ').strip())
    lista = listarStock(stock,p,l)
    print(f'---Productos con stock menor que {stock}---')
    print(lista)
  elif int(opcion)==6:
    break
  else:
    print('Opcio invalida')
