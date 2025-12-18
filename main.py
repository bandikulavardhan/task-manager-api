from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import models, schemas, auth
from database import SessionLocal, engine
from typing import List, Optional

models.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}

# This helps us talk to the database for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

@app.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Check if username already exists
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # 2. Hash the password
    hashed_pass = auth.get_password_hash(user.password)
    
    # 3. Save to database
    new_user = models.User(username=user.username, hashed_password=hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    # 1. Find user by username
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    
    # 2. Check if user exists and password is correct
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # 3. Create the token
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# 1. Create a New Task
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, 
                db: Session = Depends(get_db), 
                current_user: models.User = Depends(get_current_user)):
    new_task = models.Task(**task.dict(), owner_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# 2. Get All My Tasks (with optional priority search)
@app.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(priority: Optional[str] = None, 
              db: Session = Depends(get_db), 
              current_user: models.User = Depends(get_current_user)):
    query = db.query(models.Task).filter(models.Task.owner_id == current_user.id)
    
    # If the user searches for a priority (like ?priority=High), filter the results
    if priority:
        query = query.filter(models.Task.priority == priority)
        
    return query.all()

from typing import List, Optional

# 1. Create a Task (Only for logged-in users)
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, 
                db: Session = Depends(get_db), 
                current_user: models.User = Depends(get_current_user)):
    # .model_dump() converts the Pydantic object into a Python dictionary
    new_task = models.Task(**task.model_dump(), owner_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# 2. Get All My Tasks (Includes searching by priority)
@app.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(priority: Optional[str] = None, 
              db: Session = Depends(get_db), 
              current_user: models.User = Depends(get_current_user)):
    # Start by getting only the tasks owned by the current user
    query = db.query(models.Task).filter(models.Task.owner_id == current_user.id)
    
    # If the user provides a priority (e.g., /tasks?priority=High), filter the results
    if priority:
        query = query.filter(models.Task.priority == priority)
        
    return query.all()