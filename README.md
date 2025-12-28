# 📝 Task Manager API

A robust backend service designed for efficient daily task management. This API provides a secure way for users to handle their to-do lists with full CRUD functionality, authentication, and persistent storage.

## 🚀 Key Features
* **User Authentication:** Secure signup and login using JWT (JSON Web Tokens) to protect user data.
* **Task Management:** Full CRUD (Create, Read, Update, Delete) operations.
* **Search & Filter:** Advanced filtering to find tasks by **priority** or **due date**.
* **Database Persistence:** Integrated with a SQL database (PostgreSQL/MySQL) for reliable data storage.

## 🛠️ Tech Stack
* **Language:** Python (FastAPI/Flask) / Java (Spring Boot) 
* **Database:** SQL (PostgreSQL / MySQL)
* **Authentication:** JWT
* **Tools:** Postman / Insomnia (for API testing)

## 🛣️ API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/api/auth/register` | Create a new user account |
| **POST** | `/api/auth/login` | Login and receive Auth Token |
| **GET** | `/api/tasks` | Fetch all tasks for the logged-in user |
| **POST** | `/api/tasks` | Create a new task |
| **PUT** | `/api/tasks/{id}` | Update an existing task |
| **DELETE** | `/api/tasks/{id}` | Remove a task from the database |

## 💻 Local Installation & Setup

Follow these steps to get the API running on your machine:

### 1. Clone the Repository
`git clone [https://github.com/your-username/task-manager-api.git](https://github.com/your-username/task-manager-api.git)`
`cd task-manager-api`

### 2. Set Up the environment
# Create and activate virtual environment
`python -m venv venv`
`venv\Scripts\activate`

# Install dependencies
`pip install -r requirements.txt`

### 3. Database Configuration
`set DB_URL=postgresql://username:password@localhost:5432/task_manager`
`set SECRET_KEY=your_jwt_secret_key`

### 4. Run the application
`unicorn main:app --reload`

The API will be live at: http://localhost:8000
