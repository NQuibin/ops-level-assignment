from typing import Any

class HttpException(Exception):
    def __init__(self, status_code: int, message: Any):
        super().__init__(str(message))
        self.status_code = status_code
        self.message = message
