from enum import Enum


class RoleEnum(str, Enum):
    OWNER = "owner"
    MEMBER = "member"


class PriorityEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
