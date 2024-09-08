import logging
from pathlib import Path

import environ


logger = logging.getLogger("te_blog")


__all__ = [
    "BASE_DIR",
    "env",
    "ENV_PATH",
]


_GREEN = "\033[92m"
_RED = "\033[91m"
_ENDC = "\033[0m"

PROJECT_DIR = Path(__file__).parent.parent
BASE_DIR = PROJECT_DIR.parent


env = environ.Env(
    TE_DEBUG=(bool, False),
)
env.prefix = "TE_"
ENV_PATH = env.str("ENV_PATH", BASE_DIR / ".env")
environ.Env.read_env(ENV_PATH)
logger.warning(f"{_GREEN}Loading env from {_RED}`{ENV_PATH}`{_ENDC}")
