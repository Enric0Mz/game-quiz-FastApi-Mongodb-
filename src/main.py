from fastapi import FastAPI
from src.routes.core import router


app = FastAPI(title="Game Api", version="0.1.0", debug=True)
app.include_router(router)
