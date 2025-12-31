import sqlite3

conexion = sqlite3.connect("base1")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

cursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'DEPORTES')")

conexion.commit()

conexion.close()