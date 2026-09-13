# ⚽ Player Scouting & Comparison Tool

> Herramienta de comparación y scouting de jugadores de fútbol, construida como
> ejercicio deliberado de **TDD**, **Domain-Driven Design** y **Clean Architecture**.

## 🎯 Motivación

Este proyecto nace de la intersección entre dos intereses: el fútbol y la
ingeniería del software. En lugar de otro CRUD de práctica, el objetivo es
resolver un problema real —comparar jugadores y encontrar similitudes entre
ellos a partir de sus estadísticas— aplicando el mismo rigor de diseño y
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

- **`PuntuacionSimilitud`** (Value Object) — un porcentaje entero de 0 a
  100 que representa cuán parecidos son dos jugadores. Se valida a sí
  mismo: rechaza valores no enteros y fuera de rango.
- **`Estadisticas`** (Value Object) — agrupa las estadísticas de un
  jugador (por ahora, goles y asistencias), en vez de pasar números
  sueltos por el sistema. Se valida a sí mismo: enteros no negativos.
- **`Jugador`** (Entidad) — su identidad es el `player_id` de StatsBomb,
  no sus datos: dos jugadores con el mismo `player_id` son "el mismo
  jugador" aunque cambien de nombre o de equipo. Valida que el
  `player_id` sea un entero positivo y que la fecha de nacimiento no sea
  futura.
- **`Comparacion`** (Value Object) — compone dos `Jugador` y una
  `PuntuacionSimilitud`. Es **simétrica**: comparar A con B es lo mismo
  que comparar B con A, si la puntuación coincide.
- **`CalculadorDeSimilitud`** (Servicio de dominio) — calcula la
  similitud real entre dos jugadores a partir de sus `Estadisticas`.
  Por cada métrica (goles, asistencias) usa la fórmula
  `1 - |a-b| / max(a,b)` (con el caso especial de valores iguales →
  similitud 1, evitando así la división por cero), y combina las
  métricas con una media simple para producir una `PuntuacionSimilitud`
  final.

## 🧪 Metodología

Cada pieza de lógica de negocio se ha escrito con **TDD** (red → green →
refactor): primero el test que falla, después el código mínimo que lo
hace pasar. El historial de commits del proyecto refleja ese ciclo,
separando explícitamente el commit del test (`test:`) del de su
implementación (`feat:`), siguiendo el convenio de
[Conventional Commits](https://www.conventionalcommits.org/).

## 📦 Stack tecnológico

- **Python 3.14**
- **pytest** — testing, incluyendo `pytest.raises` para validar
  excepciones y `pytest.approx` para comparar resultados decimales
- *(próximamente)* un adaptador para [StatsBomb Open Data](https://github.com/statsbomb/open-data)
  como fuente real de estadísticas, una API (FastAPI) y un dashboard
  (Next.js)

## 🚦 Estado actual

🟡 En construcción. La capa de Dominio está completa y probada de
principio a fin:

- [x] `PuntuacionSimilitud` — Value Object con validación
- [x] `Estadisticas` — Value Object con validación
- [x] `Jugador` — Entidad con identidad y reglas de negocio
- [x] `Comparacion` — Value Object simétrico
- [x] `CalculadorDeSimilitud` — servicio de dominio que calcula la
      similitud real entre dos jugadores
- [ ] Adaptador de datos reales (StatsBomb Open Data)
- [ ] Capa de Aplicación (casos de uso)
- [ ] API (FastAPI)
- [ ] Dashboard (Next.js)

## ⚙️ Cómo ejecutar los tests

```bash
py -m venv .venv
.venv\Scripts\Activate.ps1   # En Mac/Linux: source .venv/bin/activate

pip install -r requirements.txt
pytest
```

## 📁 Estructura del proyecto

```
player-scouting/
├── src/
│   └── player_scouting/
│       └── domain/
│           ├── value_objects.py       # PuntuacionSimilitud
│           ├── estadisticas.py        # Estadisticas
│           ├── entities.py            # Jugador
│           ├── comparacion.py         # Comparacion
│           └── calculador_similitud.py # CalculadorDeSimilitud
├── tests/
│   └── domain/
│       ├── test_value_objects.py
│       ├── test_estadisticas.py
│       ├── test_entities.py
│       ├── test_comparacion.py
│       └── test_calculador_similitud.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## 📄 Licencia

Todos los derechos reservados. Este repositorio es público como
muestra de trabajo personal; no se concede permiso para copiar,
modificar o reutilizar el código sin autorización expresa del autor.
