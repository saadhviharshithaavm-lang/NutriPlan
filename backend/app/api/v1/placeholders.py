"""Shared helper for routes whose business logic is not implemented yet.

Per the master prompt (Section 5): "Do not invent API responses implying
business functionality is complete. Where future functionality is not
implemented, use ... a clear HTTP 501 response if a placeholder endpoint is
exposed." Every stub route in this milestone raises this instead of
fabricating a plausible-looking success response.
"""

from fastapi import HTTPException, status


def not_implemented(feature: str, milestone: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=f"{feature} is not implemented yet (planned for {milestone}).",
    )
