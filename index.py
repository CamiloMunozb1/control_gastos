while True:
    print(
        """
            Bienvenido al control de gastos, elije una opcion:
            1. Ingreso de nuevo usuario.
            2. Ingreso de gastos.
            3. Mostrar gastos.
            4. Salir
        """
    )
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            print("Proxima funcion.")
        elif usuario == 2:
            print("Proxima funcion.")
        elif usuario == 3:
            print("Proxima funcion.")
        else:
            print("Proxima funcion.")
    except ValueError:
        print("Error de digitacion, volver a intentar")