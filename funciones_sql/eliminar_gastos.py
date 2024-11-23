import sqlite3


def eliminar_gastos():
    try:
        with sqlite3.connect("C:/Users/POWER/gastos_control.db") as gastos_eliminar:
            consulta_cursor = gastos_eliminar.cursor()
            gasto_eliminar = str(input("Ingresa el gasto a eliminar: "))
            nombre_usuario = str(input("Ingresa el nombre de registro: "))
            apellido_usuario = str(input("Ingresa el apellido del usuario registrado: "))
            consulta_cursor.execute("SELECT usuario_ID FROM usuario WHERE nombre_usuario = ? AND apellido_usuario = ?",(nombre_usuario,apellido_usuario))
            usuario = consulta_cursor.fetchone()
            if usuario:
                usuario_id = usuario[0]
            else:
                print("Usuario no encontrado.")
            consulta_cursor.execute("DELETE FROM gastos WHERE gasto_usuario = ? AND usuario_ID = ?",(gasto_eliminar,usuario_id))
            gastos_eliminar.commit()
            print("Gasto eliminado.")
    except ValueError:
        print("Error de digitacion, volver a intentar.")
    except sqlite3.Error as error:
        print(f"{error}")