## Descripción

Sistema de gestión desarrollado para facilitar el control y administración de información sindical y asambleas corporativas. Esta aplicación permite gestionar eficientemente el registro de asambleas, control de cuotas sindicales y manejo de información de trabajadores.

## Características Principales

- **Gestión de Trabajadores**
  - Registro completo de información personal
  - Control de altas y bajas
  - Seguimiento de salarios y cuotas sindicales

- **Administración Sindical**
  - Registro de sindicatos
  - Control de cuotas y pagos (MAP)
  - Gestión de información sindical

- **Gestión de Asambleas**
  - Registro de asistencia
  - Control de acuerdos
  - Almacenamiento de evidencias fotográficas
  - Seguimiento de participación

## Tecnologías Utilizadas

- Django 4.2.7
- Python 3.x
- Django Jazzmin (Para una interfaz de administración mejorada)
- SQLite (Base de datos)

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL del repositorio]
cd gestion_info_SEPR
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar migraciones:
```bash
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor:
```bash
python manage.py runserver
```

## Configuración

El proyecto utiliza una configuración estándar de Django con las siguientes características especiales:
- Interfaz administrativa personalizada con Django Jazzmin
- Sistema de almacenamiento de medios para imágenes de asambleas
- Gestión de sesiones de usuario

## Modelos Principales

- **Sindicato**: Gestión de información básica de sindicatos
- **Trabajador**: Control detallado de información de trabajadores
- **AsambleaAfiliados**: Registro de asambleas y sus detalles
- **MAP**: Control de pagos y cuotas sindicales

## Contribución

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios
4. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
5. Push a la rama (`git push origin feature/AmazingFeature`)
6. Abre un Pull Request
