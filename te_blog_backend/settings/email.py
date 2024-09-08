from te_blog_backend.settings.environ import env


__all__ = [
    "DEFAULT_FROM_EMAIL",
    "SERVER_EMAIL",
    "EMAIL_SUBJECT_PREFIX",
    "EMAIL_BACKEND",
]


DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", "noreply@tovarisch.engineer")

SERVER_EMAIL = env.str("SERVER_EMAIL", "noreply@tovarisch.engineer")

EMAIL_SUBJECT_PREFIX = env.str("EMAIL_SUBJECT_PREFIX", "[Tovarisch Engineer Blog] ")

EMAIL_BACKEND = env.str("EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
