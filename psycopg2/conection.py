"""
Recuerda cuando estes creando una conection recuerda no escribir la escritura mal como por escribir port escribir post y asi

RECUERDA EL FETCHALL SE LE PONE ALA FUNCION 
ASI

CONEXIO.EXECUTE(quiry)
CONEXIO.FETCHALL
-

"""

import psycopg2

# Parámetros de conexión
host = "localhost"  # Cambia esto si estás usando un servidor remoto
port = "5432"       # El puerto por defecto de PostgreSQL es 5432
dbname = "nombre_de_tu_base_de_datos"
user = "tu_usuario"
password = "tu_contraseña"

# Establecer la conexión
try:
    conexion = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    print("Conexión exitosa")
except psycopg2.Error as e:
    print(f"Error al conectar a PostgreSQL: {e}")

# No olvides cerrar la conexión cuando hayas terminado
finally:
    if conexion:
        conexion.close()
        print("Conexión cerrada")
