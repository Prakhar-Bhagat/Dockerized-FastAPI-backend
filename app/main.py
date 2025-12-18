import logging
from fastapi import FastAPI, Request
from app.database import engine, Base
from app.routers import users, posts

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Request completed with status: {response.status_code}")
    return response

app.include_router(users.router)
app.include_router(posts.router)

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the API!"}