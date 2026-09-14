# ⚽ Player Scouting & Comparison Tool

> Herramienta de comparación y scouting de jugadores de fútbol, construida como
> ejercicio deliberado de **TDD**, **Domain-Driven Design** y **Clean Architecture**.

## 🎯 Motivación

Este proyecto nace de la intersección entre dos intereses: el fútbol y la
ingeniería del software. En lugar de otro CRUD de práctica, el objetivo es
resolver un problema real: comparar jugadores y encontrar similitudes entre
ellos a partir de sus estadísticas, aplicando el mismo rigor de diseño y
testing que se exige en un equipo de desarrollo profesional: cada pieza
del dominio, desde la más pequeña, ha sido construida test primero.

## 🏗️ Arquitectura

El proyecto sigue **Clean Architecture**: el dominio no depende de nada
externo (ni de una base de datos, ni de una API, ni de un framework web).
Las dependencias siempre apuntan hacia dentro.

```
┌─────────────────────────────────────────────┐
│  Presentación   (API REST, dashboard web)    │  ← pendiente
├─────────────────────────────────────────────┤
│  Infraestructura (StatsBomb, ficheros, BD)   │  ← pendiente
├─────────────────────────────────────────────┤
│  Aplicación     (casos de uso)               │  ← pendiente
├─────────────────────────────────────────────┤
│  Dominio        (entidades, reglas, servicios)│ ← ✅ construido
└─────────────────────────────────────────────┘
```

### El dominio, pieza a pieza

- **`SimilarityScore`** (Value Object): un porcentaje entero de 0 a
  100 que representa cuán parecidos son dos jugadores. Se valida a sí
  mismo: rechaza valores no enteros (incluidos booleanos) y fuera de rango.
- **`Statistics`** (Value Object): agrupa las estadísticas de un
  jugador (por ahora, goles y asistencias), en vez de pasar números
  sueltos por el sistema. Se valida a sí mismo: enteros no negativos.
- **`Player`** (Entidad): su identidad es el `player_id` de StatsBomb,
  no sus datos: dos jugadores con el mismo `player_id` son "el mismo
  jugador" aunque cambien de nombre o de equipo. Valida que el
  `player_id` sea un entero positivo y que la fecha de nacimiento no sea
  futura.
- **`Comparison`** (Value Object): compone dos `Player` y una
  `SimilarityScore`. Es **simétrica**: comparar A con B es lo mismo
  que comparar B con A, si la puntuación coincide.
- **`SimilarityCalculator`** (Servicio de dominio): calcula la
  similitud real entre dos jugadores a partir de sus `Statistics`.
  Por cada métrica (goles, asistencias) usa la fórmula
  `1 - |a-b| / max(a,b)` (con el caso especial de valores iguales →
  similitud 1, evitando así la división por cero), y combina las
  métricas con una media simple para producir una `SimilarityScore`
  final.

## 🧪 Metodología

Cada pieza de lógica de negocio se ha escrito con **TDD** (red → green →
refactor): primero el test que falla, después el código mínimo que lo
hace pasar. El historial de commits del proyecto refleja ese ciclo,
separando explícitamente el commit del test (`test:`) del de su
implementación (`feat:`), siguiendo el convenio de
[Conventional Commits](https://www.conventionalcommits.org/).

## 📦 Stack tecnológico

- **Python 3.14**, con type hints en toda la capa de dominio
- **pytest**: testing, incluyendo `pytest.raises` para validar
  excepciones y `pytest.approx` para comparar resultados decimales
- **Ruff**: linter y formatter
- **uv**: gestión de dependencias y de entornos virtuales
- *(próximamente)* un adaptador para [StatsBomb Open Data](https://github.com/statsbomb/open-data)
  como fuente real de estadísticas, una API (FastAPI) y un dashboard
  (Next.js)

## 🚦 Estado actual

🟡 En construcción. La capa de Dominio está completa y probada de
principio a fin:

- [x] `SimilarityScore`: Value Object con validación
- [x] `Statistics`: Value Object con validación
- [x] `Player`: Entidad con identidad y reglas de negocio
- [x] `Comparison`: Value Object simétrico
- [x] `SimilarityCalculator`: servicio de dominio que calcula la
      similitud real entre dos jugadores
- [x] Dominio traducido al inglés (nombres y mensajes de error)
- [x] Type hints, Ruff y uv integrados en el flujo de desarrollo
- [ ] Adaptador de datos reales (StatsBomb Open Data)
- [ ] Capa de Aplicación (casos de uso)
- [ ] API (FastAPI)
- [ ] Dashboard (Next.js)

## ⚙️ Cómo ejecutar los tests

Este proyecto usa [uv](https://docs.astral.sh/uv/) para gestionar
dependencias y el entorno virtual:

```bash
uv sync
uv run pytest
```

## 🧹 Linting y formatting

```bash
uv run ruff check .
uv run ruff format .
```

## 📁 Estructura del proyecto

```
player-scouting/
├── src/
│   └── player_scouting/
│       └── domain/
│           ├── value_objects.py        # SimilarityScore
│           ├── statistics.py           # Statistics
│           ├── entities.py             # Player
│           ├── comparison.py           # Comparison
│           └── similarity_calculator.py # SimilarityCalculator
├── tests/
│   └── domain/
│       ├── test_value_objects.py
│       ├── test_statistics.py
│       ├── test_entities.py
│       ├── test_comparison.py
│       └── test_similarity_calculator.py
├── .gitignore
├── pyproject.toml
├── uv.lock
├── pytest.ini
└── README.md
```

## 📄 Licencia

Todos los derechos reservados. Este repositorio es público como
muestra de trabajo personal; no se concede permiso para copiar,
modificar o reutilizar el código sin autorización expresa del autor.
