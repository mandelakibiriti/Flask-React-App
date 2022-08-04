# Flask React App - using React CDN (Version 1.0) with Flask Blueprints
To understand the basics of React I have simply placed [CDN links on the HTML page](https://reactjs.org/docs/cdn-links.html) and routing it through a Flask Route and using Blueprints and Flask-Assets to compile assets and serve it on the frontend.

## Creating and Connecting to Database on MySQL
Install the following dependencies after installing MySQL on local server

> ``` pipenv install flask-sqlalchemy pymysql python-dotenv mysql-connector mysql-connector-python ```

Create database using create_db.py and run it ***only once*** to create the database on MySQL or running it again will overwrite data on the current db if it was created previously. A brief breakdown of how create_db.py works:

### 1. Connecting to MySQL Server:
```
cnx = mysql.connector.connect(
        user = environ.get('Db_Username'),
        password = environ.get('Db_Password'),
        host = environ.get('Db_Host')
    )
```
> [mysql.connector](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html) object has a ```connect()``` constructor which creates a connection to the MySQL server and returns a MySQLConnection object
### 2. Use [Cursor](https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html) to create database:
> ``` my_cursor = cnx.cursor()```

> The MySQLConnection object has a ```cursor() ``` method that allows one to execute MySQL statements. Using the cursor you can create the database that Flask will connect to.

## Creating tables in database
Once the db has been created Flask can create models using SQLAlchemy through the ```config.py`` in the Config class which allows you to connect to the database and setup other configurations to the database.

At the ```__init__.py``` file the db SQLAlchemy object is created and using [app.context](https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/) in the app factory you can initialize the db using the ```init_app()`` function.

After db initialization and our app object has connected to the MySQL database your routes.py or forms.py can be used to manipulate the data that will persisted to the MySQL database. As an example, we create a test user from our ```forms.py``` file.
> Create user through /register route in forms.py
```
    username = "test"
    email = "test@email"
    if username and email:
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="This is a test user",
            admin=False
        )
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
```
> Running the route will create the test user. You can confirm on teh MySQL database using the  ```SELECT * FROM User;``` command
```
+----+----------+------------+---------------------+---------------------+-------+
| id | username | email      | created             | bio                 | admin |
+----+----------+------------+---------------------+---------------------+-------+
|  1 | test     | test@email | 2022-08-03 17:39:42 | This is a test user |     0 |
+----+----------+------------+---------------------+---------------------+-------+
1 row in set (0.00 sec)
```