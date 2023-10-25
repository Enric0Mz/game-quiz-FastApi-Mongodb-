from typing import Optional

from src.database.connection import DbConnectionHandler\


exc = None #TODO create exc module


class Repository:
    __abstract__ = True

    def __init__(self, context: DbConnectionHandler) -> None:
        self.context = context
        self.context.connect_to_db()
        self.context.transaction_begin()

    def does_not_exist(self, value: Optional[str] = ""):
        return exc.not_found_error(
            value, type(self).__name__.removesuffix("Repository")
        )

    def count_response(self, value: int):
        return {
            "message": f"{value} instances were added to the database.",
            "status_code": 201,
        }
