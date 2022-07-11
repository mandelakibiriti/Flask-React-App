# Flask React App
[Flask](https://github.com/pallets/flask) is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications using several [plugins](https://github.com/humiaozuzu/awesome-flask).
> Flask version used is 2.1.2
## 1. [Virtual Environments](https://realpython.com/pipenv-guide/)
Preference used in creating a virtual environment is pipenv. 
- Install pipenv using pip:
    > ```$ pip install pipenv```
- Create virtual environment
    > ```$ pipenv shell```
- Install dependencies of your virtual environment from Pipfile: 
    > ```$ pipenv install```
- Installing using pipenv from requirements.txt
    > ```$ pipenv install -r requirments.txt```
- Lock dependencies to your Pipfile.lock file
    > ```$ pipenv lock```

## 2. [Project Layout for a Flask App](https://hackersandslackers.com/flask-application-factory/)
Python projects use packages to organize code into multiple modules that can be imported where needed. 

For larger applications it’s a good idea to use a package instead of a module. 

> To convert simple packages into a larger one, just create a new folder yourapplication inside the existing one and move everything below it. The Flask-App project directory will contain another Flask-App directory inside the existing one and move everything below it.

> Then rename yourapplication.py to ```__init__.py```. (Make sure to delete all .pyc files first, otherwise things would most likely break). 

> Notice there's no ```app.py, main.py```, or anything of the sort in our base directory. Instead, the entirety of our app lives in the /Flask-App/FlaskApp folder, with the creation of our app happening in ```__init__.py```.
```
/Flask-App (base directory)
├── /FlaskApp
│   ├── __init__.py (Application Factory where app is initialized)
│   ├── auth.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── /static
│   └── /templates
│   └── /tests
├── config.py (app configurations)
└── wsgi.py (imports and serves as our app gateway)
```

## 3. Structuring Flask App using Blueprints
Blueprints are Flasks' python equivalent for modules which allows to structure your app by items of concern where several app features are organized as collections with standalone modules, services or classes.
> Note: You would need register a blueprint. The downside is that you cannot unregister a blueprint once an application was created without having to destroy the whole application object.

> While blueprints cannot access the templates or static files of their peers, they can utilize common assets to be shared across all blueprints (such as a layout.html template, or a general style.css file that applies to all parts of our app)

> While registering a blueprint using [app_context](https://flask.palletsprojects.com/en/2.1.x/appcontext/) using the ```current_app``` proxy which points to the application handling the current activity.
```
/flask-blueprint-tutorial
├── /flask_blueprint_tutorial
│   ├── __init__.py
│   ├── assets.py
│   ├── api.py
│   ├── /home
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /profile
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /products
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /static 
│   └── /templates
├── config.py
└── wsgi.py
```
## [4. Ensuring Flask App config variables are in config.py](https://hackersandslackers.com/configure-flask-applications)
This is where config variables are stated. Config variables areorganized set of instructions that are defined before our app is live.
> Moreover, it's much easier to avoid compromising sensitive secrets such as AWS or database credentials when we manage these things in one place. Let's explore our better options.

## [5. React with Flask Assets](https://flask-assets.readthedocs.io/en/latest/)
Flask Assets allow you to compile your web assets into common files of concern depending on the page or route in quesiton allowing you to manage concerns adequately.

## Credits
1. Todd Birchard - [hackersandslackers Flask Tutorial](https://hackersandslackers.com/series/build-flask-apps/)
2. Bob Ziroll - [Learn React For Beginners](https://scrimba.com/learn/learnreact)
3. Real Python - [Flask Tutorial](https://realpython.com/python-web-applications-with-flask-part-i/)