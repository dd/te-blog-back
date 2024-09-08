"""
File storages and operations
"""

from urllib.parse import urljoin

from te_blog_backend.settings.base import MEDIA_SITE_URL
from te_blog_backend.settings.base import STATIC_SITE_URL
from te_blog_backend.settings.environ import BASE_DIR
from te_blog_backend.settings.environ import env


__all__ = [
    "STATIC_ROOT",
    "STATIC_URL_WITHOUT_DOMAIN",
    "STATIC_URL",
    "MEDIA_ROOT",
    "MEDIA_URL_WITHOUT_DOMAIN",
    "MEDIA_URL",
    "FILE_UPLOAD_HANDLERS",
]


STATIC_ROOT = env.path("STATIC_ROOT", default=BASE_DIR / "static")
STATIC_URL_WITHOUT_DOMAIN = env.str("STATIC_URL_WITHOUT_DOMAIN", default="/static/")
STATIC_URL = env.str("STATIC_URL", default=urljoin(STATIC_SITE_URL, STATIC_URL_WITHOUT_DOMAIN))

MEDIA_ROOT = env.path("MEDIA_ROOT", default=BASE_DIR / "media")
MEDIA_URL_WITHOUT_DOMAIN = env.str("MEDIA_URL_WITHOUT_DOMAIN", default="/media/")
MEDIA_URL = env.str("MEDIA_URL", default=urljoin(MEDIA_SITE_URL, MEDIA_URL_WITHOUT_DOMAIN))

FILE_UPLOAD_HANDLERS = (
    "meringue.core.upload_handlers.MemoryFileUploadHandler",
    "meringue.core.upload_handlers.TemporaryFileUploadHandler",
)
