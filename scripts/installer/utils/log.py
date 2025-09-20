#!/usr/bin/env python3

import sys
import logging

ADW_LOG_STEP = logging.INFO + 1
ADW_LOG_SUCCESS = logging.INFO + 2

class AdwLogFormatter(logging.Formatter):
    _bold = "\033[1m"
    _reset = "\033[0m"
    _red = "\033[31m"
    _green = "\033[32m"
    _yellow = "\033[33m"
    _blue = "\033[34m"
    _magenta = "\033[35m"
    _cyan = "\033[35m"

    _format: str = "%(message)s"

    _FORMATS = {
        logging.DEBUG: f"{_bold}[DEBUG]{_reset} {_format}",
        logging.INFO: f"{_bold}{_blue}[INFO]{_reset} {_format}",
        ADW_LOG_STEP: f"{_bold}{_blue}[INFO]{_reset}{_blue} {_format}{_reset}",
        ADW_LOG_SUCCESS: f"{_bold}{_green}[ OK ]{_reset}{_green} {_format}{_reset}",
        logging.WARNING: f"{_bold}{_yellow}[WARN]{_reset}{_yellow} {_format}{_reset}",
        logging.ERROR: f"{_bold}{_red}[ERROR] {_format}{_reset}",
        logging.CRITICAL: f"{_bold}{_red}[CRITICAL] {_format}{_reset}",
    }

    def format(self, record):
        log_fmt = self._FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger("installer")
logger.setLevel(logging.INFO)

if sys.stderr.isatty():
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(AdwLogFormatter())
    logger.addHandler(handler)

def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)

def info(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)

def step(msg, *args, **kwargs):
    logger.log(ADW_LOG_STEP, msg, *args, **kwargs)

def success(msg, *args, **kwargs):
    logger.log(ADW_LOG_SUCCESS, msg, *args, **kwargs)

def warning(msg, *args, **kwargs):
    logger.warning(msg, *args, **kwargs)

def error(msg, *args, **kwargs):
    logger.error(msg, *args, **kwargs)

def critical(msg, *args, **kwargs):
    logger.critical(msg, *args, **kwargs)
    sys.exit(-1)