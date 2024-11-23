import sqlite3
import pandas as pd

def mostrar_datos():
    try:
        with sqlite3.connect("C:/Users/POWER/gastos_control.db") as datos_completos:
            consulta_cursor = datos_completos.cursor()
            consulta_cursor.execute("""
                                        SELECT usuario.nombre_usuario,apellido_usuario,gastos.gasto_usuario
                                        FROM usuario
                                        JOIN gastos ON usuario.usuario_ID == gastos.usuario_ID
                                    """)
            resultado = consulta_cursor.fetchall()
            resultado_df = pd.DataFrame(resultado)
            print(resultado_df)
    except sqlite3.Error as error:
        print(f"{error}")