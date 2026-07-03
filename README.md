# PROYECTO: Clientes

# TECNOLOGIA: FastAPI

# AUTOR: Instructor Jhonny Guerrero

# DESCRIPCION: Sistema de Gestión de Facturación y Transacciones (API de Aprendizaje)

## Contexto

El proyecto simula el núcleo financiero de una plataforma comercial. Trabajaremos con tres entidades principales, simulando al inicio una relación como BD:

1. **Clientes:** (id, nombre, email, descripcion)
2. **Facturas:** (id, fecha, vr_total, cliente)
3. **Transacciones:** (id, cantidad, vr_unitario, id_factura)

---

## Inicio del proyecto clientes

Para mantener el enfoque en los fundamentos de FastAPI, el proyecto inicia de la forma más simple posible:

1. **Sin estructura de carpetas compleja** (Todo el código vive temporalmente en un archivo principal).
2. **Sin Routers (APIRouter)** (Todos los endpoints se registran directamente en la aplicación central).
3. **Sin Base de Datos** (Los datos se gestionan en memoria utilizando listas y diccionarios de Python).

## Prerequisitos

1. Python 3.12 o superior (esa versión está en mi equipo).
2. Git (recomendado) - GitHub.
3. Gestión de entornos virtuales (`venv`).
4. Instalar FastAPI[standard].

**NOTA:** Utilizaremos el gestor de dependencias por defecto PIP, pero pueden hacer uso del gestor UV.

## Instalación y configuración

Sigue estos pasos para poner en marcha tu entorno de desarrollo local:

1. Crear una carpeta del proyecto y abrir con Visual Studio Code.
2. En la consola de VSCode digitar los siguientes comandos:
    1. Crear entorno virtual

    **Windows** python -m venv .mi_env
    **macOS/Linux** python3 -m venv .mi_env

    2. Activar el entorno

    **Windows** .mi_env\Scripts\activate
    **macOS/Linux** source .mi_env/bin/activate

3. Instalar FastAPI

    pip install "fastapi[standard]"
    pip list -> ver listado de las instalaciones

4. Crear el archivo main.py
    Escribir código propio de una API.

5. Ejecutar, (modo desarrollo recomendado)
    1. **MODO PRODUCCION:** uvicorn main:app --reload
    2. **MODO DESARROLLO:** fastapi dev main.py

6. Ejecute el comando modo de desarrollado, en la consola podemos ver diferentes lineas, como por ejemplo estas que nos interesan para ver la documentación interactiva (Swagger Interfaz Grafica) así:
