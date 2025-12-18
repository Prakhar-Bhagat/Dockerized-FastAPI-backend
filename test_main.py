from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Import your app and data tools
from app.main import app
from app.database import Base, get_db

# --- 1. Test Database Setup ---
# Use SQLite in-memory for fast, isolated tests. 
# "check_same_thread=False" is needed for SQLite with FastAPI.
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool, # Keeps data in memory during the test
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- 2. Override the Dependency ---
def override_get_db():
    try:
        db = TestingSessionLocal()
        # Create tables (empty) for the test
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        db.close()
        # Drop tables after test (clean slate)
        Base.metadata.drop_all(bind=engine)

# Swap the real get_db for our test one
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# --- 3. The Test Case ---

def test_create_user():
    # Arrange: Define the user data
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    
    # Act: Send a POST request to the signup endpoint
    response = client.post("/signup", json=user_data)
    
    # Assert: Check if the response is what we expect
    assert response.status_code == 201  # Should be 'Created'
    assert response.json() == {"message": "User created"}