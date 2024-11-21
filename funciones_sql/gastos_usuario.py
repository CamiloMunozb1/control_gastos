import sqlite3

def gastos_ingresados():
    try:
        with sqlite3.connect("C:/Users/POWER/gastos_control.db") as ingresar_gatos:
            consulta_cursor = ingresar_gatos.cursor()
            ingresar_gastos = str(input("Ingresa el gasto: "))
            nombre_usuario = str(input("Ingresa tu nombre y apellido de registro: "))
            consulta_cursor.execute("SELECT usuario_ID FROM gastos WHERE nombre_usuario,apellido_usuario = ? ,?",(nombre_usuario,))
            usuario = consulta_cursor.fetchone()
            if usuario:
                usuario_id = usuario[0]
            else:
                print("Usuario no encontrado.")
            consulta_cursor.execute("INSERT INTO gastos (gasto_usuario, usuario_ID) VALUES (?,?)",(ingresar_gastos, usuario_id))
            ingresar_gastos.commit()
            print("Gasto ingresado.")
    except ValueError:
        print("Error de digitacion, volver a intentar.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")