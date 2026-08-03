class CustomError(Exception):
    pass

class ValidationError(CustomError):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field

class NotFoundError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class PermissionError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class DatabaseError(CustomError):
    def __init__(self, message, db_code):
        super().__init__(message)
        self.db_code = db_code

class NetworkError(CustomError):
    pass

class TimeoutError(NetworkError):
    def __init__(self, message, timeout):
        super().__init__(message)
        self.timeout = timeout
