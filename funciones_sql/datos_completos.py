
#  SE IMPORTA LA LIBRERIA "sqlite3" PARA EL MANEJO DE LA BASE DE DATOS.

import sqlite3

# SE USA LA LIBRERIA "pandas" PARA DIVISAR LOS DATOS DE LA TABLA CON "dataframe".

import pandas as pd


# FUNCION PARA SER USADA EN EL INDEX

def mostrar_datos():
    try:

        # CONEXION CON LA BASE DE DATOS.

        with sqlite3.connect("C:/Users/POWER/gastos_control.db") as datos_completos:

            # SE CREA UN CURSOR PARA MANEJAR LA BASE DE DATOS.

            consulta_cursor = datos_completos.cursor()

            # CONSULTA SQL QUE PERMITE TOMAR LOS DATOS DE LA TABLA "usuario" Y JUNTARLAS CON LA TABLA "gastos".

            consulta_cursor.execute("""
                                        SELECT usuario.nombre_usuario,apellido_usuario,gastos.gasto_usuario
                                        FROM usuario
                                        JOIN gastos ON usuario.usuario_ID == gastos.usuario_ID
                                    """)
            
            # CON "fetchall" SE AGRUPAN TODAS LAS FILAS.

            resultado = consulta_cursor.fetchall()

            # VISUALISAMOS LOS DATOS CON "DataFrame".

            resultado_df = pd.DataFrame(resultado)

            # SE IMPRIMEN LOS RESULTADOS.

            print(resultado_df)
    
    # MANEJO DE ERRORES.
    
    except sqlite3.Error as error:
        print(f"{error}")