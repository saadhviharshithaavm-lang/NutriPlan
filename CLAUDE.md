# CLAUDE.md

Repository-wide conventions for working in NutriPlan. See `docs/architecture/overview.md`
for the full architecture, `docs/requirements/requirements-matrix.md` for SRS traceability,
and `docs/requirements/open-decisions.md` before resolving any ambiguity in the SRS or
Project Description yourself — check whether it's already been decided there first.

## Project phase discipline

- This repository implements **Phase 1 only**: a deterministic, rule-based recommendation
  engine. Never add LLM API calls, ML models, LangChain, or vector database dependencies.
  Phase 2 is documented for context in the requirements but is not to be built here.
- Hard constraints — dietary preference, allergies, weekly budget, cooking-time limit — must
  **never** be relaxed to improve ranking, variety, or user satisfaction, at any point in the
  pipeline, including in the (not-yet-built) replacement flow. See
  `docs/requirements/open-decisions.md`, decision D2, for what "closest feasible plan" means
  in practice: fill what can be filled without violating a hard constraint, and explicitly
  report what cannot, rather than ever serving a constraint-violating meal.
- Do not implement a feature "enough to look done." If an endpoint's business logic isn't
  built yet, it must return HTTP 501 via `app/api/v1/placeholders.not_implemented(...)` —
  never a fabricated success response. If a frontend page's backend isn't ready, render
  `components/ui/PlannedFeatureNotice`, not fake/placeholder data presented as real.

## Backend conventions (`backend/`)

- Layering is strict: `api/` → `services/` → (`repositories/` and/or `rule_engine/`) →
  `models/`. Routes never query the database directly; they depend on a service. (Milestone
  0's stub routes are the only exception, since they have no service to call yet.)
  See `docs/architecture/overview.md` for the full diagram.
- `rule_engine/` must stay framework-agnostic: no SQLAlchemy or FastAPI imports. It operates
  on the plain dataclasses in `rule_engine/types.py` so every stage is independently
  unit-testable and reusable as the future Phase 2 post-validation step.
- Every SQLAlchemy model cross-reference in a type hint (e.g. `Mapped["Recipe"]`) must have a
  corresponding `if TYPE_CHECKING:` import, so Ruff's F821 check passes without suppressions.
- Use Python 3.13 syntax: `X | None` over `Optional[X]`, `enum.StrEnum` over `(str, Enum)`,
  PEP 695 generics (`class Foo[T]`) over `typing.Generic`.
- Settings are read exclusively through `app.core.config.get_settings()` (pydantic-settings).
  Never hardcode a connection string, secret, or URL in application code.
- Run `ruff check .` and `pytest` from inside `backend/` before considering backend work
  done. A skipped test (e.g. the live-database integration test when no DB is reachable) is
  acceptable; a failing or silently-passing-but-wrong test is not.
- New Alembic migrations: when you add a bare `sa.ForeignKey(...)` column inside a raw
  migration's `op.create_table`, you must give it an explicit `sa.Integer()` (or matching)
  type — SQLAlchemy cannot infer a FK column's type from the target table outside the ORM.
  This bit the initial migration during Milestone 0; it was caught by actually running
  `alembic upgrade head`/`downgrade base` against a real Postgres instance, not by
  inspection. Always validate a new migration against a real database the same way.

## Frontend conventions (`frontend/`)

- One shared Axios instance (`src/lib/apiClient.ts`) for all HTTP calls — never construct a
  second client or hardcode a base URL in a component.
- Directory roles: `app/` (routing/app shell), `components/ui/` (generic primitives, no
  feature logic), `components/layout/` (nav/footer/layout), `pages/` (one per route),
  `features/` (feature-specific logic/components), `hooks/`, `lib/`, `types/`.
- Design tokens live in `src/index.css`'s Tailwind v4 `@theme` block (`warm-*` neutrals,
  `ink-*` text, `leaf-*` green accent). Add new tokens there rather than inlining hex values
  in components.
- Run `npm run lint`, `npm run typecheck`, `npm test`, and `npm run build` before considering
  frontend work done.

## Documentation discipline

- `docs/requirements/NutriPlan-SRS.docx` and `NutriPlan-Project-Description.docx` are
  authoritative source documents — never edit them. If you find a new ambiguity or make a new
  assumption, add it to `docs/requirements/open-decisions.md` rather than silently resolving
  it in code.
- Keep `docs/requirements/requirements-matrix.md`'s status column honest as features land —
  it is the single source of truth for "what's actually implemented" versus what's scaffolded
  or planned.
