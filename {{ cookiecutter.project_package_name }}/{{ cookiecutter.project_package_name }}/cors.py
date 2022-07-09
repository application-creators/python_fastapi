from fastapi.middleware.cors import CORSMiddleware
from settings import settings


def configure_cors(app):
    if settings.cors_enabled:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.cors_allow_origins,
            allow_methods=settings.cors_allow_methods,
            allow_headers=settings.cors_allow_headers,
        )
