import os
from dotenv import load_dotenv
load_dotenv('./.env')
import mysql.connector
# video 6- 8:10
# first_number=1+1
# print(first_number)

# second_number=105+10
# print(second_number)

# total = first_number + second_number
# print(total)

# video 7- 7:34
# print(2+2)
# print(100-20)
# print(100+20-80)
# print(2*2)
# print(2/4)
# print(type(2))
# print(type(0.5))
# print(5%3)

# video 8- 4:36

# order de las operaciones
# p (), o **, d /, m *, a +, s -

# print(2*5-1) # queriamos 8 5-1 luego *2
# print(2*(5-1))

# video 9- Proyecto pocion de salud - parte 1- 9:57
# import random
# salud = 50
# dificultad = 1

# pocionSalud = int(random.randint(25,50) / dificultad)

# # parte 2- 9:55
# salud = salud + pocionSalud
# print(salud)

# video 11 modulo math- 4:44
# print(round(2.1))
# print(round(1.5))
# import math
# print(math.floor(1.5)) # redondea al numero menor (1)
# print(math.ceil(2.1)) # redondea al numero mayor (3)
# print(math.e)
# print(math.pi)
# print(math.pow(2,3)) # es exponente 2**3
# print(2**3)

# video 12 hola mundo - 8:38

# video 13- 12:26

# pedir nombre al usuario
# nombre = input('Cual es tu nombre: ')
# print(nombre)

# #pedir edad al usuario
# edad = input('Cual es tu edad: ')

# #pedir direccion al usuario
# ciudad = input('Cual es tu ciudad: ')

# # pedir hobbie al usuario
# hobbie = input('Cual es tu hobbie: ')

# # video 14 - 10:34
# #crear texto de salida
# salida = f'Tu nombre es {nombre} y tienes {edad} de edad, vives en {ciudad} y te gusta {hobbie}'
# #imprimir texto de salidad en la pantalla
# print(salida)

# video 15- 12:05
# cuantas veces se encuentra una cadena
# texto = 'happy birthday'
# print(texto.count('o'))
# print(texto.lower()) # minuscula
# print(texto.upper()) # mayuscula
# print(texto.capitalize()) # mayuscula la primera letra
# print(texto.title()) # poner cada primera letra en mayuscula
# print(texto.islower()) # si es minuscula
# print(texto.isupper()) # si es mayuscula
# print(texto.istitle()) # preguntar si cada primera letra esta en mayuscula
# print(texto.isalpha()) # si solo tiene letras (no)
# print(texto.isdigit()) #  si tiene solo numeros enteros
# print(texto.isalnum()) # si tiene solo letras o numeros (no cuenta espacios)

# cideo 16- 11:12

# x = 'happy birthday'
# print(x.index('birthday')) # dice donde inicia la cadena buscada, si no la encuentra lanza error
# print(x.find('birthday')) # lo mismo pero si no lo encuentra no lanza error sino un -1 para no alnzar error
# x = '0000000happybirthay00000000'
# print(x.strip('0')) # los elimina de lado y lado, con lstrip, lo quita a la izquiera y con rstrip a la derecha
# # con .strip() solo borra los espacios de mas al final
# # cantidad de caracteres
# print(len(x))

# video 17- 12:48

# palabra = 'programacion'

# print(palabra[0:8:1]) # va desde el indice 0 has el 8 en paso de 1
# print(palabra[0:8:2])# va desde el indice 0 has el 8 en paso de 2
# print(palabra[7:10:1])# va desde el indice 7 has el 10 en paso de 1
# print(palabra[3:])# va desde el indice 3 hasta el final
# print(palabra[3::2])# va desde el indice 3 hasta el final en paso de 2
# print(palabra[:8])# va desde el indice 0 hasta el indice 8
# print(palabra[::-1])# imprime la cadena al revez, al ser -1, sera en paso de 1 pero desde el final hasta el inicio

# video 18- 6:53
# palabra = 'programacion'

# print(palabra[-5]) # viene desde el final hasta el inicio e inicia desde -1

# print(palabra.index('aci')) # asi puedo saber donde inicia la parte que quiero borrar

# print(palabra[palabra.index('aci'):palabra.index('on')]) # corto obeniendo el indice inicial y final

# video 19- 7:33
# cortador de correo

# obtener el email de usuario
# email = input('Cual es tu email?: ').strip()
# #cortar el nombre del usuario
# usuario = email[:email.index('@')] # corta hasta antes del arroba

# # corat el dominio
# dominio = email[email.index('@')+1:] # inicia cortando desde el arroba, entonces le sumamos 1 para obtemer hasta todo lo que sigue del @
# #formatear el mensaje
# salida = f'Tu nombre de usuario es {usuario} y tu nombre de domino es {dominio}'
# # mostrar mensaje de salida
# print(salida)

# video 20- 8:36
# video 21- 11:31
# num1 = 100
# num2 = 150

# if num1 > num2:
#   print('Num1 es mayor que num2')
# elif num2 > num1:
#   print('Num2 es mayor que num1')
# else:
#   print('Ambos son iguales')

# video 22- 7:52

# video 23- 8:57
# c=6
# d=2

# if (c>5 and d>5) or (c>1 and d>1):
#     print('Funciono')


# video 24- 14:57
# nuestraLista = [27,46,-5,17,99]
# # print(type(nuestraLista))
# jackson= ['a','b','c',1,2,3,'do','rey','mi',True,False]
# # print(jackson[7])
# # print(jackson[-2])
# x=jackson[6]
# # print(jackson[:3]) # ira de a hasta c, porque el 1 no lo toma

# nuestra_lista=[1,2,[3,4,5],6,7,8]
# # print(nuestra_lista[2][0])
# # print(nuestra_lista[2][:2])
# nuestraTabla = [[1,2,3],[4,5,6],[7,8,9]]
# print(nuestraTabla[0])
# print(nuestraTabla[1])
# print(nuestraTabla[2])
# print(nuestraTabla[0][2])

# video 25- 9:08
# video 26- 10:36
# video 27- 5:45
# usuariosConocidos = ['Alice','Bob','Claire','Dan','Emma','Fred','Georgie','Harry']
# # print(len(usuariosConocidos))

# l=['a','b','c','d']
# # del l[0] #elimino por posicion
# del l[0:2]# elimina desde el inicio has la posicion 1 (porque el 2 es de referencia, borra hasta antes de ese número)
# print(l)

# while True:
#   print('Hola, mi nombre es Keto')
#   nombre=input('Cual es tu nombre: ').strip().capitalize() # la primerla letra la pongo en mayuscula
# if nombre in usuariosConocidos:
#   print('nombre reconocido')
#   print(f'Hola {nombre}')
#   eliminar = input('Te gustaria ser eliminado del sistema (y/n)?: ').strip()
#   if eliminar == 'y':
#     usuariosConocidos.remove(nombre) # elimino si encuentra el elemento
#   elif eliminar == 'n':
#     print('No hay problema si no deseas salir')
# else:
#   print(f'Hmm no creo haberte conocido aun {nombre}')
#   agregar = input('Te gustaria ser agregado al sistema (y/n)?: ').strip().lower()
#   if agregar == 'y':
#     usuariosConocidos.append(nombre)
#   elif agregar =='n':
#     print('No te preocupes, nos vemos')

# video 28- 12:31
# a= [5,12,72,55,89]
# a=a+[1] # con el + puedo sumarle o agregarle listas
# print(a)
# a=a+list('bcd') # lo convierte a lista por cada elemento
# print(a)
# a=a+[[5,6,7,8]] # asi no le suma la lista, sino que agrega la lista en una posicion
# a.append([8,7,6,5])
# print(a)
# a= [5,12,72,55,89]
# a.insert(2,100) # se agrega en el indice 2, el numero 100
# print(a)
# a.insert(2,[1,2,3,4])
# print(a)
# a= [5,12,72,55,89]
# a[0]='asi' # asigno un valor a esa posicion
# print(a)

# video 29- 8:39
# nuestraTupla = 1,2,3,'a','b','c' # se puede crear asi
# # print(type(nuestraTupla))
# nuestraTupla = (1,2,3,'a','b','c') # pero normalmente es asi
# # print(type(nuestraTupla))
# print(nuestraTupla[0:3])

# nuestraLista=[1,2,3,4,5,6,7]
# nuestraLista[2]=100
# print(nuestraLista)
# # nuestraTupla[2]=1 # no se puede pq es inmutable
# a=[1,2,3]
# a=tuple(a) # asi lo combierto a tupla
# print(type(a))
# (a,b,c) = 1,2,3 # asi puedo definir varias variables
# print(a)
# d,e,f = [1,2,3] # mismo resultado, asi puedo asignar un arreglo a variables

# g,h,i = "ert" # funciona igual

# video 30- 12:14
# estudiantes = {'alice':25,'bob':27,'claire':17,'dan':21,'emma':22}
# # error_estudiantes = {alice:25,bob:27} # debe ser un string si no hay una variable para asignar
# print(estudiantes['dan'])
# #agreagr clave
# estudiantes['fred']=25
# print(estudiantes['fred'])
# #modificar
# estudiantes['alice']=26
# print(estudiantes['alice'])
# del estudiantes['fred']
# # print(estudiantes['fred']) # error
# print(estudiantes.keys()) # imprimo las claves pero no puedo acceder por indice, entonces lo convierto en lista, lo mismo para values()
# a=list(estudiantes.keys())
# print(a[2])

# video 31- 11:17
# estudiantes = {
#     'alice':{'id':'ID0001','edad':26,'grado':'A'},
#     'bob':{'id':'ID0002','edad':27,'grado':'B'},
#     'claire':{'id':'ID0003','edad':17,'grado':'C'},
#     'dan':{'id':'ID0004','edad':21,'grado':'D'},
#     'emma':{'id':'ID0005','edad':22,'grado':'E'}
#     }

# print(estudiantes['dan']['edad'])

# print(estudiantes['emma']['id'], estudiantes['emma']['grado'])

# video 32- 15:00

# peliculas = {
#     'Nemo':[3,5],
#     'Bourne':[18,5],
#     'Tarzan':[15,5],
#     'Spiderman':[12,5]
# }
# while True:
#   eleccion = input('Que pelicula te gustaria ver?: ').strip().title()

#   if eleccion in peliculas:
#     edad = int(input('Cuantos años tienes?: ').strip())

#     if edad >=peliculas[eleccion][0]:
#       numBoletos=peliculas[eleccion][1]
#       if numBoletos >0:
#         print('Disfruta la pelicula')
#         peliculas[eleccion][1]-=1
#       else:
#         print('Perdón, se agotaron los boletos')
#     else:
#       print('Eres demasiado joven para ver esta pelicula')
#   else:
#     print('No tenemos esa pelicula')

# video 31- 13:33
# video 32- 8:04
# from random import choice
# preguntas = [
#   'Porque el cielo es azul?: ',
#   'Porque hay una cara en la luna?: ',
#   'Donde estan los dinosaurios?: '
# ]

# pregunta = choice(preguntas)

# respuesta =  input(pregunta).strip()

# while respuesta != 'porque si':
#   respuesta = input('porque?: ').strip().lower()

# print('Oh entiendo')

# video 35- 10:46
# for numero in range(1,11,2):
#     print(numero)
# vocales = 0
# consonantes = 0
# for letra in 'programacion':
#   if letra.lower() in 'aeiou':
#     vocales += 1
#   elif letra==' ':
#     pass
#   else:
#     consonantes += 1

# print(f'Tenemos {vocales} vocales.')
# print(f'Tenemos {consonantes} consonantes.')

# video 36- 7:12
# estudiantes = {
#   'masculino':['Tom','Charlie','Harry','Frank'],
#   'fememino':['Sarah','Huda','Samantha','Emily','Elizabeth']
# }

# for key in estudiantes.keys():
#   for nombre in estudiantes[key]:
#     if 'a' in nombre:
#       print(nombre)

# video 37- 6:04
# compresion de listas

# num_pares = [x for x in range(1,101) if x %2 ==0]
# # print(num_pares)
# num_impares = [x for x in range(1,101) if x %2 != 0]
# # print(num_impares)

# palabras = ['python','es','un','lenguaje','de','programacion']
# respuesta = [[w.upper(),w.lower(),len(w)] for w in palabras] # creo arreglos dentro de otras listas y con un for
# # print(respuesta)

# video 38- 4:34
# video 39- 16-10

# obtener oracion del usuario
# original = input('Ingresa una oracion: ').strip().lower()
# #dividir en palabras
# palabras = original.split() #por defecto parte en palabras

# #recorrer palabras y convertirlas con el traducto
# nuevasPalabras = []
# for palabra in palabras:
#     if palabra[0] in 'aeiou':
#         nuevaPalabra= palabra + 'yay'
#         nuevasPalabras.append(nuevaPalabra)
#     else:
#         vocal_pos=0
#         for letra in palabra:
#             if letra not in 'aeiou':
#                 vocal_pos+=1
#             else:
#                 break
#         cons=palabra[:vocal_pos] # saco las consonantes antes de la primera vocal
#         elResto=palabra[vocal_pos:] # saco la parte de la palabrra desde la primera vocal hasta el final
#         nuevaPalabra = elResto+cons+'ay' #lo uno
#         nuevasPalabras.append(nuevaPalabra) # lo agrego a la lista
# #unir palabras en una oración
# salida = ' '.join(nuevasPalabras)# entre cada elemento de la lista, pondra un espacio en blanco y lo une en una cadena
# #generar cadena final
# print(salida)

# video 40- 11:33
# def agregar(x,y):
#   return x + y

# res = agregar(100,20)
# # print(res)
# def reves(texto):
#   return texto[::-1] #tambien funciona para arreglos
# palabra = "lapiz"
# print(reves(palabra))
# lista=[1,2,3,4,5]
# print(reves(lista))

# video 41- 9:32
# video 42- 7:53
# variables scope, global y local
# a=250 # es de alcance global entones es visible en todo el programa
# def f1():
#   global a # asi puedo mofidicar esa a de forma global
#   a = 100
#   # b=a+10
#   # a=100 # aqui esta fuera del alcance de f2, es de alcance local
#   print(a)

# def f2():
#   a=50 # global
#   print(a)

# f1()
# f2()
# print(a)# sigue en 250, y no podemos cambiar las variables globales dentro de las funciones
# a= [1,2,3]

# def f1():
#     a[0]=5 # si modifica el valor del arreglo, y aplica lo mismo para dicts
#     print(a)

# def f2():
#     a = 50 # no modifica el arreglo total
#     print(a)

# print(a)
# video 43- 10:05
# argumentos y parametros
# ahi ya le puse un valor predeterminado a gustos por si la persona no ingresa uno
# def sobre(nombre,edad,gustos='python'): #parametros, lo que recibe la funcion
#     oracion = f"Es {nombre} tiene {edad} años de edad y le gusta {gustos}"
#     return oracion

# print(sobre(edad=24, nombre='jack',gustos='futbol')) #argumentos, lo que le paso a la funcion en la llamada
# # puede ser en orden, o en desorden pero diciendole a que parametro pertenece

# print(sobre(edad=24, nombre='jack'))

# video 44- 15:44

# numeros = [1,2,3,4,5]
# # print(numeros)
# # print(*numeros) # recorre el iterable y es como si le pasara (1,2,3,4,5)

# # print(*'abc') # recorre el iterable y es como si le pasara ('a','b','c')

# def agregar(*numeros): # lo que le pase, lo empaquetara en una tupla llamada numeros
#   total = 0
#   for i in numeros:
#     total+=i

#   return total

# # print(agregar(1,2,3,4,5,6,7,8,9)) # es como si se guardara (1,2,3,4,5,6,7,8,9)

# def sobre(nombre, edad, gustos):
#   oracion = f'Es {nombre} tiene {edad} años de edad y le gusta {gustos}'
#   return oracion

# dictionary = {'nombre':'Jack','edad':23,'gustos':'python'}

# # print(sobre(**dictionary))# al ser diccionario lo paso con **, y lo que hace es como que (nombre=tal, edad=32,gustos=tal) utilizando el diccionario
# #es lo mismo que decir
# # print(sobre(nombre='Jack',edad=23,gustos='Python'))


# def mi_funcion(**kwargs): #puede ser cualquier nombre, pero ahi recibe lo de (n=1,t=2,b=5) y lo convierte a diccionario
#   for key,value in kwargs.items():
#     print(f'{key}:{value}')


# mi_funcion(huda='femenino',jack='masculino',john='masculino')

# #* para pasar valores como tupla o listas, y el ** para tipo diccionario, para empaquetar o desempaquetar

# video 45- 10:52
# video 46- 14:21
# tic tac toc

# tablero = ["  " for i in range(9)]

# def print_tablero():
#     fila1 = f'| {tablero[0]} | {tablero[1]} | {tablero[2]} |'
#     fila2 = f'| {tablero[3]} | {tablero[4]} | {tablero[5]} |'
#     fila3 = f'| {tablero[6]} | {tablero[7]} | {tablero[8]} |'

#     print()
#     print(fila1)
#     print(fila2)
#     print(fila3)
#     print()

# def jugador_mov(icono):
#     if icono == 'X':
#         numero = 1
#     elif icono == 'O':
#         numero = 2
#     print(f'Tu tunro jugador {numero}')
#     elecccion = int(input('Ingrese su movimiento (1-9): ').strip())
#     if tablero[elecccion -1] == '  ':
#         tablero[elecccion -1] = icono
#     else:
#         print()
#         print('El espacio esta ocupado')
# def es_victoria(icono):
#     if (tablero[0]==icono and tablero[1]==icono and tablero[2]==icono) or \
#     (tablero[3]==icono and tablero[4]==icono and tablero[5]==icono) or \
#     (tablero[6]==icono and tablero[7]==icono and tablero[8]==icono) or \
#     (tablero[0]==icono and tablero[3]==icono and tablero[6]==icono) or \
#     (tablero[1]==icono and tablero[4]==icono and tablero[7]==icono) or \
#     (tablero[2]==icono and tablero[5]==icono and tablero[8]==icono) or \
#     (tablero[0]==icono and tablero[4]==icono and tablero[8]==icono) or \
#     (tablero[2]==icono and tablero[4]==icono and tablero[6]==icono):
#         return True
#     else:
#         return False

# def es_empate():
#     if '  ' not in tablero:
#         return True
#     else:
#         return False

# while True:
#     print_tablero()
#     jugador_mov('X')
#     print_tablero()
#     if es_victoria('X'):
#         print('X es el ganador')
#         break
#     elif es_empate():
#         print('esto es empate')
#         break
#     jugador_mov('O')
#     if es_victoria('O'):
#         print('X es el ganador')
#         break
#     elif es_empate():
#         print('esto es empate')
#         break

# video 47- 4:53
# video 48- 7:36
# video 49- 16:44
# video 50- 13:05
# video 51- 13:49

# import random
# class Moneda:
#     def __init__(self, raro=False, limpio=True, caras=True, **kwargs):
#         for key, value in kwargs.items():
#             # setattr es para pasarle los atributos del dict, primero el objeto, segundo nombre y tercero su valor
#             setattr(self, key, value)
#         self.es_raro = raro
#         self.es_limpio = limpio
#         self.caras = caras

#         if self.es_raro:
#             self.valor = self.valor_original * 1.25
#         else:
#             self.valor = self.valor_original

#         if self.es_limpio:
#             self.color = self.color_limpio
#         else:
#             self.color = self.color_oxidado
#     def __str__(self):
#         if self.valor_original >=1:
#             return f"Moneda {str(self.valor_original)} Libra"
#         else:
#             return f"Moneda {str(self.valor_original*100)} Penique"

#     # def __del__(self):  # destruye el objeto
#     #     print('Moneda gastada')

#     def oxido(self):
#         self.color = self.color_oxidado

#     def limpiar(self):
#         self.color = self.color_limpio

#     def vueltas(self):
#         caras_opciones = [True, False]
#         eleccion = random.choice(caras_opciones)
#         self.caras = eleccion

# class Un_Penique(Moneda): #hereda
#     def __init__(self):
#         data = {
#             'valor_original': 0.01,
#             'color_limpio': 'bronce',
#             'color_oxidado': 'marron',
#             'num_bordes': 1,
#             'diametro': 20.3,
#             'grosor': 1.52,
#             'peso': 3.56
#         }
#         super().__init__(**data)

# class Dos_Penique(Moneda): #hereda
#     def __init__(self):
#         data = {
#             'valor_original': 0.02,
#             'color_limpio': 'bronce',
#             'color_oxidado': 'marron',
#             'num_bordes': 1,
#             'diametro': 25.9,
#             'grosor': 1.85,
#             'peso': 7.12
#         }
#         super().__init__(**data)

# class Cinco_Penique(Moneda): #hereda
#     def __init__(self):
#         data = {
#             'valor_original': 0.05,
#             'color_limpio': 'plata',
#             'color_oxidado': None,
#             'num_bordes': 1,
#             'diametro': 18.0,
#             'grosor': 1.77,
#             'peso': 3.25
#         }
#         super().__init__(**data)

#     def oxido(self): # como el plata no se puede oxidar y aqui llamo el metodo y lo sobreescribo pero solo para esta clase
#         self.color = self.color_limpio

# class Libra(Moneda): #hereda
#     def __init__(self):
#         data = {
#             'valor_original': 1.00,
#             'color_limpio': 'dorado',
#             'color_oxidado': 'verdoso',
#             'num_bordes': 1,
#             'diametro': 22.5,
#             'grosor': 3.15,
#             'peso': 9.5
#         }
#         #con super hago referencia a la clase super, y pues le paso los datos desde aqui del init al init del padre para que cree los atributos para esta moneda por el data
#         super().__init__(**data)  # desempaquetamos por el argumento

# monedas=[Libra(),Un_Penique(),Dos_Penique(),Cinco_Penique()]

# for moneda in monedas:
#   argumentos = [moneda,moneda.color,moneda.valor,moneda.diametro,moneda.grosor,moneda.num_bordes,moneda.peso]
#   cadena = "{} - Color: {}, Valor: {}, diametro(mm): {}, grosor(mm): {}, bordes: {}, peso: {}".format(*argumentos) # utilizo para desempaquetar y que se pongan ahi en los {} en el orden del arreglo
#   print(cadena)

#   #video 52- 15:02

# class Cuenta:
#     def __ini__(self,nombre,balance,balance_min):
#       self.nombre = nombre
#       self.balance = balance
#       self.balance_min = balance_min
    
#     def deposito(self,monto):
#        self.balance += monto

#     def retiro(self,monto):
#       if self.balance - monto >= self.balance_min:
#           self.balance -= monto
#       else:
#          print('Lo siento, no hay dinero')
    
#     def declaracion(self):
#        print(f'Balance de la cuenta {self.balance}')


# class Corriente(Cuenta):
#   def __init__(self,nombre,balance):
#       super().__init__(nombre,balance,balance_minimo = -1000)
  
#   def __str__(self):
#      return f'Cuenta de {self.nombre} - Balance de {self.balance}'


# class Ahorro(Cuenta):
#   def __init__(self,nombre,balance):
#       super().__init__(nombre,balance,balance_minimo = 0)
  
#   def __str__(self):
#      return f'Cuenta de {self.nombre} - Balance de {self.balance}'

# z = Corriente('Juan',500)
# t = Ahorro('Tom',300)

#video 53- 7:48
# ruta = 'D:/programacion/Python/Udemy/Python/La Ruta de Python - Django Fullstack Developer/Fundamentos de python/datos.txt'
# archivo=open(ruta,'r') #,encoding='UTF-8' asi modifico el codigo si quiero
# #mirar ruta
# print(archivo.encoding)
# print(archivo.name)
# # print(archivo)
# # print(archivo.mode) # mirar el modo,r para leer, w para sobreescribir todo el numero, a para escribir al final
# # print(archivo.closed) #verificar si ya se cerro el archivo
# archivo.close() # cerrar el archivo
# # print(archivo.closed) #verificar si ya se cerro el archivo

#video 54- 8:00
# ruta = 'D:/programacion/Python/Udemy/Python/La Ruta de Python - Django Fullstack Developer/Fundamentos de python/datos.txt'
# archivo=open(ruta,'r')

# registro = archivo.readline() #devuelve la primera linea + el salto de linea
# registro = archivo.readlines() # mete en un arreglo cada valor de las lineas
# #al ser arreglo, puedo acceder a cada linea como acceder a un arreglo
# # registro = archivo.read() #devuelve todo los datos
# # si pongo un readline y luego otro, no me va a poner el mismo dato o linea, sino que continua en la linea
# # print(registro[2])
# registro1 = archivo.readline()
# registro2 = archivo.readline()
# archivo.seek(0) # le digo a que linea volver
# registros = archivo.readlines()
# print(registro1)
# print(registro2)
# print(registros)
# #imprime lo 2 primeros, y al ultimo lo lee desde ahi

# siempre cerrar el archivo
# archivo.close()

#video 55- 11:40

# ruta1 = 'D:/programacion/Python/Udemy/Python/La Ruta de Python - Django Fullstack Developer/Fundamentos de python/datos.txt'

# ruta2 = 'D:/programacion/Python/Udemy/Python/La Ruta de Python - Django Fullstack Developer/Fundamentos de python/datos_esc.txt'

# archivo_lec=open(ruta1,'r')
# # archivo_esc = open(ruta2,'w') #voy a escribir
# # archivo_esc = open(ruta2,'a') # agrega al final los textos
# archivo_esc = open(ruta2,'r+') # significa que sera de lectura y escritura a la vez, pero como el modo a

# # registros = archivo_lec.read()#leo ese archivo
# # archivo_esc.write(registros)
# # archivo_esc.write('Yoiner') # sobreescribe todo, porque esta en modo w
# # archivo_esc.write('\nYuri') # lo agrega, ys i no le pongo el salto de linea lo va a poner enseguida de lo que haya
# # archivo_esc.write('''
# # Yoiner
# # Perez
# # Daniel
# # Aleja
# # Danna''') # asi lee los saltos de linea 
# archivo_esc.seek(0,2)# le digo que 2 para que pongo el cursor al final y escribir ahi
# archivo_esc.write('Yoiner')

# archivo_lec.close()
# archivo_esc.close()

# video 56- 10:37
# ruta = 'D:/programacion/Python/Udemy/Python/La Ruta de Python - Django Fullstack Developer/Fundamentos de python/datos_1.txt'

# archivo=open(ruta,'w')

# print(archivo.readline())
# archivo.write('Maria')

# archivo.close() # si no cierro, no guarda nada

# with open(ruta,'r') as archivo1:
#   with open(ruta,'a') as archivo2:
#     #asi puedo leer con r y modificar con w
#     registros = archivo1.read()
#     print(registros)

#video 57- 20:09
# ruta = 'D:/programacion/Python/Udemy/Python/La Ruta de Python - Django Fullstack Developer/Fundamentos de python/personas.txt'

# def agregar(nombre,edad,genero):
#     with open(ruta,'a') as archivo:
#         fila=f'{nombre},{edad},{genero}\n'
#         archivo.write(fila)
#         print('-'*5+'Persona agregada'+'-'*5)

# # agregar('aleja',19,'F')

# def lista():
#     with open(ruta,'r') as archivo:
#         print('-'*5+'Lista'+'-'*5)
#         print(archivo.read())
#         print('-'*15)

# # lista()

# def listarGenero(letraGenero):
#     with open(ruta,'r') as archivos:
#         # print(archivos.readlines())
#         archivos.seek(0,0) #reiniciar cursor para que lea al inicio porque el readlines dejo el cursor al final
#         for archivo in archivos:
#             archivo=archivo.strip('\n') #quitar el salto de linea
#             nombre,edad,genero = archivo.split(',')

#             if letraGenero.lower()==genero.lower():
#                 print(archivo)

# # listarGenero('m')
# while True:
#     print('---Elige una opcion---')
#     print('1 - Agregar una persona')
#     print('2 - Listar personas')
#     print('3 - Listar personas por genero')
#     print('4 - Cerrar registro')

#     opcion = input('¿Que quieres hacer? (1-4): ').strip()
#     if int(opcion) ==1:
#         nom = input('Tu nombre: ').strip().capitalize()
#         ed = input('Tu edad: ').strip()
#         gen = input('Tu genero: ').strip().upper()
#         agregar(nom,ed,gen)
#     elif int(opcion) == 2:
#         lista()
#     elif int(opcion) == 3:
#         gen = input('Ingresa el genero: ').strip().upper()
#         listarGenero(gen)
#     elif int(opcion) == 4:
#         break
#     else:
#         print('opcion invalida')

# video 58- 2:18
# video 59- 7:55
# video 60- 11:22
# video 61- 5:58
# video 62- 18:36
# video 63- 17:42
# video 64- 11:08
# video 65- 5:15

# def funcion_principal(funcion_parametro):
#     print('Dentro de funcion principal')
#     def funcion_ejecutar(nom):
#         print('Dentro de funcion_ejecutar')
#         return funcion_parametro(nom)
#     # funcion_ejecutar()
#     #se puede retornar
#     return funcion_ejecutar

# def saludo(nombre):
#     print('Hola',nombre)

# def pregunta(nombre):
#     print(f'Como estas {nombre}?')
# # saludo()
# # s=saludo # asi puedo asignar una funcion a una variable (objecto funtion)
# # s()

# respuesta = funcion_principal(pregunta) # se lo paso sin los ()
# respuesta('Juan')

# video 66- 10:53

# def decorador(funcion_parametro):
#     def funcion_ejecutar(a,b):
#         a=int(a)
#         b=int(b)
#         return funcion_parametro(a,b)
#     return funcion_ejecutar
# @decorador
# def suma(a,b):
#     c = a + b
#     return c

# @decorador
# def resta(a,b):
#     c=a-b
#     return c

# res=suma(2,5)
# # es como si fuera esto
# # obj_funcion=decorador(resta) # se utiliza para los modulos
# # resultado = obj_funcion(4,5)
# # print(resultado)
# print(res)

# video 67- 14:22
# video 68- 10:39
# video 69- 4:10
# video 70- 11:03

# a = input('Ingresa un valor de a: ')
# b = input('Ingresa un valor de b: ')

# try:
#   resultado = int(a)/int(b)
#   print(resultado)
# except ValueError:
#   print('a o b no son numericos')
# except ZeroDivisionError:
#   print('Lo siento, no puedes dividir por cero')
# except Exception as error: # este debe ir de ultimo
#   print(type(error)) # ver que tipo de error es
#   print(f'Lo siento, hubo un error ({error})')

# print('Fuera del bloque try-ecxept')

# video 71- 5:44
# video 72- 7:14
# video 73- 9:06
# video 74- 12:28
# import mysql.connector

# mi_db=mysql.connector.connect(
#     host=os.environ.get('DBHOST'),
#     user=os.environ.get('DBUSER'),
#     password=os.environ.get('DBPASS')
# )

# mi_cursor=mi_db.cursor()
# # sql = 'CREATE DATABASE ecommerce'
# # mi_cursor.execute(sql)

# # sql = 'DROP DATABASE ecommerce'
# # mi_cursor.execute(sql)

# sql = 'SHOW DATABASES'
# mi_cursor.execute(sql)
# for item in mi_cursor:
#     print(item)

# mi_db.close()

# video 75- 8:59

# mi_db=mysql.connector.connect(
#     host=os.environ.get('DBHOST'),
#     user=os.environ.get('DBUSER'),
#     password=os.environ.get('DBPASS'),
#     database='ecommerce'
# )

# mi_cursor=mi_db.cursor()
# sql = '''CREATE TABLE cliente (
#             nombre VARCHAR(255),
#             apellido VARCHAR(255)
# )'''
# mi_cursor.execute(sql)

# # sql = 'DROP TABLE IF EXISTS cliente'
# # mi_cursor.execute(sql)


# mi_cursor.execute('SHOW TABLES')
# for tabla in mi_cursor:
#     print(tabla)

# mi_db.close()
# video 76- 7:12
# mi_db=mysql.connector.connect(
#     host=os.environ.get('DBHOST'),
#     user=os.environ.get('DBUSER'),
#     password=os.environ.get('DBPASS'),
#     database='ecommerce'
# )

# mi_cursor=mi_db.cursor()

# sql='''ALTER TABLE 
#         cliente ADD cliente_id INT AUTO_INCREMENT PRIMARY KEY'''
# mi_cursor.execute(sql)

# mi_cursor.execute('DESCRIBE cliente')
# for columnas in mi_cursor:
#     print(columnas)

# mi_db.close()

# video 77- 7:50
# mi_db=mysql.connector.connect(
#     host=os.environ.get('DBHOST'),
#     user=os.environ.get('DBUSER'),
#     password=os.environ.get('DBPASS'),
#     database='ecommerce'
# )

# mi_cursor=mi_db.cursor()

# #sql = '''INSERT INTO cliente
# #          (nombre,apellido)
# #          VALUES ('Maria','Paredes')'''
# #mi_cursor.execute(sql)

# mi_cursor.execute('SELECT * FROM cliente')
# for reg in mi_cursor:
#     print(reg)

# # mi_db.commit() # para que se apliquen los cambios antes de cerrar la conexión
# mi_db.close()

# video 78- 8:11
# mi_db=mysql.connector.connect(
#     host=os.environ.get('DBHOST'),
#     user=os.environ.get('DBUSER'),
#     password=os.environ.get('DBPASS'),
#     database='ecommerce'
# )

# mi_cursor=mi_db.cursor()

# sql = '''INSERT INTO cliente
#             (nombre, apellido)
#             VALUES (%s, %s)'''

# # valores = ('Mercedes','Rojas')
# # mi_cursor.execute(sql, valores)

# valores = [('Carlos','Parco'),
#            ('Kyle','Smith'),
#            ('Anderson','Salazar')]
# mi_cursor.executemany(sql, valores)
# mi_db.commit()

# mi_cursor.execute('SELECT * FROM cliente')
# for cliente in mi_cursor:
#     print(cliente)

# mi_db.close()

# video 79- 8:13
# mi_db=mysql.connector.connect(
#     host=os.environ.get('DBHOST'),
#     user=os.environ.get('DBUSER'),
#     password=os.environ.get('DBPASS'),
#     database='ecommerce'
# )

# mi_cursor=mi_db.cursor()

# # sql = ''' SELECT nombre,apellido FROM cliente '''
# # sql = ''' SELECT nombre,apellido FROM cliente 
#           # WHERE nombre='Maria' '''
# sql = ''' SELECT nombre,apellido FROM cliente 
#           WHERE nombre=%s '''

# mi_cursor.execute(sql,('Pedro',))
# for reg in mi_cursor:
#     print(reg)

# mi_db.close()

# video 80- 9:03
# delete
# mi_db=mysql.connector.connect(
#     host=os.environ.get('DBHOST'),
#     user=os.environ.get('DBUSER'),
#     password=os.environ.get('DBPASS'),
#     database='ecommerce'
# )
# mi_cursor=mi_db.cursor()

# sql = '''DELETE FROM cliente 
#           WHERE nombre = %s '''
# valores = ('Carlos',)
# mi_cursor.execute(sql,valores)
# mi_db.commit()

# mi_cursor.execute('SELECT * FROM cliente')
# for reg in mi_cursor:
#     print(reg)

# mi_db.close()

# update
# mi_db=mysql.connector.connect(
#     host=os.environ.get('DBHOST'),
#     user=os.environ.get('DBUSER'),
#     password=os.environ.get('DBPASS'),
#     database='ecommerce'
# )
# mi_cursor=mi_db.cursor()

# sql = '''UPDATE cliente 
#           SET nombre = %s 
#           WHERE nombre = %s'''

# valores=('Juan','Anderson')
# mi_cursor.execute(sql,valores)
# mi_db.commit()

# mi_cursor.execute('SELECT * FROM cliente')
# for reg in mi_cursor:
#     print(reg)

# mi_db.close()

# video 81- 13:53
# video 82- 16:47
