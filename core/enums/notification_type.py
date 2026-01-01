from enum import Enum

class NotificationType(Enum):
    ONCE = 'once'
    INTERVAL = 'interval'
    DAYLI = 'dayli'
    WEEKLY = 'weekly'
    CUSTOM = 'custom'
