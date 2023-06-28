# Micro Blog Django-rest-framework

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/webcam121/MicroBlog.git
```

Second, go to the main project:

```bash
cd Microblog
```

Create virtual environment

```bash
python -m venv my_env
```
Activate virtual environment on Windows:
```bash
.\venv\Scripts\activate
```
Activate virtual environment on linux:
```bash
source my_env/bin/activate
```


Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

Install PosgreSQL

```bash
sudo su - postgres
```

```bash
psql
```

```bash
CREATE DATABASE microblog;
```
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
Admin page: **localhost:8000/admin/**

User Register **127.0.0.1:8000/users/register**

User login **127.0.0.1:8000/users/login**

blog endpoint **127.0.0.1:8000/api/post**
