# Better Together Fitness - developed using Django with Django allauth. 
# Deployed on AWS using s3 and IAM. 

##  **Setting up Django and Allauth.**
The workplace has been set up using the Code Institute Template they provided during the course..

### To set up Django:
1. pip3 install Django <br>
This install Django onto the workspace. <br>

2. django-admin startproject PROJECTNAME . <br>
This creates the project in the current directory. It creates a Django project folder, which includes the settings.py, urls.py and other files. <br>

3. Create a .gitignore file.<br>
Add:<br>
 *.sqlite2<br>
*.pyc<br>
__pycache__/ <br>

4. Run inital migrations by running the command:<br>
python3 manage.py migrate<br>

5. Create superuser by running command<br>
python3 manage.py createsuperuser

6. Create requirements.txt file by running command:<br>
pip3 freeze > requirements.txt<br>

7. To run the server use the command:<br>
python3 manage.py runserver

### To set up Allauth: