
# SE IMPORTA LA LIBRERIA "sqlite3" PARA EL MANEJO DE LA BASE DE DATOS.

import sqlite3


#  FUNCION QUE SERA USADA EN EL INDEX.

def ingreso_usuario():
    try:

        # CONEXION CON LA BASE DE DATOS.

        with sqlite3.connect("C:/Users/POWER/gastos_control.db") as nuevo_usuario:

            # SE CREA UN CURSOR PARA MANEJAR LA BASE DE DATOS.

            consulta_cursor = nuevo_usuario.cursor()

            # INGRESO DE USUARIO PARA INGRESAR SU NOMBRE Y APELLIDO.

            usuario_nuevo = str(input("Ingresa tu nombre: "))
            apellido_usuario = str(input("Ingresa tu apellido: "))

            # CONSULTA SQL QUE INGRESA EL NOMBRE Y APELLIDO A LA BASE DE DATOS.

            consulta_cursor.execute("INSERT INTO usuario (nombre_usuario, apellido_usuario) VALUES (?,?)",(usuario_nuevo,apellido_usuario))

            # SE SUBEN LOS CAMBIOS A LA BASE DE DATOS.

            nuevo_usuario.commit()

            # MENSAJE DE EXITO.

            print("Ingreso exitoso.")

    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a ingresar.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")
    
