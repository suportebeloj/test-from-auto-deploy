import uvicorn
from fastapi import FastAPI
from internal.ports.app import APIInterface

from internal.ports.framework_left import HTTPAPIInterface
from internal.ports.framework_right import DbportInterface


class Adapter(HTTPAPIInterface):

    def __init__(self, http_server_instance: FastAPI, database_adapter: DbportInterface = None, application_adapter: APIInterface = None):
        super().__init__(http_server_instance, database_adapter, application_adapter)
        self.server.add_api_route(
            "/addition/{a}/{b}", self.get_addition_route, methods=["GET"])
        self.server.add_api_route(
            "/subtraction/{a}/{b}", self.get_subtraction_route, methods=["GET"])
        self.server.add_api_route(
            "/multiplication/{a}/{b}", self.get_multiplication_route, methods=["GET"])
        self.server.add_api_route(
            "/division/{a}/{b}", self.get_division_route, methods=["GET"])

    def get_addition_route(self, a, b):
        try:
            a = int(a)
        except Exception as err:
            return str(err)

        try:
            b = int(b)
        except Exception as err:
            return str(err)

        return self.application.GetAddition(a, b)

    def get_subtraction_route(self, a, b):
        try:
            a = int(a)
        except Exception as err:
            return str(err)

        try:
            b = int(b)
        except Exception as err:
            return str(err)
        print(a, b)
        return self.application.GetSubtraction(a, b)

    def get_multiplication_route(self, a, b):
        try:
            a = int(a)
        except Exception as err:
            return str(err)

        try:
            b = int(b)
        except Exception as err:
            return str(err)

        return self.application.GetMultiplication(a, b)

    def get_division_route(self, a, b):
        try:
            a = int(a)
        except Exception as err:
            return str(err)

        try:
            b = int(b)
        except Exception as err:
            return str(err)

        return self.application.GetDivision(a, b)

    def run(self, host: str = None, port: int = None):
        if not host:
            host = "0.0.0.0"
        if not port:
            port = 8080

        uvicorn.run(self.server, host=host, port=port)
