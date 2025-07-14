# 4thewords - Backend

Este proyecto corresponde a la parte backend del sistema **4thewords**, desarrollado con **FastAPI** y ejecutado con Uvicorn.

## ✅ Requisitos

- Python 3.9 o superior
- pip
- Git (opcional)
- Virtualenv (opcional pero recomendado)

## 🚀 Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/usuario/4thewords_backend_nombre_apellido.git
   cd 4thewords_backend_nombre_apellido
   ```

2. (Opcional) Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

4. Restaura la base de datos:

   - Se deja incluido un archivo `.sql` para clonar la base de datos.
   - Puedes usar herramientas como **MySQL Workbench** para importar el archivo SQL.
   - Modifica el archivo `app/database.py` con los datos de conexión a tu base de datos local.

5. Ejecuta el servidor:

   ```bash
   uvicorn app.main:app --reload --host localhost --port 8080
   ```

6. Una vez ejecutado, abre tu navegador y ve a:

   ```
   http://localhost:8080/docs
   ```

   Desde ahí podrás registrar un nuevo usuario usando el endpoint `/register`.

## 📌 Notas

- El backend se ejecuta en `http://localhost:8080`
- Asegúrate de que este puerto esté libre antes de iniciar.
- Es recomendable usar **MySQL Workbench** para restaurar la base de datos desde el archivo `.sql`.
