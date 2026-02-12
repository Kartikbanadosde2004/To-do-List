To-Do List Application
1.Project Overview

Purpose: This is a simple web application that helps users manage their daily tasks. It allows users to create a list of things they need to do, update them when they are finished, and delete them if they are no longer needed.

2. Requirements :

2.1 User Accounts
Registration: A new user can create an account with a username and password.

Login: The user can log in to see their personal tasks.

Security: Passwords are not saved as plain text; they are "hashed" (scrambled) for safety.

Logout: The user can sign out to protect their account.

2.2  Managing Tasks (CRUD)
Create: Add a new task with a title and priority (High, Medium, Low).

Read: View a list of all pending and completed tasks.

Update: Change a task's details or mark it as "Done".

Delete: Permanently remove a task from the list.

3. Technical Tools
3.1 Backend (Logic)
Python: The main programming language.

Flask: A lightweight tool (framework) that helps Python build websites. It handles the links (URLs) and logic.

3.2 Database (Storage)
MySQL: The database used to store user info and tasks.

3.3 Frontend (Design)
HTML: Creates the structure of the pages (forms, buttons, lists).
CSS: Makes the pages look good (colors, layout).

4. Diagrams

4.1 System Flow

flowchart TD
    Start([Start]) --> Login[Login Page]
    Login --> Check{Password Correct?}
    
    Check -- No --> Login
    Check -- Yes --> Dashboard[User Dashboard]

    Dashboard --> Choice{What to do?}
    
    Choice --> Add[Add New Task]
    Choice --> Edit[Edit Task]
    Choice --> Delete[Remove Task]
    Choice --> Done[Mark as Completed]
    
    Add --> Save[Save to Database]
    Edit --> Save
    Delete --> Save
    Done --> Save
    
    Save --> Dashboard
    Dashboard --> Logout([Logout])

    4.2 Use Case Diagram

    graph TD
    User((User))
    System[To-Do App]

    User -->|Register & Login| System
    User -->|Add Task| System
    User -->|Edit Task| System
    User -->|Delete Task| System
    User -->|Complete Task| System

    4.3 ER Diagram (Database Design)

    erDiagram
    USER ||--o{ TASK : "has"

    USER {
        int id PK
        string username
        string password
    }

    TASK {
        int id PK
        int user_id FK
        string title
        string status
        string priority
    }
    }
