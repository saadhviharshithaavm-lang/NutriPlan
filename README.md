# NutriPlan — Adaptive Meal Planning Based on Lifestyle

NutriPlan is a full-stack web application that generates personalized weekly meal plans and
consolidated grocery lists based on a user's dietary preferences, health goals, allergies,
weekly budget, and available cooking time.

**Status: Milestone 0 — Project Foundation.** This repository currently contains a runnable
scaffold (backend, frontend, database schema, CI) with the application's *structure* in place
and its *business logic* intentionally not yet implemented. See
[Implemented vs. planned](#implemented-vs-planned-features) below before assuming any feature
works end to end.

## Project scope

- **Phase 1 (this repository):** a deterministic, rule-based recommendation engine. Every
  recommendation decision is explainable, reproducible, and validated against non-negotiable
  constraints (diet, allergies, budget, cooking time).
- **Phase 2 (future, out of scope):** an LLM personalization layer operating on Phase 1's
  candidate plans, with its output re-validated by the same constraint validator before it
  reaches a user. No LLM/ML code exists in this repository.

See `docs/requirements/` for the source SRS and Project Description, and
`docs/requirements/requirements-matrix.md` for the requirement-by-requirement implementation
status.

## Technology stack

| Layer | Technology |
|---|---|
| Frontend | React 19 + TypeScript, Vite, Tailwind CSS v4, React Router 8, Axios, React Hook Form + Zod, Recharts, Vitest + React Testing Library |
| Backend | Python 3.13, FastAPI, Pydantic v2 + pydantic-settings, SQLAlchemy 2.x, Alembic, PostgreSQL via psycopg 3, Pytest + HTTPX, Ruff |
| Infrastructure | Docker Compose (local PostgreSQL), GitHub Actions CI |

Exact pinned versions are in `backend/requirements.txt` and `frontend/package.json`.

## Monorepo structure

```
NutriPlan/
├── backend/            FastAPI application
│   ├── app/
│   │   ├── api/v1/      Versioned REST routes
│   │   ├── core/        Settings, security, logging, error handling
│   │   ├── db/          Session management, declarative base
│   │   ├── models/      SQLAlchemy entities
│   │   ├── schemas/     Pydantic request/response schemas
│   │   ├── repositories/ Persistence layer
│   │   ├── services/    Business logic orchestration
│   │   └── rule_engine/ Deterministic recommendation pipeline (structure only)
│   ├── alembic/         Migrations
│   └── tests/
├── frontend/            Vite + React + TypeScript application
│   └── src/
│       ├── app/          Routing and app shell
│       ├── components/   ui/ (primitives) and layout/ (nav, footer)
│       ├── pages/         One component per route
│       ├── features/      Feature-specific logic (e.g. health check)
│       ├── hooks/, lib/, types/
├── docs/
│   ├── requirements/     SRS, Project Description, traceability matrix, open decisions
│   └── architecture/     Architecture and database design docs
├── .github/workflows/    CI
└── compose.yaml          Local PostgreSQL
```

## Prerequisites

- Python 3.13
- Node.js 22+ and npm
- Docker Desktop (for local PostgreSQL via Docker Compose)

## Environment setup

Copy the example environment files (never commit the real `.env` files):

```powershell
# Windows PowerShell
Copy-Item .env.example .env
Copy-Item backend\.env.example backend\.env
Copy-Item frontend\.env.example frontend\.env
```

```bash
# macOS/Linux
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

The root `.env` is consumed by Docker Compose; `backend/.env` must use the same Postgres
credentials and the same host port (`5433`, not Postgres's default `5432`).

## Docker: local PostgreSQL

```powershell
docker compose up -d db
```

```bash
docker compose up -d db
```

This starts PostgreSQL 16, bound to `127.0.0.1:5433`, with data persisted in a named Docker
volume (`nutriplan_db_data`).

## Backend: install and run

```powershell
# Windows PowerShell, from the repository root
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
python -m alembic upgrade head
python -m uvicorn app.main:app --reload
```

```bash
# macOS/Linux
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m alembic upgrade head
python -m uvicorn app.main:app --reload
```

The API is then available at `http://127.0.0.1:8000`, with interactive Swagger docs at
`http://127.0.0.1:8000/docs`.

### Database migrations

```powershell
python -m alembic upgrade head     # apply all migrations
python -m alembic downgrade base   # roll back everything (destructive)
python -m alembic revision -m "describe your change"   # create a new empty migration
```

## Frontend: install and run

```powershell
cd frontend
npm install
npm run dev
```

```bash
cd frontend
npm install
npm run dev
```

The app is then available at `http://localhost:5173`. In development, requests to `/api/*`
are forwarded by Vite's dev proxy to the backend on port 8000 (see `frontend/vite.config.ts`)
— no CORS configuration is needed for local development.

## Development URLs

| Service | URL |
|---|---|
| Frontend (Vite dev server) | http://localhost:5173 |
| Backend API | http://127.0.0.1:8000 |
| Swagger / OpenAPI docs | http://127.0.0.1:8000/docs |
| PostgreSQL (host port) | 127.0.0.1:5433 |

## Tests

```bash
# Backend, from backend/ with the venv active
ruff check .
python -m pytest

# Frontend, from frontend/
npm run lint
npm run typecheck
npm test
npm run build
```

The backend's live-database integration test (`tests/test_db_integration.py`) skips itself
automatically if no PostgreSQL instance is reachable at the configured `DATABASE_URL` —
run `docker compose up -d db` first if you want it to actually execute.

## Troubleshooting

- **`psycopg.OperationalError: connection refused`** — the Postgres container isn't running
  or hasn't finished starting. Run `docker compose up -d db` and wait a few seconds, or check
  `docker compose logs db`.
- **Alembic can't find `app`** — run `alembic` commands from inside `backend/` with the venv
  activated, not from the repository root.
- **Frontend shows "API unreachable"** — the backend isn't running, or isn't on port 8000.
  Start it with `python -m uvicorn app.main:app --reload` from `backend/`.
- **Docker Desktop hangs / `docker info` never returns** — this can happen if Docker Desktop
  is stuck on a first-run license dialog. Open the Docker Desktop app directly and complete
  any prompt, then retry `docker compose up -d db`.
- **Port 5433 already in use** — another process (or a previous NutriPlan Postgres container)
  is bound to it; stop it with `docker compose down`, or change the host port mapping in
  `compose.yaml` and update `backend/.env` to match.

## Implemented vs. planned features

| Feature | Status |
|---|---|
| Health check (`GET /api/v1/health`), Swagger docs | **Implemented** |
| Database schema (13 tables) + initial migration | **Implemented** |
| Rule engine package structure (interfaces, types, documented constants) | **Implemented** (structure only — no recommendation logic yet) |
| Frontend routes/shells for all 10 planned screens | **Implemented** (static shells; see each page's "Planned — Milestone N" notice) |
| User registration, login, profile management | Planned — Milestone 1 |
| Nutrition target calculation, hard-constraint filtering | Planned — Milestone 2 |
| Weekly meal plan generation, grocery list aggregation | Planned — Milestone 3 |
| Feedback capture, meal replacement | Planned — Milestone 4 |
| Dashboard, Admin Panel CRUD | Planned — Milestone 5 |
| Phase 2 LLM personalization layer | Out of scope for this repository |

See `docs/requirements/requirements-matrix.md` for the full requirement-by-requirement
mapping and `docs/development-roadmap.md` for the milestone plan.

## Safety

Nutrition values and meal costs shown anywhere in NutriPlan are estimates for planning
purposes. NutriPlan is not a substitute for professional medical or nutritional advice.
