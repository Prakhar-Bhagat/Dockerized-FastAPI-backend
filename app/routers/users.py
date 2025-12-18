import logging
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import schemas, models, database, auth

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Users"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    logger.info(f"Attempting to create user: {user.email}") # <--- Log entry
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email registered")
    
    hashed_pw = auth.get_password_hash(user.password)
    new_user = models.User(email=user.email, username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()

    logger.info(f"User created successfully: {user.email}") # <--- Log success
    return {"message": "User created"}

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    # Swagger sends the email in the 'username' field
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        logger.error(f"Login failed for email: {form_data.username}") # <--- Log error
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    logger.info(f"User logged in: {user.email}")
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}