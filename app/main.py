import logging
from fastapi import FastAPI, Request
from app.database import engine, Base
from app.routers import users, posts

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with **users**. The **login** logic is also here.",
    },
    {
        "name": "Posts",
        "description": "Manage posts. One user can own _multiple_ posts.",
    },
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Blog API",
    description="A robust API for managing users and posts. Built with **FastAPI** and **PostgreSQL**.",
    version="1.0.0",
    
    openapi_tags=tags_metadata # Apply the tag descriptions
)


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