## Project Setup

prequisites - 
python

1. Clone this repo
git clone <your-repo-url>
cd <your-project-directory>

2. Create a virtual env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. install the requirements
pip install -r requirements.txt

4. run migrations
python manage.py makemigrations
python manage.py migrate

5. start your server
python manage.py runserver


## implemented Features

1. User CRUD Endpoints

Role-based access for:

    Admin/Manager: Can create, read, update, delete any user.

Endpoints:

    POST /api/users/ – Create user (Admin & Manager)

    GET /api/users/ – List users (Admin & Manager)

    GET /api/users/<int:pk>/ – Retrieve user  (Admin & Manager)

    PUT /api/users/<int:pk>/ – Update user (Admin & Manager)

    DELETE /api/users/<int:pk>/ – Delete user (Admin & Manager)

2. Task CRUD Endpoints

Role-based access:

    Admin/Manager: Can create, view, update, and delete task.

    User: Can view and update tasks.

Endpoints:

    POST /api/tasks/create – Create task

    GET /api/tasks/ – List tasks

    GET /api/tasks/<int:pk>/ – Retrieve task

    PUT /api/tasks/<int:pk>/update/ – Update task

    DELETE /api/tasks/<int:pk>/delete/ – Delete task

3. Check Inactive User Command

Command to deactivate inactive users.

    python manage.py check_inactive_users

4. Reactivate User Endpoint

Role-based access:

    Admin/Manager: Reactivate  user

EndPoints:

    POST /api/users/<int:pk>/reactivate/'


## Notes
Postman collection link - 
https://.postman.co/workspace/Local~97a852b1-b21a-48d5-9238-dfd2d0521cbc/collection/38623284-234b8def-58a2-4663-9ff4-cba151147cdd?action=share&creator=38623284
