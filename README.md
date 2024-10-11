# Assignment Submission Portal

A Django-based portal for users to upload assignments and admins to manage them, with MongoDB as the database.

## Features

- **Users** can register, log in, and upload assignments.
- **Admins** can register, log in, and manage assignments (accept/reject).

## Tech Stack

- **Backend:** Django
- **Database:** MongoDB
- **Authentication:** Django’s built-in authentication

## Setup Instructions

### Prerequisites

- Python 3.x
- MongoDB (local or MongoDB Atlas)
- Git

### Installation

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/your-username/assignment-submission-portal.git
   cd assignment-submission-portal

2.  **Set Up Virtual Environment:**



    ```bash
    python -m venv env
    source env/bin/activate   # Windows: env\Scripts\activate

3.  **Install Dependencies:**



    ```bash
    pip install -r requirements.txt

5.  **Configure MongoDB:** Update the `DATABASES` setting in `settings.py` with your MongoDB details.

6.  **Run Migrations:**



    ```bash
    python manage.py migrate

7.  **Run the Server:**



    ```bash
    python manage.py runserver

API Endpoints
-------------

-   **User Registration:** `POST /users/register/`
-   **Admin Registration:** `POST /users/register/`
-   **Login:** `POST /users/login/`
-   **Upload Assignment:** `POST /assignments/upload/`
-   **Get Admins List:** `GET /users/admins/`
-   **View Assignments (Admin):** `GET /assignments/`
-   **Accept/Reject Assignment:** `POST /assignments/{id}/{action}/`

Testing
-------

Use Postman or another tool to test the endpoints with sample data.

License
-------

This project is licensed under the MIT License.
