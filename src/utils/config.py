"""Config."""

from __future__ import annotations

import argparse
from configparser import ConfigParser


def parse_args() -> argparse.ArgumentParser.parse_args:
    """Parse arguments."""
    parser = argparse.ArgumentParser(description="Load configuration file")

    parser.add_argument(
        "--config",
        type=str,
        default="config.ini",
        help="Path to the configuration file",
    )

    return parser.parse_args()


def read_config(path: str) -> None:
    """Read config.ini file with typer."""
    config = ConfigParser()
    config.read(path)
    config.sections()

    return config


class Config:
    """Config load."""

    def __init__(self) -> None:
        self._args = parse_args()
        self._config_path = self._args.config
        self.config_parser = ConfigParser()
        self.config_parser.read(self._config_path)
