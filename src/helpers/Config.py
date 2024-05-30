from __future__ import annotations

import json
from dataclasses import dataclass
import os

import re

from logging import getLogger

log = getLogger(__name__)

__all__ = ("Config",)


@dataclass
class Config:
    token: str | None = None
    prefix: str | None = None
    api_key: str | None = None
    db_uri: str | None = None
    error_webbook: str | None = None

    def init(cls, filename: str = "config.json") -> Config:
        cls.__generate()
        with open(filename) as configFile:
            data = json.load(configFile)

        config = Config(**data)

        if not config.error_webbook:
            return config

        url = re.search("^(https:|http:|www\.)\S*", config.error_webbook)

        if not url:
            log.error("Webhook url is invalid, webhooks will not work")
            config.error_webbook = None
            return config

        return config

    def close(cls):
        return

    # Internal generator class
    def __generate(cls, filename: str = "config.json"):
        if not os.path.exists(filename):
            with open(filename, "w+") as configFile:
                json.dump(cls.__dict__, configFile, indent=4)
