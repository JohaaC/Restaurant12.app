from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    def __init__(self):

        self.archivo_servicio = ArchivoServicio()

        # Colecciones principales
        self.productos = []
        self.usuarios = []
        self.ventas = []

        # Índices auxiliares para búsquedas rápidas
        self.productos_por_codigo = {}
        self.usuarios_por_identificacion = {}
        self.ventas_por_usuario = {}

        # Cargar datos desde JSON
        self.cargar_datos()

    # ==========================================
    # CARGA Y RECONSTRUCCIÓN DE ÍNDICES
    # ==========================================

    def cargar_datos(self):

        datos_productos = (
            self.archivo_servicio.cargar_productos()
        )

        for datos in datos_productos:
            try:
                producto = Producto.desde_diccionario(datos)

                self.productos.append(producto)

                self.productos_por_codigo[
                    producto.codigo
                ] = producto

            except (KeyError, ValueError) as error:
                print(
                    f"Error al cargar producto: {error}"
                )

        datos_usuarios = (
            self.archivo_servicio.cargar_usuarios()
        )

        for datos in datos_usuarios:
            try:
                usuario = Usuario.desde_diccionario(datos)

                self.usuarios.append(usuario)

                self.usuarios_por_identificacion[
                    usuario.identificacion
                ] = usuario

            except (KeyError, ValueError) as error:
                print(
                    f"Error al cargar usuario: {error}"
                )

        datos_ventas = (
            self.archivo_servicio.cargar_ventas()
        )

        for datos in datos_ventas:
            try:
                venta = Venta.desde_diccionario(datos)

                self.ventas.append(venta)

                if venta.usuario_id not in self.ventas_por_usuario:
                    self.ventas_por_usuario[
                        venta.usuario_id
                    ] = []

                self.ventas_por_usuario[
                    venta.usuario_id
                ].append(venta)

            except (KeyError, ValueError) as error:
                print(
                    f"Error al cargar venta: {error}"
                )

    # ==========================================
    # PRODUCTOS
    # ==========================================

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        stock: int
    ):

        if codigo in self.productos_por_codigo:
            return False, "Ya existe un producto con ese código."

        try:
            producto = Producto(
                codigo,
                nombre,
                precio,
                stock
            )

            self.productos.append(producto)

            # Actualizar índice
            self.productos_por_codigo[
                codigo
            ] = producto

            self.archivo_servicio.guardar_productos(
                self.productos
            )

            return True, "Producto registrado correctamente."

        except ValueError as error:
            return False, str(error)

    def buscar_producto(self, codigo: str):

        # Búsqueda optimizada con dict
        return self.productos_por_codigo.get(codigo)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        stock: int
    ):

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        try:
            producto.actualizar(
                nombre,
                precio,
                stock
            )

            self.archivo_servicio.guardar_productos(
                self.productos
            )

            return True, "Producto actualizado correctamente."

        except ValueError as error:
            return False, str(error)

    def eliminar_producto(self, codigo: str):

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        self.productos.remove(producto)

        # Eliminar también del índice
        del self.productos_por_codigo[codigo]

        self.archivo_servicio.guardar_productos(
            self.productos
        )

        return True, "Producto eliminado correctamente."

    def listar_productos(self):
        return self.productos

    # ==========================================
    # USUARIOS
    # ==========================================

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str
    ):

        if (
            identificacion
            in self.usuarios_por_identificacion
        ):
            return False, "Ya existe un usuario con esa identificación."

        try:
            usuario = Usuario(
                identificacion,
                nombre
            )

            self.usuarios.append(usuario)

            # Actualizar índice
            self.usuarios_por_identificacion[
                identificacion
            ] = usuario

            self.archivo_servicio.guardar_usuarios(
                self.usuarios
            )

            return True, "Usuario registrado correctamente."

        except ValueError as error:
            return False, str(error)

    def buscar_usuario(
        self,
        identificacion: str
    ):

        # Búsqueda optimizada con dict
        return self.usuarios_por_identificacion.get(
            identificacion
        )

    def actualizar_usuario(
        self,
        identificacion: str,
        nombre: str
    ):

        usuario = self.buscar_usuario(
            identificacion
        )

        if usuario is None:
            return False, "Usuario no encontrado."

        try:
            usuario.actualizar(nombre)

            self.archivo_servicio.guardar_usuarios(
                self.usuarios
            )

            return True, "Usuario actualizado correctamente."

        except ValueError as error:
            return False, str(error)

    def eliminar_usuario(
        self,
        identificacion: str
    ):

        usuario = self.buscar_usuario(
            identificacion
        )

        if usuario is None:
            return False, "Usuario no encontrado."

        self.usuarios.remove(usuario)

        # Eliminar también del índice
        del self.usuarios_por_identificacion[
            identificacion
        ]

        self.archivo_servicio.guardar_usuarios(
            self.usuarios
        )

        return True, "Usuario eliminado correctamente."

    def listar_usuarios(self):
        return self.usuarios

    # ==========================================
    # VENTAS
    # ==========================================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ):

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:
            return False, "Usuario no encontrado."

        producto = self.buscar_producto(
            codigo_producto
        )

        if producto is None:
            return False, "Producto no encontrado."

        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que cero."

        if producto.stock < cantidad:
            return False, "Stock insuficiente."

        try:
            venta = Venta(
                usuario.identificacion,
                producto.codigo,
                cantidad
            )

            # Mantener colección principal
            self.ventas.append(venta)

            # Mantener índice de ventas por usuario
            if (
                usuario.identificacion
                not in self.ventas_por_usuario
            ):
                self.ventas_por_usuario[
                    usuario.identificacion
                ] = []

            self.ventas_por_usuario[
                usuario.identificacion
            ].append(venta)

            # Disminuir stock
            producto.vender(cantidad)

            # Guardar cambios
            self.archivo_servicio.guardar_ventas(
                self.ventas
            )

            self.archivo_servicio.guardar_productos(
                self.productos
            )

            return True, "Venta realizada correctamente."

        except ValueError as error:
            return False, str(error)

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ):

        # Consulta optimizada
        return self.ventas_por_usuario.get(
            identificacion_usuario,
            []
        )

    def listar_ventas(self):
        return self.ventas