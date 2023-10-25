from odmantic import Model, EmbeddedModel

from .choice import Choice


class GameQuestion(EmbeddedModel):
    name: str
    point_multiplier: int


class Question(Model):
    question: str
    question_type: GameQuestion
    choices: list[Choice]
