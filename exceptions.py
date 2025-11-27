class TaskError(Exception):
    """Базовое исключение для ошибок задания."""
    pass


class EmptyArrayError(TaskError):
    """Ошибка, когда массивы не были введены."""
    pass


class InvalidMenuChoiceError(TaskError):
    """Ошибка неверного пункта меню."""
    pass


class InvalidNumberError(TaskError):
    """Ошибка, когда ожидалось число."""
    pass

#Все исключения имеют базовый класс TaskError, что облегчает обработку.
