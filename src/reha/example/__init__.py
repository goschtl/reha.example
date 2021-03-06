import pathlib
import logging
import importlib
import importscan
from reiter.application.browser import TemplateLoader


TEMPLATES = TemplateLoader(
    str((pathlib.Path(__file__).parent / "templates").resolve()), ".pt"
)


def install_me(app):
    importscan.scan(importlib.import_module(__name__))
    logging.info(f"Import Addon {__name__}")
