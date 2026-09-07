import json
import os


class ArchivoServicio:

    def __init__(self):
        self.ruta_base = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "datos"
        )

        os.makedirs(self.ruta_base, exist_ok=True)

        self.ruta_productos = os.path.join(
            self.ruta_base,
            "productos.json"
        )

        self.ruta_usuarios = os.path.join(
            self.ruta_base,
            "usuarios.json"
        )

        self.ruta_ventas = os.path.join(
            self.ruta_base,
            "ventas.json"
        )

    def cargar_productos(self):
        return self._cargar(self.ruta_productos)

    def cargar_usuarios(self):
        return self._cargar(self.ruta_usuarios)

    def cargar_ventas(self):
        return self._cargar(self.ruta_ventas)

    def guardar_productos(self, productos):
        datos = [
            producto.a_diccionario()
            for producto in productos
        ]

        self._guardar(self.ruta_productos, datos)

    def guardar_usuarios(self, usuarios):
        datos = [
            usuario.a_diccionario()
            for usuario in usuarios
        ]

        self._guardar(self.ruta_usuarios, datos)

    def guardar_ventas(self, ventas):
        datos = [
            venta.a_diccionario()
            for venta in ventas
        ]

        self._guardar(self.ruta_ventas, datos)

    def _cargar(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                f"Advertencia: el archivo {os.path.basename(ruta)} "
                "contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                f"Error: no hay permisos para leer "
                f"{os.path.basename(ruta)}."
            )
            return []

    def _guardar(self, ruta, datos):
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print(
                f"Error: no hay permisos para guardar "
                f"{os.path.basename(ruta)}."
            )