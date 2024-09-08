from .environ import env


__all__ = [
    "SITE_DOMAIN",
    "API_SITE_DOMAIN",
    "ADMIN_SITE_DOMAIN",
    "STATIC_SITE_DOMAIN",
    "MEDIA_SITE_DOMAIN",
    "SITE_URL",
    "API_SITE_URL",
    "ADMIN_SITE_URL",
    "STATIC_SITE_URL",
    "MEDIA_SITE_URL",
]


SITE_DOMAIN = env.str("SITE_DOMAIN", default="tovarisch.engineer")
API_SITE_DOMAIN = env.str("API_SITE_DOMAIN", default="api.tovarisch.engineer")
ADMIN_SITE_DOMAIN = env.str("ADMIN_SITE_DOMAIN", default="admin.tovarisch.engineer")
STATIC_SITE_DOMAIN = env.str("STATIC_SITE_DOMAIN", default="static.tovarisch.engineer")
MEDIA_SITE_DOMAIN = env.str("MEDIA_SITE_DOMAIN", default="media.tovarisch.engineer")

# Don't include '/admin' or a trailing slash
SITE_URL = env.str("SITE_URL", default="https://tovarisch.engineer")
API_SITE_URL = env.str("API_SITE_URL", default="https://api.tovarisch.engineer")
ADMIN_SITE_URL = env.str("ADMIN_SITE_URL", default="https://admin.tovarisch.engineer")
STATIC_SITE_URL = env.str("STATIC_SITE_URL", default="https://static.tovarisch.engineer")
MEDIA_SITE_URL = env.str("MEDIA_SITE_URL", default="https://media.tovarisch.engineer")
