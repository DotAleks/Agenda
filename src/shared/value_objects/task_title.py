from src.shared.errors import InvalideTaskTitle


class TaskTitle:
    def __init__(self, value: str):
        if not value.strip():
            raise InvalideTaskTitle()

        if len(value) > 150:
            raise InvalideTaskTitle()

        self.value = value
