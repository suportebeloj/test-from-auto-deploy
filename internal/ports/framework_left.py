from fastapi import FastAPI
from internal.ports.app import APIInterface
from internal.ports.framework_right import DbportInterface


class HTTPAPIInterface:

    def __init__(self, http_server_instance: FastAPI, database_adapter: DbportInterface = None, application_adapter: APIInterface = None):
        self.server = http_server_instance
        self.database = database_adapter
        self.application = application_adapter

    def get_addition_route(self, a, b):
        pass

    def get_subtraction_route(self, a, b):
        pass

    def get_multiplication_route(self, a, b):
        pass

    def get_division_route(self, a, b):
        pass

    def run(self, host:str=None, port:int=None):
        pass
