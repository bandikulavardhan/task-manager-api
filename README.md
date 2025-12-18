Task Manager API

📝 About the Project

This is a backend API designed to help users manage their daily tasks efficiently. It allows users to create, view, update, and delete tasks (CRUD operations) while ensuring data is stored securely in a database.

🚀 Key Features

* User Authentication: Secure login and signup to keep user tasks private.
* Task Management: Full CRUD (Create, Read, Update, Delete) functionality for tasks.
* Search & Filter: Find tasks easily by their **priority** or **due date**.
* Database Integration: Uses a SQL database to store information reliably.
* Containerization: Fully Dockerized for easy setup on any machine.

🛠️ Tech Stack

* Language: [Python (FastAPI/Flask) OR Java (Spring Boot)]
* Database: SQL (PostgreSQL/MySQL)
* DevOps: Docker & Docker Compose
* Tools: Postman (for API testing)

## 🛣️ API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| **POST** | `/api/auth/register` | Create a new user account |
| **POST** | `/api/auth/login` | Login and get a token |
| **GET** | `/api/tasks` | Get all tasks for the logged-in user |
| **POST** | `/api/tasks` | Create a new task |
| **PUT** | `/api/tasks/{id}` | Update an existing task |
| **DELETE** | `/api/tasks/{id}` | Delete a task |

💻 How to Run the Project

1. Prerequisites

* [Python / Java] installed
* Docker installed (optional)

2. Using Docker (Recommended)

  1. Open your terminal in the project folder.
  2. Run the following command:
  Bash
  docker-compose up --build
  3. The API will be live at `http://localhost:8000` (or your chosen port).

3. Manual Setup

1. Install dependencies:
`[pip install -r requirements.txt OR ./mvnw install]`
2. Set up your database environment variables.
3. Start the server:
`[python main.py OR ./mvnw spring-boot:run]`
