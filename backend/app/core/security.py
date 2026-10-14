"""Security dependency placeholders.

Authentication (password hashing, login/logout, session or JWT issuance) is
explicitly out of scope for Milestone 0 (see docs/requirements/open-decisions.md,
decision D7) and will be implemented in Milestone 1. This module exists now so
that route modules can import a stable dependency name (`get_current_user`,
`require_admin`) without being rewritten when auth lands.

Until Milestone 1 ships, every dependency here raises 501 Not Implemented
rather than silently granting or denying access, so no endpoint can appear to
enforce security it does not actually have.
"""

from fastapi import HTTPException, status


def get_current_user() -> None:
    """Placeholder for the future "resolve the authenticated user" dependency.

    TODO(Milestone 1): validate a session/JWT token and return the User.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Authentication is not implemented yet (planned for Milestone 1).",
    )


def require_admin() -> None:
    """Placeholder for the future "require Administrator role" dependency.

    TODO(Milestone 1 / 5): depend on get_current_user and check role == ADMIN.
    Per REQ-4.7.1, a public user must never be able to self-assign this role.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Admin authorization is not implemented yet (planned for Milestone 1/5).",
    )
