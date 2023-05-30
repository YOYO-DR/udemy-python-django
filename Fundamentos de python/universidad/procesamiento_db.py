import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv('./.env')
def conexionDB():
  mi_db=mysql.connector.connect(
      host=os.environ.get('DBHOST'),
      user=os.environ.get('DBUSER'),
      password=os.environ.get('DBPASS'),
      database='universidad'
  )

  return mi_db

def registrarAlumno(nombre,apellido,carrera,edad):
  mi_db=conexionDB()
  mi_cursor=mi_db.cursor()

  sql = '''INSERT INTO estudiantes
            (nombre, apellido, carrera, edad)
            VALUES (%s,%s,%s,%s)'''
  valores = (nombre,apellido,carrera,edad)
  try:
    mi_cursor.execute(sql, valores)
  except:
    mi_db.rollback() # si sale un error con ese insert entonces hace que no tenga efecto
    retorno = 1
  else:
    mi_db.commit()
    retorno = 0
  finally:
    mi_db.close()
  return retorno

# res=registrarAlumno('Carlos','Rojas','Programación',23)
# print(res)

def listarAlumnos():
  mi_db = conexionDB()
  mi_cursor = mi_db.cursor()
  sql = '''SELECT nombre, apellido, carrera, edad FROM estudiantes'''
  try:
    mi_cursor.execute(sql)
  except:
    mi_db.rollback()
    retorno = 1
  else:
    retorno = []
    for alumno in mi_cursor:
      retorno.append(alumno)
  finally:
    mi_db.close()
    return retorno

# res=listarAlumnos()
# print(res)

def obtenerAlumnoId(id_est):
  mi_db=conexionDB()
  mi_cursor=mi_db.cursor()

  sql = ''' SELECT nombre, apellido,carrera, edad 
  FROM estudiantes
  WHERE estudiante_id=%s '''
  valores = (id_est,)
  try:
    mi_cursor.execute(sql, valores)
  except:
    mi_db.rollback()
    retorno = 1
  else:
    retorno = ()
    for alumno in mi_cursor:
      retorno = alumno
  finally:
    mi_db.close()
    return retorno
  
# res=obtenerAlumnoId(1)
# print(res)

def actualizarCarreraAlumno(carrera,id_est):
  mi_db = conexionDB()
  mi_cursor=mi_db.cursor()
  sql = '''UPDATE estudiantes 
            SET carrera=%s 
            WHERE estudiante_id=%s'''
  valores = (carrera,id_est)
  try:
    mi_cursor.execute(sql,valores)
  except:
    mi_db.rollback()
    retorno = 1
  else:
    mi_db.commit()
    retorno = 0
  finally:
    mi_db.close()
    return retorno

# res=actualizarCarreraAlumno('Desarrollo web',1)
# print(res)

def eliminarAlumno(id_est):
  mi_db = conexionDB()
  mi_cursor=mi_db.cursor()
  sql = '''DELETE FROM estudiantes 
            WHERE estudiante_id=%s'''
  valores = (id_est,)
  try:
    mi_cursor.execute(sql,valores)
  except:
    mi_db.rollback()
    retorno = 1
  else:
    mi_db.commit()
    retorno = 0
  finally:
    mi_db.close()
    return retorno

# res = eliminarAlumno(2)
# print(res)