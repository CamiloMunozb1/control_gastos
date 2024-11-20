import sqlite3

def ingreso_usuario():
    try:
        with sqlite3.connect("C:/Users/POWER/gastos_control.db") as nuevo_usuario:
            consulta_cursor = nuevo_usuario.cursor()
            usuario_nuevo = str(input("Ingresa tu nombre: "))
            apellido_usuario = str(input("Ingresa tu apellido: "))
            consulta_cursor.execute("INSERT INTO usuario (nombre_usuario, apellido_usuario) VALUES (?,?)",(usuario_nuevo,apellido_usuario))
            nuevo_usuario.commit()
            print("Ingreso exitoso.")
    except ValueError:
        print("Error de digitacion, volver a ingresar.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")
    
