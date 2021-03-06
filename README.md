# Better Together Fitness - developed using Django with Django allauth. 
# Deployed on AWS using s3 and IAM. 

##  **Setting up Django and Allauth.**
The workplace has been set up using the Code Institute Template they provided during the course..

# To set up Django:
1. pip3 install Django <br>
This install Django onto the workspace. <br>

2. django-admin startproject PROJECTNAME . <br>
This creates the project in the current directory. It creates a Django project folder, which includes the settings.py, urls.py and other files. <br>

3. Create a .gitignore file.<br>
Add:<br>
 *.sqlite3<br>
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

# To set up Allauth:

A powerful pre-built open-sourced authentication system, gives users the ability to log in, log out and register for an account etc. 

1. Install allauth:<br>
pip3 install django-allauth==0.41.0

2. Navigate to settings.py to add some allauth settings from the documentation. (https://django-allauth.readthedocs.io/en/latest/installation.html) 

3. In the templates, context processors, make sure the following is included:
'django.template.context_processors.request', <br>


4. Add the following authentication backends and SITE_ID underneath the templates section in settings.py:<br>
AUTHENTICATION_BACKENDS = [ 
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

]<br>

SITE_ID =1 

5. Add the following apps to installed apps in settings.py:<br>
'django.contrib.sites',<br>
    'allauth',<br>
    'allauth.account',<br>
    'allauth.socialaccount'<br>

6. Navigate to the project level urls.py and add the allauth urls and import 'include' at the top:<br>
path('accounts/', include('allauth.urls')),

7. Run migrations to update the database:<br>
python3 manage.py migrate

8. Run server and navigate to admin page and log in.<br>
Under the sites heading updated the default site to 
betterTogetherFitness.axample.com<br>
Change the display name to betterTogetherFitness<br>
Not a critical setting but it would be if we were using social media authentication. 

9. In settings.py add the following setting:<br>
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'<br>
This logs the confirmation emails to the console temporarily whilst being made.

10. Add the following settings:<br>
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'<br>
ACCOUNT_EMAIL_REQUIRED = True<br>
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'<br>
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True<br>
ACCOUNT_USERNAME_MIN_LENGTH = 4<br>
LOGIN_URL = '/accounts/login/'<br>
LOGIN_REDIRECT_URL = '/'<br>

These are settings that tell allauth what is required when a user registers. 

11. Go to django admin and manually verify an email by:<br>
Clicking on email addresses under the accounts section<br>
Add new email<br>
Select the superuser already created (click on magnifying glass image).<br>
Select verified and primary. 

12. Test it by running server and navigate to /accounts/login

13. Run pip3 freeze > requirements.txt

14. Set up templates directories:<br>
mkdir templates<br>
mkdir templates/allauth (allauth templates will live in here.)

15. Make copies of allauth templates in the new templates/allauth folder so that we can customize them later.:<br>
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/


# Create a base.html template

The base.html template for. th eproject itself in which every other html pgae will be extended from. <br>
Create base.html in the project level templates folder.<br><br>
Organize base template into blocks so it can be easily edited or removed in other templates throughout the project.

# Creating new app (I have used the home app for an example)

1. python3 manage.py startapp home - This creates the app. 

2. Create a templates directory in the home app.<br>
mkdir -p home/templates/home

3. Create an index.html file in the templates/home directory. 

4. In index.html add the {% extends 'base.html' %} {% load static %} tags at the top to extend the base.html and load the static pages.<br>
Main content for the page will go inside the {% block content %} tags.

5. In the views.py file:<br>
def index(request):<br>

    return render(request, 'home/index.html')  <br>

6. Create a urls.py file in the home app and copy and paste contents of other urls.py file to use as a shell.<br>
Add a url path to render the views for index.html. <br>
Import views at the top of the page 'from . import views'

7. Go to project level urls.py page and add the path for the home app urls:<br>
***path('', include('home.urls')),***

8. Add the home app to list of installed apps in settings.py.

9. Add the route templates directory to the dirs setting in settings.py:<br>
***os.path.join(BASE_DIR, 'templates'),<br>
os.path.join(BASE_DIR, 'templates', 'allauth'),***<br>

# Setting up static files. 

1. Create required folders:<br>
mkdir static<br>
mkdir static/css<br>
mkdir media<br>

2. Create base.css fold in css folder.

3. Add the following in the settings.py:

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

4. In the root level urls.py file add:<br>
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)<br><br>

Make sure the following is included in the imports of the urls.py file.<br>
***from django.conf import settings<br>
from django.conf.urls.static import static***<br>

