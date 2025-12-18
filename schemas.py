from pydantic import BaseModel

# What the user sends when they sign up
class UserCreate(BaseModel):
    username: str
    password: str

# What the API sends back (we don't send the password back!)
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

# What the user sends to create a task
class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str

# What the API sends back to the user
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    owner_id: int

    class Config:
        from_attributes = True

# What the user sends to create a task
class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str # Example: High, Medium, Low

# What the API sends back to the user
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    owner_id: int

    class Config:
        from_attributes = True