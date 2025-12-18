from pydantic import BaseModel, Field

# Post Schemas 
class PostBase(BaseModel):

    title: str = Field(
        ..., 
        description="The headline of the post", 
        min_length=5,
        max_length=100,
        example="My First Blog Post" 
    )
    content: str = Field(
        ..., 
        description="The main content body", 
        example="This is the content of my very first post."
    )

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    user_id: int
    
    class Config:
        from_attributes = True

        json_schema_extra = {
            "example": {
                "title": "My First Blog Post",
                "content": "This is the content of my very first post.",
                "id": 1,
                "user_id": 42
            }
        }

# User Schemas 
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str