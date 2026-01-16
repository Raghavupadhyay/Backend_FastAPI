from fastapi import FastAPI
from app.api import auth, users, items
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

# API
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)
