"""main."""

from __future__ import annotations

import logging
from typing import Annotated

import typer

from src.utils.logging import SetLogger

logger = SetLogger().logger

app = typer.Typer()


def setup_logging() -> None:
    """Set up logging level."""
    logger.setLevel(logging.DEBUG)

    for handler in logger.handlers:
        handler.setLevel(logging.DEBUG)

    logger.info("Updated logger level to: DEBUG")


@app.command()
def main(
    *,
    verbose: Annotated[bool, typer.Option(help="Verbose mode")] = False,
) -> None:
    """Recieve meta data for analytics."""
    if verbose:
        setup_logging()
