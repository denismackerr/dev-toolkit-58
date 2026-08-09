class CustomError(Exception):
    pass

class NotFoundError(CustomError):
    def __init__(self, message="Not Found Error Occurred", *args):
        super().__init__(message, *args)

class ValidationError(CustomError):
    def __init__(self, message="Validation Error Occurred", *args):
        super().__init__(message, *args)

class DatabaseError(CustomError):
    def __init__(self, message="Database Error Occurred", *args):
        super().__init__(message, *args)

def handle_error(error):
    if isinstance(error, NotFoundError):
        print(f"Error: {error}")
    elif isinstance(error, ValidationError):
        print(f"Error: {error}")
    elif isinstance(error, DatabaseError):
        print(f"Error: {error}")
    else:
        print(f"Unknown Error: {error}")

try:
    raise NotFoundError()
except CustomError as e:
    handle_error(e)