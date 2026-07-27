from .arif import ArifProfile
from .stub import StubProfile
from .base import BaseProfile


DEFAULT_PROFILES = [
    ArifProfile(),
]

__all__ = [
    "ArifProfile",
    "BaseProfile",
    "DEFAULT_PROFILES",
]