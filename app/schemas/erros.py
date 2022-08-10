from fastapi import HTTPException


class ExampleBaseException(HTTPException):
    status_code = 500
    detail = "Internal Server Error"

    def __init__(self, detail=None):
        if detail:
            self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)


class UnauthorizedErrorResponse(ExampleBaseException):
    status_code = 401


class BadGatewayResponse(ExampleBaseException):
    status_code = 502
