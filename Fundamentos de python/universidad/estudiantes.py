import procesamiento_db as modulo

# registrarAlumno(nombre,apellido,carrera,edad)
# listarAlumnos()
# obtenerAlumnoId(id_est)
# actualizarCarreraAlumno(carrera,id_est)
# eliminarAlumno(id_est)

while True:
  print()
  print('='*5+' Estudiantes '+'='*5)
  print('''1. Registrar un alumno
2. Listar Alumnos
3. Buscar un alumno
4. Actualizar carrera de alumno
5. Eliminar un alumno
6. Cerrar sistema''')
  print('='*15)
  opcion = int(input('Elige una opcion (1-6): ').strip())
  print('='*15)
  if opcion==1:
    print('=== Datos de alumno ===')
    nom = input('Nombre: ').strip().capitalize()
    ape = input('Apellido: ').strip().capitalize()
    car = input('Carrera: ').strip().capitalize()
    edad = int(input('Edad: ').strip())
    res = modulo.registrarAlumno(nom,ape,car,edad)
    if res==1:
      print('=== Ups, hubo un error al insertar ===')
    else:
      print('=== Alumno inscrito ==')
  elif opcion==2:
    print('=== Listado de Alumnos ===')
    res = modulo.listarAlumnos()
    print(res)
  elif opcion==3:
    print('=== Buscar un alumno ===')
    est_id = int(input('Id de alumno: ').strip())
    res=modulo.obtenerAlumnoId(est_id)
    if res==1:
      print('=== Ups, hubo un error al buscar ===')
    elif res==():
      print('=== No hay alumno con ese id ===')
    else:
      print(res)
  elif opcion==4:
    print('=== Actualizar carrera de alumno ===')
    est_id = int(input('Id de alumno: ').strip())
    res=modulo.obtenerAlumnoId(est_id)
    if res==1:
      print('=== Ups, hubo un error al buscar ===')
    elif res==():
      print('=== No hay alumno con ese id ===')
    else:
      carr = input('Ingresa nueva carrera: ').strip().capitalize()
      res = modulo.actualizarCarreraAlumno(carr,est_id)
      if res==1:
        print('=== Ups, hubo un error al actualizar ===')
      else:
        print('=== Carrera cambiada ===')
  elif opcion==5:
    print('=== Eliminar alumno ===')
    est_id = int(input('Id de alumno: ').strip())
    res=modulo.obtenerAlumnoId(est_id)
    if res==1:
      print('=== Ups, Intentalo nuevamente ===')
    elif res==():
      print('=== No hay alumno con ese id ===')
    else:
      res = modulo.eliminarAlumno(est_id)
      if res==1:
        print('=== Ups, hubo un error al eliminar ===')
      else:
        print('=== Alumno eliminado ===')
  elif opcion==6:
    print('=== Sistema cerrado ===')
    break
  else:
    print('=== Error, intentalo nuevamente ===')