# To-do-List
## Diagrams
### 1. System Flow Diagram
```mermaid
flowchart TD
    A[User] --> B[Register / Login]
    B --> C[Authentication & Session]
    C --> D[Create Task]
    D --> E[Edit / Delete Task]
    E --> F[Update Status]
    F --> G[View Task History]
    G --> H[Logout]
```

### 2. Use Case Diagram
```mermaid
graph TD
    Student -->|Register / Login| System
    Employee -->|Create Task| System
    Manager -->|Edit Task| System
    Student -->|Delete Task| System
    Admin -->|Monitor Users| System
```

### 3. ER Diagram
```mermaid
erDiagram
    USER ||--o{ TASK : manages

    USER {
        int user_id
        string username
        string password
        string role
    }

    TASK {
        int task_id
        string title
        string priority
        string status
    }
```


1. Purpose
It is to help users manage their daily tasks efficiently.
The system allows users to create, update, and track tasks so that they can organize their work and improve productivity.

2. Users
The users of the system include:
•	Employees
•	Managers
•	Admin
3. Scope
•	Creating and managing daily tasks
•	Updating task status 
•	Viewing task lists based on priority
•	Secure user login and task management
•	Admin monitoring user activity
4. Functional Requirements
•	User registration and login
•	User authentication using username and password
•	Create new tasks
•	Edit existing tasks
•	Delete tasks
•	Mark tasks as completed
•	View task history
5. Technical and Backend Technology
•	Programming Language: Python
•	Framework: Flask
•	Database:MySQL
6. Frontend Technology
•	HTML
•	CSS


