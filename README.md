# Task Manager API

A tiny Flask + SQLite REST API for managing tasks.

## Endpoints

- `GET /tasks` — list all tasks
- `GET /tasks/<id>` — get a single task
- `POST /tasks` — create a task (`{"title": "...", "description": "..."}`)
- `DELETE /tasks/<id>` — delete a task

## Run locally

```bash
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
python -m app.main
```

## Test

```bash
pytest
```
