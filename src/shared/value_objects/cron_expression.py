from src.shared.errors import InvalideCron
from croniter import croniter
from datetime import datetime


class CronExpression:
    """"""

    def __init__(self, value: str):
        value = value.strip()

        if not croniter.is_valid(value):
            raise InvalideCron(f"Invalid cron expression: {value}")

        self.value = value

    def next(self, from_dt: datetime | None = None) -> datetime:
        """"""
        base = from_dt or datetime.now()
        itr = croniter(self.value, base)
        return itr.get_next(datetime)
