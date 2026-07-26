from .base import BaseProfile


class StubProfile(BaseProfile):

    def __init__(self):
        super().__init__(
            name="Stub",
            min_score=0,
            keywords=[],
        )