import random

from odmantic import query
from datetime import datetime

from src.database.connection import DbConnectionHandler
from src.database.repositories.question import QuestionRepository
from src.schemas import question as schemas
from src.models.question import Question


class GetRandonQuestionUseCase:
    def __init__(self, context: DbConnectionHandler) -> None:
        self._repository = QuestionRepository(context)

    async def execute(self):
        result = await self._repository.fetch({})
        return random.choice(result)



class CreateQuestionUseCase:
    def __init__(self, payload: schemas.QuestionSchema, context: DbConnectionHandler) -> None:
        self._repostitory = QuestionRepository(context)
        self._payload = payload

    async def execute(self):
        return await self._repostitory.create(
            schemas.CreateQuestionSchema(
                created_at=datetime.now(), **self._payload.dict()
            )
        )


class DeleteQuestionUseCase:
    def __init__(self, question_id: str, context: DbConnectionHandler) -> None:
        self._repository = QuestionRepository(context)
        self._question_id = question_id

    async def execute(self):
        await self._repository.delete(
            query.eq(Question.id, self._question_id)
        )


class UpdateQuestionUseCase:
    def __init__(self, question_id: str, context: DbConnectionHandler, payload: schemas.UpdateQuestionSchema) -> None:
        self._repository = QuestionRepository(context)
        self._question_id = question_id
        self._payload = payload

    async def execute(self):
        return await self._repository.update(query.eq(Question.id, self._question_id), self._payload)
