# Player Scouting

A small domain model, built test-first, for comparing football players by
how similar their statistics are.

## Domain

- `Player` — a player's identity (`player_id`, `name`, `position`,
  `date_of_birth`).
- `Statistics` — a player's `goals` and `assists`.
- `SimilarityScore` — a validated percentage (0-100) expressing how similar
  two players are.
- `SimilarityCalculator` — computes a `similarity_metric` between two values
  and a `total_similarity` between two `Statistics`, returning a
  `SimilarityScore`.
- `Comparison` — pairs two `Player`s with the `SimilarityScore` between
  them; two comparisons are equal regardless of player order.

## Project layout

```
src/player_scouting/domain/   # domain model
tests/domain/                 # unit tests
```

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) for dependency management

## Setup

```bash
uv sync
```

## Running tests

```bash
uv run pytest
```

## Linting and formatting

This project uses [Ruff](https://docs.astral.sh/ruff/) for both linting and
formatting:

```bash
uv run ruff check .
uv run ruff format .
```
