try:# probar
    archivo = open('Fundamentos de python\excepcion\prueba.txt') 
except Exception as err: # si hay un error
    print(f'Error al abrir archivo ({err})')
else: #si no hay errores
    print('Archivo abierto, continua...')
    archivo.close()
finally: # siempre se ejecuta
    print('Procediminento final, nos vemos...')