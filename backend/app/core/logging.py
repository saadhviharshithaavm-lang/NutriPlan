"""Structured logging configuration for the FastAPI application."""

import logging
import sys


def configure_logging(debug: bool) -> None:
    level = logging.DEBUG if debug else logging.INFO
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(name)s %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S%z",
        )
    )
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers = [handler]

    # Quiet overly chatty third-party loggers in development.
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)
