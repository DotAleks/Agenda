from src.shared.errors import InvalideDescriptionTitle


class TaskDescription:
    def __init__(self, value: str | None):
        if value is not None and len(value) > 400:
            raise InvalideDescriptionTitle()

        self.value = value
