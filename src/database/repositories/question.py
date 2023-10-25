from odmantic.query import QueryExpression

from src.database.repositories.base import Repository
from src.models.question import Question
from src.schemas.question import QuestionSchema, QuestionPayloadSchema


class QuestionRepository(Repository):
    def to_dto(self, obj: Question) -> QuestionSchema:
        return QuestionPayloadSchema.parse_obj(
            {
                "_id": obj.id,
                "question": obj.question,
                "question_type": obj.question_type,
                "choices": [
                    choice for choice in obj.choices
                ]
            }
        )

    async def fetch(self, filter: QueryExpression):
        result = await self.context.acquire_session().find(
            Question, filter
        )
        return [self.to_dto(item) for item in result if item is not None]


    async def create(self, payload: QuestionSchema):
        result = await self.context.acquire_session().save(
            Question(**payload.dict())
        )
        return result
