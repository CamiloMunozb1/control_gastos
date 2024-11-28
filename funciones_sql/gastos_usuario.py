
# SE IMPORTA LA LIBRERIA "sqlite3" PARA EL MANEJO DE LA BASE DE DATOS. 

import sqlite3


#  FUNCION QUE SERA USADA EN EL INDEX.

def gastos_ingresados():
    try:

        # CONEXION CON LA BASE DE DATOS.

        with sqlite3.connect("C:/Users/POWER/gastos_control.db") as ingresar_gastos:

            # SE CREA UN CURSOR PARA MANEJAR LA BASE DE DATOS.

            consulta_cursor = ingresar_gastos.cursor()

            # ENTRADAS DE USUARIO PARA INGRESAR EL GASTO E IDENTIFICAR AL USUARIO.

            ingresar_gasto = str(input("Ingresa el gasto: "))
            nombre_usuario = str(input("Ingresa tu nombre de registro: "))
            apellido_usuario = str(input("Ingresa tu apellido de registro: "))

            # CONSULTA SQL PARA IDENTIFICAR EL ID DEL USUARIO Y CON ESTE SU NOMBRE Y APELLIDO.

            consulta_cursor.execute("SELECT usuario_ID FROM usuario WHERE nombre_usuario = ? AND apellido_usuario = ? ",(nombre_usuario, apellido_usuario))

            # CON EL METODO "fetchone" SE BUSCA EL REGISTRO DE LA CLAVE.

            usuario = consulta_cursor.fetchone()

            if usuario:

                #  RASTREAR AL CLIENTE EN LA BASE DE DATOS.

                usuario_id = usuario[0]
            else:
                print("Usuario no encontrado.")

            # CONSULTA SQL PARA INGRESAR EL GASTO DEL USUARIO Y SU NOMBRE

            consulta_cursor.execute("INSERT INTO gastos (gasto_usuario, usuario_ID) VALUES (?,?)",(ingresar_gasto, usuario_id))

            # SE SUBEN LOS CAMBIOS A LA BASE DE DATOS.

            ingresar_gastos.commit()

            # MESNAJE DE EXITO.

            print("Gasto ingresado.")

    # MANEJO DE ERROES.
    
    except ValueError:
        print("Error de digitacion, volver a intentar.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")