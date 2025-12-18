from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, database, auth

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post(
    "/", 
    response_model=schemas.PostResponse,
    summary="Create a new post",                 # 1. Short summary (collapsed view)
    response_description="The created post object", # 2. Description of the response
    status_code=status.HTTP_201_CREATED
)
def create_post(
    post: schemas.PostCreate, 
    db: Session = Depends(database.get_db), 
    current_user: models.User = Depends(auth.get_current_user)
):
    """
    # Create a new Post
    
    This endpoint allows a logged-in user to create a new post.
    
    - **title**: The title of the post (required)
    - **content**: The body of the post (required)
    
    The post will be automatically linked to the **current authenticated user**.
    """
    new_post = models.Post(**post.dict(), user_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=List[schemas.PostResponse])
def read_posts(db: Session = Depends(database.get_db)):
    return db.query(models.Post).all()