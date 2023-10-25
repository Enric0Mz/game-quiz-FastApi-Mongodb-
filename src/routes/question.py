from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends

from src.database.connection import DbConnectionHandler
from src.schemas.question import QuestionSchema, QuestionPayloadSchema
from src.domain import question as domain


router = APIRouter()


@router.get("/", response_model=QuestionPayloadSchema)
async def get_question(
    context: DbConnectionHandler = Depends()
):
    return await domain.GetRandonQuestionUseCase(context).execute()


@router.post("/")
async def create_question(
    payload: QuestionSchema = Body(...),
    context: DbConnectionHandler = Depends()
):
    return await domain.CreateQuestionUseCase(payload, context).execute()
