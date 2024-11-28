
# SE IMPORTA LA LIBRERIA "sqlite3" PARA EL MANEJO DE LA BASE DE DATOS.

import sqlite3


# FUNCION QUE SERA USADA EN EL INDEX.

def eliminar_gastos():
    try:

        # CONEXION CON LA BASE DE DATOS.

        with sqlite3.connect("C:/Users/POWER/gastos_control.db") as gastos_eliminar:

            # SE CREA UN CURSOR PARA MANEJAR LA BASE DE DATOS.

            consulta_cursor = gastos_eliminar.cursor()

            # ENTRADAS DE USUARIO QUE PIDE EL GASTO Y EL NOMBRE DEK USUARIO PARA ELIMINAR REGISTRO.

            gasto_eliminar = str(input("Ingresa el gasto a eliminar: "))
            nombre_usuario = str(input("Ingresa el nombre de registro: "))
            apellido_usuario = str(input("Ingresa el apellido del usuario registrado: "))

            # CONSULTA SQL PARA IDENTIFICAR EL ID DEL USUARIO Y CON ESTE SU NOMBRE Y APELLIDO.

            consulta_cursor.execute("SELECT usuario_ID FROM usuario WHERE nombre_usuario = ? AND apellido_usuario = ?",(nombre_usuario,apellido_usuario))

            # CON EL METODO "fetchone" SE BUSCA EL REGISTRO DE LA CLAVE.

            usuario = consulta_cursor.fetchone()


            if usuario:

                #  RASTREAR AL CLIENTE EN LA BASE DE DATOS

                usuario_id = usuario[0]
            else:
                print("Usuario no encontrado.")

            # CONSULTA SQL PARA ELIMINAR EL GASTO DEL USUARIO Y SU NOMBRE.

            consulta_cursor.execute("DELETE FROM gastos WHERE gasto_usuario = ? AND usuario_ID = ?",(gasto_eliminar,usuario_id))

            # SE SUBEN LOS CAMBIOS A LA BASE DE DATOD.

            gastos_eliminar.commit()
            print("Gasto eliminado.")
    
    # MANWJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a intentar.")
    except sqlite3.Error as error:
        print(f"{error}")