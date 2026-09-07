# Sistema de Restaurante - Semana 12

## Descripción

Este proyecto corresponde a la evolución del sistema `restaurante_app` desarrollado para la asignatura de Programación Orientada a Objetos.

En esta Semana 12 se mantiene la funcionalidad desarrollada anteriormente y se incorporan mejoras en el uso de colecciones para optimizar las búsquedas y consultas frecuentes del sistema.

La aplicación permite administrar productos, usuarios y ventas, controlar el stock y conservar la información mediante archivos JSON.

---

## Objetivo de la Semana 12

El objetivo principal es mejorar el rendimiento de las operaciones de búsqueda y consulta mediante el uso adecuado de colecciones.

Se mantienen las listas principales para almacenar, recorrer y persistir los objetos, mientras que se utilizan diccionarios como estructuras auxiliares para realizar búsquedas mediante claves conocidas sin recorrer toda la lista.

---

## Funcionalidades

El sistema permite:

- Registrar productos.
- Buscar productos mediante su código.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Buscar usuarios mediante su identificación.
- Actualizar usuarios.
- Eliminar usuarios.
- Listar usuarios.
- Realizar ventas.
- Controlar el stock de los productos.
- Consultar las ventas de un usuario.
- Listar todas las ventas.
- Guardar y recuperar información mediante archivos JSON.

---

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
