# Sistema de Gestión de Cines

Sistema de gestión para complejos cinematográficos en Python, con interfaz de consola. Administra películas, salas, funciones, venta de entradas e informes.

Proyecto final de **Algoritmos y Estructuras de Datos I** (UADE). Después de la entrega le sumé tests unitarios y separé la lógica de negocio de las validaciones.

## Funcionalidades

**Películas**
- Alta, modificación y listado
- Filtros por idioma y formato (2D / 3D)
- Funciones asociadas por día y horario

**Venta de entradas**
- Selección de cine, película, función y butacas
- Mapa de sala actualizado en tiempo real
- Cancelación con liberación automática de butacas
- Consulta de entradas por DNI

**Complejo de cines**
- Alta, baja y modificación de cines
- Salas con planta visual de butacas (EXTREME / NORMAL)
- Habilitación e inhabilitación de butacas individuales
- Comparación entre cines: películas en común, cines sin cartelera, películas disponibles en varios complejos

**Informes**
- Ventas por cine y por película
- Plantillas de salas con estado de butacas
- Análisis de butacas por tipo y de funciones por día

**Promociones**
- Simulador de descuentos sobre las tarifas vigentes

## Requisitos

- Python 3.8 o superior
- pytest (solo para los tests)

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

Tests:

```bash
pytest tests/
```

## Estructura

```
Progra1/
├── main.py              # Punto de entrada, menús y flujo principal
├── utils.py             # Lógica de negocio y acceso a datos
├── validaciones.py      # Validaciones y expresiones regulares
├── tests/
│   ├── test_utils.py
│   └── test_validaciones.py
├── peliculas.json       # Persistencia de películas
├── cines.json           # Persistencia de cines
├── salas.json           # Persistencia de salas y butacas
├── funciones.json       # Persistencia de funciones
├── entradas.json        # Persistencia de entradas vendidas
├── precios.json         # Tarifas por formato
└── errores.log          # Log de errores en tiempo de ejecución
```

## Implementación

**Persistencia en JSON.** Todo el estado del sistema —cines, salas, funciones, entradas y precios— vive en archivos JSON separados por entidad. No hay base de datos: al arrancar se cargan y al modificar se reescriben.

**Manejo de errores con log.** Las excepciones se capturan y se registran en `errores.log` con su contexto, en vez de cortar la ejecución. El usuario ve un mensaje claro y el detalle técnico queda guardado.

**Validaciones con expresiones regulares.** DNI, horarios, identificadores de butaca, nombres y direcciones se validan antes de llegar a la lógica de negocio, en un módulo aparte.

**Recursividad.** El conteo de butacas disponibles por sala está resuelto recursivamente recorriendo la matriz de la planta.

**Operaciones con conjuntos.** Las comparaciones entre carteleras de distintos cines usan intersección, diferencia y subconjunto en lugar de recorrer listas anidadas.

**Tests unitarios.** Suite con pytest sobre `utils` y `validaciones`, agregada después de la entrega para poder refactorizar sin romper nada.

---

Parte de mi portfolio: [lexsa21.github.io](https://lexsa21.github.io)
