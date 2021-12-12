class InvalidValueException(RuntimeError):
    """Invalid value."""


class UnauthorizedException(RuntimeError):
    """Not authorized."""


class ConflictValueException(RuntimeError):
    """Conflict."""
