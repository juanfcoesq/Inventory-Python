# 🧾 Inventory Manager

Una aplicación web para gestionar productos de inventario, pensada para empresas dedicadas a la distribución de tuberías de agua. Permite a los usuarios registrar productos, clasificarlos por categoría, gestionar cantidades y llevar un control organizado.

---

## 🚀 Características

- Registro y autenticación de usuarios.
- Agregado de productos con nombre, cantidad, proveedor y categoría.
- Visualización del inventario por usuario.
- Gestión de categorías para clasificar productos.

---

## 🛠️ Tecnologías usadas

- **Python 3.x**
- **Django 4.x**
- **Bootstrap 5**
- **SQLite**

---

## ⚙️ Instalación y ejecución

### 1. Clona el repositorio

```bash
https://github.com/juanfcoesq/Inventory-Python.git
cd inventory-manager
```

### 2. Crea un entorno virtual

```bash
python -m venv env
```

### 3. Activa el entorno virtual

#### En Windows

```bash
.\env\Scripts\activate
```

#### En macOS / Linux

```bash
source env/bin/activate
```

### 4. Aplica las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crea un superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para asignar nombre de usuario, correo y contraseña.

### 6. Ejecuta el servidor

```bash
python manage.py runserver
```

Accede a la app en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 👤 Usuarios

- Puedes registrarte como usuario desde la interfaz.
- También puedes acceder al panel de administración en:

```plaintext
http://127.0.0.1:8000/admin
```

---

## 🗃️ Estructura del proyecto

```plaintext
inventory-manager/
│
├── inventory/              # Aplicación principal
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── inventory_manager/      # Proyecto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3              # Base de datos SQLite
├── manage.py
└── requirements.txt
```

---

## 📦 Categorías sugeridas

Puedes agregar categorías desde el panel de administración o la base de datos. Ejemplos útiles para una empresa de tuberías:

- PVC
- PEX
- Conectores
- Válvulas
- Herramientas
- Accesorios
- Bridas
- Tubería Cobre

---
