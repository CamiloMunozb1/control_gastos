from funciones_sql.usuario_new import ingreso_usuario
from funciones_sql.gastos_usuario import gastos_ingresados
from funciones_sql.eliminar_gastos import eliminar_gastos
from funciones_sql.datos_completos import mostrar_datos

while True:
    print(
        """
            Bienvenido al control de gastos, elije una opcion:
            1. Ingreso de nuevo usuario.
            2. Ingreso de gastos.
            3. Eliminar gastos.
            4. Mostrar gastos.
            5. Salir
        """
    )
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            ingreso_usuario()
        elif usuario == 2:
            gastos_ingresados()
        elif usuario == 3:
            eliminar_gastos()
        elif usuario == 4:
            mostrar_datos()
        else:
            print("Gracias por usar el controlador de gastos, cuida tus ganancias.")
            break
    except ValueError:
        print("Error de digitacion, volver a intentar")