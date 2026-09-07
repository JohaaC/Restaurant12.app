class Usuario:
    def __init__(self, identificacion: str, nombre: str):
        if not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self.identificacion = identificacion
        self.nombre = nombre

    def actualizar(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self.nombre = nombre

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            datos["identificacion"],
            datos["nombre"]
        )

    def __str__(self):
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre}"
        )