from servicios.restaurante import Restaurante


def mostrar_menu():

    print("\n========================================")
    print("       SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Registrar usuario")
    print("7. Buscar usuario")
    print("8. Listar usuarios")
    print("9. Actualizar usuario")
    print("10. Eliminar usuario")
    print("11. Realizar venta")
    print("12. Consultar ventas por usuario")
    print("13. Listar todas las ventas")
    print("14. Salir")
    print("========================================")


def main():

    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        )

        # ==================================
        # REGISTRAR PRODUCTO
        # ==================================

        if opcion == "1":

            codigo = input(
                "Código: "
            )

            nombre = input(
                "Nombre: "
            )

            try:
                precio = float(
                    input("Precio: ")
                )

                stock = int(
                    input("Stock: ")
                )

                exito, mensaje = (
                    restaurante.registrar_producto(
                        codigo,
                        nombre,
                        precio,
                        stock
                    )
                )

                print(mensaje)

            except ValueError:
                print(
                    "Error: precio o stock inválido."
                )

        # ==================================
        # BUSCAR PRODUCTO
        # ==================================

        elif opcion == "2":

            codigo = input(
                "Código del producto: "
            )

            producto = (
                restaurante.buscar_producto(codigo)
            )

            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")

        # ==================================
        # ACTUALIZAR PRODUCTO
        # ==================================

        elif opcion == "3":

            codigo = input(
                "Código del producto: "
            )

            nombre = input(
                "Nuevo nombre: "
            )

            try:
                precio = float(
                    input("Nuevo precio: ")
                )

                stock = int(
                    input("Nuevo stock: ")
                )

                exito, mensaje = (
                    restaurante.actualizar_producto(
                        codigo,
                        nombre,
                        precio,
                        stock
                    )
                )

                print(mensaje)

            except ValueError:
                print(
                    "Error: precio o stock inválido."
                )

        # ==================================
        # ELIMINAR PRODUCTO
        # ==================================

        elif opcion == "4":

            codigo = input(
                "Código del producto: "
            )

            exito, mensaje = (
                restaurante.eliminar_producto(
                    codigo
                )
            )

            print(mensaje)

        # ==================================
        # LISTAR PRODUCTOS
        # ==================================

        elif opcion == "5":

            productos = (
                restaurante.listar_productos()
            )

            if not productos:
                print(
                    "No existen productos registrados."
                )

            else:
                for producto in productos:
                    print(producto)

        # ==================================
        # REGISTRAR USUARIO
        # ==================================

        elif opcion == "6":

            identificacion = input(
                "Identificación: "
            )

            nombre = input(
                "Nombre: "
            )

            exito, mensaje = (
                restaurante.registrar_usuario(
                    identificacion,
                    nombre
                )
            )

            print(mensaje)

        # ==================================
        # BUSCAR USUARIO
        # ==================================

        elif opcion == "7":

            identificacion = input(
                "Identificación: "
            )

            usuario = (
                restaurante.buscar_usuario(
                    identificacion
                )
            )

            if usuario:
                print(usuario)
            else:
                print("Usuario no encontrado.")

        # ==================================
        # LISTAR USUARIOS
        # ==================================

        elif opcion == "8":

            usuarios = (
                restaurante.listar_usuarios()
            )

            if not usuarios:
                print(
                    "No existen usuarios registrados."
                )

            else:
                for usuario in usuarios:
                    print(usuario)

        # ==================================
        # ACTUALIZAR USUARIO
        # ==================================

        elif opcion == "9":

            identificacion = input(
                "Identificación: "
            )

            nombre = input(
                "Nuevo nombre: "
            )

            exito, mensaje = (
                restaurante.actualizar_usuario(
                    identificacion,
                    nombre
                )
            )

            print(mensaje)

        # ==================================
        # ELIMINAR USUARIO
        # ==================================

        elif opcion == "10":

            identificacion = input(
                "Identificación: "
            )

            exito, mensaje = (
                restaurante.eliminar_usuario(
                    identificacion
                )
            )

            print(mensaje)

        # ==================================
        # REALIZAR VENTA
        # ==================================

        elif opcion == "11":

            identificacion = input(
                "Identificación del usuario: "
            )

            codigo = input(
                "Código del producto: "
            )

            try:
                cantidad = int(
                    input("Cantidad: ")
                )

                exito, mensaje = (
                    restaurante.vender_producto(
                        codigo,
                        identificacion,
                        cantidad
                    )
                )

                print(mensaje)

            except ValueError:
                print(
                    "Error: la cantidad debe ser un número entero."
                )

        # ==================================
        # CONSULTAR VENTAS
        # ==================================

        elif opcion == "12":

            identificacion = input(
                "Identificación del usuario: "
            )

            ventas = (
                restaurante.consultar_ventas_usuario(
                    identificacion
                )
            )

            if not ventas:
                print(
                    "El usuario no tiene ventas registradas."
                )

            else:

                print(
                    "\nVENTAS DEL USUARIO"
                )

                for venta in ventas:

                    producto = (
                        restaurante.buscar_producto(
                            venta.producto_codigo
                        )
                    )

                    if producto:
                        print(
                            f"Producto: {producto.nombre} | "
                            f"Código: {venta.producto_codigo} | "
                            f"Cantidad: {venta.cantidad}"
                        )
                    else:
                        print(venta)

        # ==================================
        # LISTAR VENTAS
        # ==================================

        elif opcion == "13":

            ventas = (
                restaurante.listar_ventas()
            )

            if not ventas:
                print(
                    "No existen ventas registradas."
                )

            else:

                for venta in ventas:
                    print(venta)

        # ==================================
        # SALIR
        # ==================================

        elif opcion == "14":

            print(
                "Gracias por utilizar el sistema."
            )

            break

        else:
            print(
                "Opción inválida. Intente nuevamente."
            )


if __name__ == "__main__":
    main()