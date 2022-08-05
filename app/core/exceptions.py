from typing import ClassVar

from fastapi import status


class BaseException(Exception):
    STATUS_CODE: ClassVar[int] = status.HTTP_500_INTERNAL_SERVER_ERROR
    MESSAGE: ClassVar[str] = "Internal Server Error"

    def __init__(self, message: str | None = None):
        self.status_code = self.STATUS_CODE
        self.message = message or self.MESSAGE
        super().__init__(f"{self.status_code} - {self.message}")


class BadRequestException(BaseException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    MESSAGE = "Bad Request"


class NotAuthorizedException(BaseException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    MESSAGE = "Unauthorized"


class ForbiddenException(BaseException):
    STATUS_CODE = status.HTTP_403_FORBIDDEN
    MESSAGE = "Forbidden"


class NotFoundException(BaseException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    MESSAGE = "Not Found"


class BadGatewayException(BaseException):
    STATUS_CODE = status.HTTP_502_BAD_GATEWAY
    MESSAGE = "Bad Gateway"
