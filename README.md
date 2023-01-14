#  BlogPostsAPI

[![My Skills](https://skills.thijs.gg/icons?i=vue,django,python,js,html,css)](https://skills.thijs.gg)

This simple project was intended to practice FullStack Development, using Django and Django REST Framework for the backend and
Vue.js for the frontend. It is a simple blog, where any user can post using his name, email and photo, as well as have CRUD ability. 


# 🚀 How to Run the project 

## Backend
  At the root folder, start running a python venv and activating it:
  ```cmd 
    python -m venv venv  
    cd .\venv\Scripts\
    ./activate/
   ```
  Install all the packages required at requirements.txt:
  
  ```cmd
    pip install -r requirements.txt
  ```
  Make migrations and migrate as usual in Django projects:
  
  ```cmd
    python manage.py makemigrations
    python manage.py migrate
  ```
  Create your admin superuser:
  
  ```cmd
    python manage.py createsuperser
  ```
  Run the server: 
  
  ```cmd
    python manage.py runserver
  ```
  
  ## Frontend
  Navigate to the frontend folder and install the dependecies: 
  ```cmd
    npm install 
  ```
  Run the server: 
  ```cmd
    npm run serve
  ```
  
  # :dart: Backend Tests
  
  Some tests were implemented for the api endpoints at test.py in the blogposts folder.
  To run them, just run python manage.py test:
  
  ```cmd
    python manage.py test
  ```
