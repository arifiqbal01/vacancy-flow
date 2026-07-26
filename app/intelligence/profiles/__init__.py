from .arif import ArifProfile
from .stub import StubProfile
from .base import BaseProfile


DEFAULT_PROFILES = [
    ArifProfile(),
    StubProfile(),
]

__all__ = [
    "ArifProfile",
    "StubProfile",
    "BaseProfile",
    "DEFAULT_PROFILES",
]