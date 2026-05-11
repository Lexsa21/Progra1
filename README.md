# 🎬 Sistema de Gestión de Cines

Sistema de gestión integral para complejos cinematográficos desarrollado en Python. Permite administrar películas, salas, funciones, venta de entradas y generación de informes desde una interfaz de consola.

Proyecto final de la materia **Algoritmos y Estructuras de Datos I**.

---

## 📋 Funcionalidades

### 🎥 Gestión de Películas
- Agregar, modificar y listar películas
- Filtrar por idioma y formato (2D / 3D)
- Gestión de funciones por película (días y horarios)

### 🎟️ Venta de Entradas
- Selección de cine, película, función y butacas
- Visualización del mapa de sala en tiempo real
- Cancelación de entradas con liberación automática de butacas
- Consulta de entradas por DNI

### 🏢 Gestión de Complejo de Cines
- Alta, baja y modificación de cines
- Gestión de salas con planta visual de butacas (tipo EXTREME / NORMAL)
- Habilitación/inhabilitación de butacas individuales
- Operaciones con conjuntos: películas en común entre cines, cines sin películas, películas disponibles en múltiples cines

### 📊 Informes
- Informe de ventas por cine y película
- Listado de películas disponibles
- Plantillas de salas con estado de butacas
- Análisis de butacas por tipo (EXTREME / NORMAL)
- Conteo recursivo de butacas disponibles
- Análisis de funciones por día y horario

### 💰 Promociones
- Simulador de descuentos sobre tarifas actuales

---

## 🗂️ Estructura del proyecto

```
Progra1/
├── main.py              # Punto de entrada, menús y flujo principal
├── utils.py             # Lógica de negocio y acceso a datos
├── validaciones.py      # Validaciones y expresiones regulares
├── tests/
│   ├── test_utils.py        # Tests unitarios de utilidades
│   └── test_validaciones.py # Tests unitarios de validaciones
├── peliculas.json       # Persistencia de películas
├── cines.json           # Persistencia de cines
├── salas.json           # Persistencia de salas y butacas
├── funciones.json       # Persistencia de funciones
├── entradas.json        # Persistencia de entradas vendidas
├── precios.json         # Tarifas por formato
└── errores.log          # Log de errores en tiempo de ejecución
```

---

## ⚙️ Requisitos

- Python 3.8 o superior
- pytest (solo para ejecutar los tests)

Instalación de dependencias:
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución

```bash
python main.py
```

Para correr los tests:
```bash
pytest tests/
```

---

## 🧪 Conceptos aplicados

| Concepto | Aplicación en el proyecto |
|---|---|
| Matrices | Generación de la sala 8x8 con tipos de butaca |
| Tuplas | Constantes de configuración (menús, días, formatos) |
| Comprensión de listas | Filtrado y transformación de películas, entradas y salas |
| Rebanado | Obtención de las primeras N películas |
| Cadenas | Formateo de salidas, normalización de entradas del usuario |
| Diccionarios | Estructura principal de datos (películas, cines, entradas) |
| Conjuntos | Operaciones entre cines (intersección, diferencia, subconjunto) |
| Lambda / map / filter / reduce | Informes de ventas, formateo de precios, filtros de películas |
| Excepciones | Manejo de errores con log persistente en `errores.log` |
| Archivos JSON | Persistencia completa de todos los datos del sistema |
| Expresiones regulares | Validación de DNI, horarios, butacas, nombres, direcciones |
| Recursividad | Conteo recursivo de butacas disponibles por sala |
| Tests unitarios | Suite de tests con pytest para utils y validaciones |
| Git | Historial de commits con ramas por entrega |
