Certainly! Here’s a detailed README.md for your Django project, outlining the installation method, creating a superuser, running migrations, and running the application.

```markdown
# Resume Upload Application

This is a Django-based application that allows users to register, log in, upload resumes in CSV format, and view their resumes. Admin users can view all registered users and their uploaded resumes.

## Table of Contents

- [Installation](#installation)
- [Creating Superuser](#creating-superuser)
- [Running Migrations](#running-migrations)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Available Endpoints](#available-endpoints)

## Installation

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.12+
- pip (Python package installer)
- virtualenv (optional but recommended)

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/TTKhumalo/resume_upload_app.git
   cd resume_upload_app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```sh
   python manage.py migrate
   ```

## Creating Superuser

To access the Django admin interface, you need to create a superuser.

1. **Create superuser:**
   ```sh
   python manage.py createsuperuser
   ```

2. Follow the prompts to enter your username, email, and password.

## Running Migrations

Whenever you make changes to your models, you need to create and apply migrations.

1. **Create migrations:**
   ```sh
   python manage.py makemigrations
   ```

2. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

## Running the Application

To start the development server, use the following command:

```sh
python manage.py runserver
```

Then, open your browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

## Test data

Use the csv located in `csv` folder


## Project Structure

```
resume_upload_app/
│
├── resume_manager/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── tailwind.css
│   ├── templates/
│   │   ├── admin_view_users.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── register.html
│   │   ├── upload_resume.html
│   │   ├── view_resume.html
│   │   ├── view_user_resumes.html
│   │   └── registration/
│   │       └── login.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

## Available Endpoints

- `/` - Home page
- `/register/` - User registration page
- `/login/` - User login page
- `/logout/` - User logout
- `/upload_resume/` - Upload resume page (authenticated users)
- `/view_resume/` - View uploaded resume (authenticated users)
- `/admin_view_users/` - View all users (admin only)
- `/view_user_resumes/<int:user_id>/` - View resumes of a specific user (admin only)
- `/admin/` - Django admin interface (admin only)

## Additional Notes

- Ensure you have configured your `settings.py` correctly for the database, static files, and media files.
- For production deployment, remember to set `DEBUG = False` and configure a proper database and static/media file handling.




## Steps to Build and Run the Docker Container

1. **Build the Docker image**
    Navigate to the root directory of your project (where the Dockerfile is located) and run:

    ```sh
    docker build -t resume_upload_app .
    ```
2. **Run the Docker container:**

    ```sh
    docker run -p 8000:8000 resume_upload_app
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

---

Feel free to reach out if you have any questions or need further assistance.

```

Copy this content into a `README.md` file in the root of your project. It provides comprehensive instructions and details about your Django application, ensuring anyone can set it up and run it smoothly.



