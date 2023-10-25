from fastapi import APIRouter

from . import question


router = APIRouter(prefix="/api")


@router.get("/health-check")
def health():
    return {"status": "ok"}


router.include_router(question.router, prefix="/question", tags=["Question"])
