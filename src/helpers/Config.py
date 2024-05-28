from __future__ import annotations

import json
from dataclasses import dataclass
import os

from logging import getLogger

log = getLogger(__name__)

__all__ = ("Config",)


@dataclass
class Config:
    token: str | None = None
    prefix: str | None = None
    api_key: str | None = None
    db_uri: str | None = None

    def init(cls, filename: str = "config.json") -> Config:
        with open(filename) as configFile:
            data = json.load(configFile)

        return Config(**data)

    def close(cls):
        return

    def generate(cls, filename: str = "config.json"):
        if os.path.exists(filename):
            log.error("File already exists")
            return
        log.warn("No file found, generating new config file")
        # Generate a file based on the dict of required items
        with open(filename, "w+") as configFile:
            json.dump(cls.__dict__, configFile, indent=4)

        print("Successfully generated config file")
