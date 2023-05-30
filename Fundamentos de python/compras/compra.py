# de esta forma, como las funciones de las compras van a trabajar, con un archivo, no necesito poner eso en cada funcion, creo el decorador, el cual recibe la funcion, y y dentro, creo la funcion que va a recibir los parametros cuando la invoque, y ya dentro le paso el archivo ejecutando la funcion y pasandole los kwargs o diccionario empaquetado, y ya ahi retorno la ejecucion de esa funcion, y asi nomas cuando llame la funcion agregar solo le paso la data, y el decorador le pone el archivo que necesita
ruta = 'Fundamentos de python\compras\compra.txt'

def archivo(funcion_parametro):
    def funcion_ejecutar(**kwargs):
        with open(ruta,"a+") as ar:
            return funcion_parametro(ar,**kwargs) # el kwargs tambien hacer de que no no haym solo le pasa el ar normal
    return funcion_ejecutar

@archivo
def agregarCompra(obj_ar,**kwargs):
    nom = kwargs['nom_producto']
    cant = kwargs['cant']
    prec_unit = kwargs['prec_unit']
    total = kwargs['cant'] * kwargs['prec_unit']
    fila = f'{nom},{cant},{prec_unit},{total}\n'
    obj_ar.write(fila)

# data ={'nom_producto':'Cepillo','cant':2,'prec_unit':4}
# agregarCompra(**data)

@archivo
def listarProductos(obj_ar):
    obj_ar.seek(0,0) #para que se ponga al inicios
    print(obj_ar.read())

# listarProductos()

@archivo
def obtenerProductos(obj_ar):
    obj_ar.seek(0,0)
    return obj_ar.readlines()

# resultado=obtenerProductos()
# print(resultado)

def totalVentas():
    total=0
    for producto in obtenerProductos():
        producto=producto.strip('\n') # le quito el \n
        totalProducto=producto.split(',')[3] # separo por comas
        total+=int(totalProducto)
    print(f'El total de ventas del dia es: {total}')

# totalVentas()

def totalProductosVendidos():
    totalCantidad=0
    for producto in obtenerProductos():
        producto=producto.strip('\n') # le quito el \n
        cantidadProducto=producto.split(',')[1] # separo por comas
        totalCantidad+=int(cantidadProducto)
    print(f'Se vendieron {totalCantidad} productos')

totalProductosVendidos()
