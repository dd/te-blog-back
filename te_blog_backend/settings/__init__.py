# ruff: noqa: F405, I001

import logging

from .environ import BASE_DIR
from .base import *
from .django import *
from .static_and_media import *
from .email import *
# from .wagtail import *
# from .debug import *
# INSTALLED_APPS.extend(_DEBUG_INSTALLED_APPS)
# MIDDLEWARE.extend(_DEBUG_MIDDLEWARE)
# from .api import *


logger = logging.getLogger("te_blog")


_GREEN = "\033[92m"
_RED = "\033[91m"
_ENDC = "\033[0m"


"""
It is suggested that local_settings store only settings specific to a specific runtime environment.
For example, an application running on the server can use a separate backend to send emails, for
which it is necessary to have an additional set of settings, which were not intended during the
development of the entire application and relate exclusively to a specific application on the
server.
"""
try:
    from local_settings import *
except ImportError:
    pass
else:
    logger.warning(
        f"{_GREEN}Additional settings have been downloaded from {_RED}`local_settings.py`{_ENDC}"
    )
