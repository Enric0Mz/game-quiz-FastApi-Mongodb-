from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from yarl import URL

from src.core import settings


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_uri = URL.build(scheme="mongodb", user=settings.USERNAME, password=settings.PASSWORD, host=settings.DB_HOST, port=settings.PORT)
        self.__database_name = settings.DB_NAME
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        connection_uri_str = self.__connection_uri.human_repr()
        self.__client = AsyncIOMotorClient(connection_uri_str)
        self.__db_connection = AIOEngine(
            client=self.__client, database=self.__database_name
        )

    def acquire_session(self):
        return self.__db_connection

    def acquire_client(self):
        connection_uri_str = self.__connection_uri.human_repr()
        return AsyncIOMotorClient(connection_uri_str)

    def transaction_begin(self):
        return self.__db_connection.transaction()

    def connection_close(self):
        return self.__client.close
