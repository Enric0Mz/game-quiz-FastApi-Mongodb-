import random

from datetime import datetime

from src.database.connection import DbConnectionHandler
from src.database.repositories.question import QuestionRepository
from src.schemas.question import QuestionSchema, CreateQuestionSchema
from src.models.question import Question


class GetRandonQuestionUseCase:
    def __init__(self, context: DbConnectionHandler) -> None:
        self._repository = QuestionRepository(context)

    async def execute(self):
        result = await self._repository.fetch({})
        return random.choice(result)



class CreateQuestionUseCase:
    def __init__(self, payload: QuestionSchema, context: DbConnectionHandler) -> None:
        self._repostitory = QuestionRepository(context)
        self._payload = payload

    async def execute(self):
        return await self._repostitory.create(
            CreateQuestionSchema(
                created_at=datetime.now(), **self._payload.dict()
            )
        )        
