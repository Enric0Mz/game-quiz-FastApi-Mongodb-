from datetime import datetime
from typing import Optional

from pydantic import Field
from enum import Enum

from .base import BaseSchema, PyObjectId


class QuestionEnum(str, Enum):
    VERY_EASY = "muito facil"
    EASY = "facil"
    MEDIUM = "medio"
    HARD = "dificil"
    VERY_HARD = "muito dificil"


POINT_MULTIPLIERS = {
    QuestionEnum.VERY_EASY: 1,
    QuestionEnum.EASY: 2,
    QuestionEnum.MEDIUM: 3,
    QuestionEnum.HARD: 4,
    QuestionEnum.VERY_HARD: 5,
}


class QuestionTypeSchema(BaseSchema):
    name: QuestionEnum
    point_multiplier: int


class QuestionChoiceSchema(BaseSchema):
    text: str
    is_correct: bool


class ExtendedQuestionChoiceSchema(QuestionChoiceSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")


class QuestionSchema(BaseSchema):
    question: str
    choices: list[QuestionChoiceSchema]
    question_type: QuestionTypeSchema


class CreateQuestionSchema(QuestionSchema):
    created_at: datetime


class QuestionPayloadSchema(BaseSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    question: str
    choices: list[ExtendedQuestionChoiceSchema]
    question_type: QuestionTypeSchema


class UpdateQuestionSchema(BaseSchema):
    question: Optional[str]
    choices: Optional[list[ExtendedQuestionChoiceSchema]]
    question_type: Optional[QuestionTypeSchema]