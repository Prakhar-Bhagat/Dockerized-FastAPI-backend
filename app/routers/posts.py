from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, database, auth

router = APIRouter(
    prefix="/posts", # All endpoints here will start with /posts
    tags=["Posts"]
)

@router.post("/", response_model=schemas.PostResponse)
def create_post(
    post: schemas.PostCreate, 
    db: Session = Depends(database.get_db), 
    current_user: models.User = Depends(auth.get_current_user)
):
    new_post = models.Post(**post.dict(), user_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=List[schemas.PostResponse])
def read_posts(db: Session = Depends(database.get_db)):
    return db.query(models.Post).all()