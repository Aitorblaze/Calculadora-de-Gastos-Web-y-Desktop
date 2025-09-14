Calculadora de Gastos Web y Desktop

Calculadora de Gastos Web y Desktop es una aplicación para registrar ingresos y gastos, calcular totales, visualizar gráficos interactivos y gestionar tus finanzas personales.
Incluye una versión web con Flask y una versión de escritorio con PyQt5, con almacenamiento en CSV y posibilidad de generar un ejecutable (.exe) para Windows.

🔹 Características

Registrar ingresos y gastos con descripción.

Visualizar totales: ingresos, gastos y saldo.

Mostrar gráfica interactiva de ingresos vs gastos.

Guardar registros en CSV (database.csv).

Interfaz profesional, limpia y fácil de usar.

Posibilidad de convertir la aplicación en .exe para escritorio.Calculadora de Gastos Web y Desktop

Calculadora de Gastos Web y Desktop es una aplicación para registrar ingresos y gastos, calcular totales, visualizar gráficos interactivos y gestionar tus finanzas personales.
Incluye una versión web con Flask y una versión de escritorio con PyQt5, con almacenamiento en CSV y posibilidad de generar un ejecutable (.exe) para Windows.

🔹 Características

Registrar ingresos y gastos con descripción.

Visualizar totales: ingresos, gastos y saldo.

Mostrar gráfica interactiva de ingresos vs gastos.

Guardar registros en CSV (database.csv).

Interfaz profesional, limpia y fácil de usar.

Posibilidad de convertir la aplicación en .exe para escritorio.
CalculadoraGastosWeb/
│
├── app.py                 # Versión web Flask
├── calculadora_desktop.py # Versión escritorio PyQt5
├── database.csv           # Archivo de datos (se genera automáticamente)
├── templates/             # Plantillas HTML para Flask
│     └── index.html
├── static/                # Archivos CSS o JS opcionales
└── README.md              # Este archivo

🔹 Tecnologías utilizadas

Python 3 → Lenguaje principal

Flask → Desarrollo web

PyQt5 → Interfaz de escritorio

Bootstrap 5 → Estilo y diseño web

Chart.js → Gráficas web

Matplotlib → Gráficas desktop

CSV → Almacenamiento de datos

INSTALACIÓN Y USO

Versión Web (Flask)

Instalar dependencias: pip install flask pandas

Ejecutar la app: python app.py

Abrir navegador en http://127.0.0.1:5000/

Usar la calculadora: añadir ingresos y gastos, ver totales y gráfica interactiva

Versión Desktop (PyQt5)

Instalar dependencias: pip install pyqt5 matplotlib pandas

Ejecutar la app: python calculadora_desktop.py

Se abrirá una ventana con inputs para ingresar datos, lista de registros, totales y gráfica integrada

CONVERSIÓN A EJECUTABLE (.exe)

Para web: pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
Para escritorio: pyinstaller --onefile --add-data "database.csv;." calculadora_desktop.py
El .exe se genera en la carpeta dist/. Doble clic abre la app directamente, sin necesidad de abrir la terminal.

Autor: Aitor Chamorro

GitHub: https://github.com/Aitorblaze

Email: chamorroblancaaitor@gmail.com
